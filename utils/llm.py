"""
LLM integration utility for content and reply generation.
Supports OpenAI, Gemini, and Ollama (local) with centralized config.
"""
import os
from enum import Enum
from typing import Optional
from config.settings import Config
import openai
import google.generativeai as genai
import requests
import ollama

# Gemini stub import (to be implemented)
# from google.generativeai import GenerativeModel

class LLMProvider(Enum):
    OPENAI = 'openai'
    GEMINI = 'gemini'
    OLLAMA = 'ollama'

class LLMModel(Enum):
    # OpenAI
    GPT_4O = 'gpt-4o'
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    # Gemini
    GEMINI_FLASH = 'gemini-1.5-flash'
    GEMINI_PRO = 'gemini-1.5-pro'
    # Ollama
    OLLAMA_LLAMA3 = 'llama3'
    OLLAMA_MISTRAL = 'mistral'
    # Add more as needed

def get_api_key(provider: LLMProvider) -> Optional[str]:
    if provider == LLMProvider.OPENAI:
        return Config.OPENAI_API_KEY
    elif provider == LLMProvider.GEMINI:
        return Config.GEMINI_API_KEY
    return None  # Ollama does not need a key

def generate_with_llm(prompt: str, model: LLMModel = LLMModel.GPT_4O, max_tokens: int = 256, provider: LLMProvider = LLMProvider.OPENAI) -> str:
    """
    Generate content using an LLM (OpenAI, Gemini, or Ollama).
    """
    if provider == LLMProvider.OPENAI:
        api_key = get_api_key(provider)
        if not api_key:
            raise ValueError("OpenAI API key not set in config.")
        openai.api_key = api_key
        try:
            response = openai.chat.completions.create(
                model=model.value,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[OpenAI Error: {e}]"
    elif provider == LLMProvider.GEMINI:
        api_key = get_api_key(provider)
        if not api_key:
            raise ValueError("Gemini API key not set in config.")
        if api_key.startswith("AIza"):
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model.value}:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "maxOutputTokens": max_tokens,
                    "temperature": 0.7
                }
            }
            try:
                resp = requests.post(url, headers=headers, json=data)
                resp.raise_for_status()
                result = resp.json()
                if "candidates" in result and len(result["candidates"]) > 0:
                    return result["candidates"][0]["content"]["parts"][0]["text"].strip()
                else:
                    return f"[Gemini Error: No candidates returned. Response: {result}]"
            except requests.exceptions.RequestException as e:
                error_details = ""
                if hasattr(e, 'response') and e.response is not None:
                    try:
                        error_json = e.response.json()
                        error_details = f" | Error details: {error_json}"
                    except:
                        error_details = f" | Response text: {e.response.text}"
                return f"[Gemini REST Error: {e}{error_details}]"
            except Exception as e:
                return f"[Gemini REST Error: {e}]"
        else:
            try:
                genai.configure(api_key=api_key)
                model_obj = genai.GenerativeModel(model.value)
                generation_config = {
                    "max_output_tokens": max_tokens,
                    "temperature": 0.7
                }
                response = model_obj.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                if response.text:
                    return response.text.strip()
                else:
                    return f"[Gemini SDK Error: No text generated. Response: {response}]"
            except Exception as e:
                return f"[Gemini SDK Error: {e}]"
    elif provider == LLMProvider.OLLAMA:
        try:
            response = ollama.generate(
                model=model.value,
                prompt=prompt
            )
            return response["response"].strip()
        except Exception as e:
            return f"[Ollama Error: {e}]"
    else:
        return "[Unknown LLM provider]" 
from utils.llm import generate_with_llm, LLMProvider, LLMModel

prompt = "Write a short, funny tweet about AI."

print("Testing OpenAI (GPT-4o):")
try:
    result = generate_with_llm(prompt, model=LLMModel.GPT_4O, provider=LLMProvider.OPENAI)
    print(result)
except Exception as e:
    print(f"OpenAI error: {e}")

print("\nTesting Gemini (Gemini Flash):")
try:
    result = generate_with_llm(prompt, model=LLMModel.GEMINI_FLASH, provider=LLMProvider.GEMINI)
    print(result)
except Exception as e:
    print(f"Gemini error: {e}")

print("\nTesting Ollama (Llama3):")
try:
    result = generate_with_llm(prompt, model=LLMModel.OLLAMA_LLAMA3, provider=LLMProvider.OLLAMA)
    print(result)
except Exception as e:
    print(f"Ollama error: {e}") 
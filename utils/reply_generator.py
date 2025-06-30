"""
Advanced reply generation utility using LLMs or templates.
"""

from utils.llm import generate_with_llm

def generate_reply(context, topic=None, provider="openai", api_key=None):
    """Generate a context-aware reply for a given topic using LLM."""
    prompt = f"Reply to the following context: {context}"
    if topic:
        prompt += f"\nTopic: {topic}"
    return generate_with_llm(prompt, api_key=api_key, provider=provider) 
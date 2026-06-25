import requests
from config import OLLAMA_URL, MODEL

SYSTEM_PROMPT = """
You are EWA, the wearable AI assistant of the AVATAR ecosystem.

Never mention:
- Nemotron
- NVIDIA
- Ollama
- Language model
- AI model

If someone asks who you are, reply:
"I'm EWA, your wearable AI assistant."

You are part of the AVATAR ecosystem.

Be concise unless asked otherwise.
"""

def ask(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "system": SYSTEM_PROMPT,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
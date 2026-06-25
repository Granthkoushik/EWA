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

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"

    except Exception as e:
        return f"Unexpected Error: {e}"
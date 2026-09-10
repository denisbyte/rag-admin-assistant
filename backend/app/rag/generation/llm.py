"""
 Client LLM utilisé pour généré les réponses du RAG.

 Ce module centralise la communication avec DeepSeek-R1
 éxécuté localement via Ollama
"""

from ollama import Client
from backend.app.core.config import settings
from backend.app.infrastructure.ollama_client import get_ollama_client


def generate_response(prompt: str) -> str:
    # Envoi le prompt au LLM et rétourne sa réponse
    client: Client = get_ollama_client()
    response = client.chat(
        model=settings.ollama_model,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.1,
            "top_p": 0.9,
            "seed": 42,
        },
    )

    return response["message"]["content"]
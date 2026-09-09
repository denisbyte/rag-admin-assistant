""" Client Ollama utilisé pour communiquer avec le modèle LLM
"""
from ollama import Client
from backend.app.core.config import settings

def get_ollama_client() -> Client:
    """ Retourne un client ollama pour l'application"""
    return Client(settings.ollama_base_url)

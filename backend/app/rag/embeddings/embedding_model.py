"""
 Modèle d'embedding utilisé par le pipeline RAG
 
"""
from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings
from backend.app.core.config import settings

@lru_cache(maxsize=1)

def get_embedding_model() -> HuggingFaceEmbeddings:
    # Retourne le modèle d'embedding utilisé par l'application
    return HuggingFaceEmbeddings(
        model_name = settings.embedding_model
    )
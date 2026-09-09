"""
 Modèle d'embedding utilisé par le pipeline RAG
 
"""
from langchain_huggingface import HuggingFaceEmbeddings
from backend.app.core.config import settings

def get_embedding_model() -> HuggingFaceEmbeddings:
    # Retourne le modèle d'embedding utilisé par l'application
    return HuggingFaceEmbeddings(
        model_name = settings.embedding_model
    )
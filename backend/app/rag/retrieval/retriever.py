"""
 Retriever utilisé par le pipeline RAG
"""
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from backend.app.rag.retrieval.vector_store import get_vector_store

def get_retriever() -> BaseRetriever:
    # Retourne le retriever connecté à notre base chromaDB
    vector_store = get_vector_store()

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

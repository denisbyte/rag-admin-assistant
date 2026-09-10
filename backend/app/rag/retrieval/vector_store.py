"""
 Gestion de la base vectorielle chromaDB
"""
from langchain_chroma import Chroma
from langchain_core.documents import Document

from backend.app.core.config import settings
from backend.app.rag.embeddings.embedding_model import get_embedding_model

# Nom de la collection contenant les documents administratifs
COLLECTION_NAME = "documents_administratifs"

def get_vector_store() -> Chroma:
    # Retourne la base vectorielle ChromaDB du projet
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embedding_model(),
        persist_directory=settings.chroma_path
    )

def index_documents(documents: list[Document]) -> Chroma:
    vector_store = get_vector_store()

    # Identifiants deterministe afin de pouvoir générer les memes chunks
    ids = [f"chunk-{index}" for index in range(len(documents))]
    vector_store.add_documents(
        documents=documents,
        ids = ids,
    )

    return vector_store
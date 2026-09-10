"""
Reranking des documents récupérés par le retriever.


"""

from functools import lru_cache

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder


RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L6-v2"
RERANK_THRESHOLD = 0.0


@lru_cache(maxsize=1)
def get_reranker() -> CrossEncoder:
    # Charge le modèle de reranking une seule fois par processus.
    return CrossEncoder(RERANKER_MODEL)


def rerank_documents(
    question: str,
    documents: list[Document],
    top_k: int = 3,
) -> list[Document]:
    """
    Reclasse les documents selon leur pertinence
    et élimine ceux dont le score est trop faible.
    """

    if not documents:
        return []

    reranker = get_reranker()

    pairs = [
        (question, document.page_content)
        for document in documents
    ]

    scores = reranker.predict(pairs)

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda item: float(item[1]),
        reverse=True,
    )

    filtered_documents = [
        document
        for document, score in ranked_documents
        if float(score) >= RERANK_THRESHOLD
    ]

    return filtered_documents[:top_k]
"""
Pipeline principal du système RAG
"""

from langchain_core.documents import Document

from backend.app.rag.retrieval.retriever import get_retriever
from backend.app.rag.generation.prompt import build_prompt
from backend.app.rag.generation.llm import generate_response
from backend.app.rag.retrieval.reranker import rerank_documents


REFUSAL_MESSAGE = (
    "L'information n'est pas disponible dans les documents fournis."
)


def build_context(documents: list[Document]) -> str:
    """
    Transforme les documents récupérés en contexte textuel
    qui sera envoyé au LLM.
    """

    context_parts = []

    for document in documents:
        source = document.metadata.get(
            "document",
            "Document inconnu"
        )
        page = document.metadata.get(
            "page",
            "Page inconnue"
        )

        context_parts.append(
            f"[Source : {source} | Page : {page}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(context_parts)


def answer_question(
    question: str
) -> tuple[str, list[Document]]:

    retriever = get_retriever()

    # 1. Récupération des candidats depuis ChromaDB
    documents = retriever.invoke(question)

    # 2. Reranking + filtrage
    documents = rerank_documents(
        question,
        documents,
        top_k=3,
    )

    # 3. Aucun document suffisamment pertinent
    if not documents:
        return REFUSAL_MESSAGE, []

    # 4. Construction du contexte
    context = build_context(documents)

    # 5. Construction du prompt
    prompt = build_prompt(question, context)

    # 6. Génération de la réponse
    answer = generate_response(prompt).strip()

    # 7. Si le LLM conclut que le contexte ne permet
    # pas de répondre, aucune source ne doit être retournée
    if REFUSAL_MESSAGE in answer:
        return REFUSAL_MESSAGE, []

    return answer, documents
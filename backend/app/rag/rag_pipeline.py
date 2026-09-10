"""
 Pipeline principal du système RAG
"""
from langchain_core.documents import Document

from backend.app.rag.retrieval.retriever import get_retriever
from backend.app.rag.generation.prompt import build_prompt
from backend.app.rag.generation.llm import generate_response

def build_context(documents: list[Document]) -> str:
    """
     Transforme les documents récupérés en contexte textuel qui sera envoyé au LLM
    """

    context_parts = []
    for document in documents:
        source = document.metadata.get("document", "Document inconnu")
        page = document.metadata.get("page", "Page inconnu")

        context_parts.append(
            f"[Source : {source} | Page : {page}]\n"
            f"{document.page_content}"
        )
        return "\n\n".join(context_parts)

    
def answer_question(question: str) -> tuple[str, list[Document]]:
    """
    Éxécute le pipeline RAG complet pour une question 
    """
    ## Recherche des chunks pertinents
    retriever = get_retriever()
    documents = retriever.invoke(question)

    # Construction du context à partir des chunks récupérés
    context = build_context(documents)

    # Construction du prompt contenant la question et le contexte
    prompt = build_prompt(question, context)

    # Génération de la réponse avec DeepSeek
    answer = generate_response(prompt)
    return answer, documents




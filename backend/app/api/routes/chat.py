"""
Route API permettant de poser une question à l'assistant administratif
"""
from fastapi import APIRouter

from backend.app.rag.rag_pipeline import answer_question
from backend.app.schemas.chat import ChatRequest, ChatResponse, Source
from backend.app.services.cache_service import (
    get_cached_response,set_cached_response
)

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Verifie si la réponse existe déja dans notre cache Redis
    cached_data = get_cached_response(request.question)
    if cached_data is not None:
     return ChatResponse(
        answer=cached_data["answer"],
        sources=[
        Source(**source)
        for source in cached_data["sources"]
        ],
        cached=True

    )

    # Si la réposnse n'est pas dans le cache on éxécute le RAG
    answer , documents = answer_question(request.question)
    sources = [
       Source(
          document=document.metadata.get("document", "Inconnu"),
            page=document.metadata.get("page"),
            title=document.metadata.get("title"),
            url=document.metadata.get("url"),
       )
       for document in documents
    ]
    # Préparation des données à stocker dans Redis
    cache_data = {
       "answer": answer,
       "sources": [
          source.model_dump()
          for source in sources
       ],
    }

    # Enregistrement dans Redis
    set_cached_response(
       request.question,
       cache_data,
    )
    # Retour de la réponse
    return ChatResponse(
       answer= answer,
       sources= sources,
       cached= False
    )

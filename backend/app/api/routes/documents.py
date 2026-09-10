"""
 Route API permettant de récupérer les docuements 
 administratifs possibles
"""

from fastapi import APIRouter

from backend.app.rag.ingestion.document_metadata import DOCUMENT_METADATA
from backend.app.schemas.documents import Document

router = APIRouter()

@router.get('/documents', response_model=list[Document])
def get_documents():

    documents = []

    for filename, metadata in DOCUMENT_METADATA.items():
        documents.append(
            Document(
                filename= filename,
                title=metadata.get('title'),
                source="Service-Public.gouv.fr",
                url=metadata.get("url"),
            )
        )

    return documents
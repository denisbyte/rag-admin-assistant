from fastapi import FastAPI

from backend.app.api.routes.chat import router as chat_router
from backend.app.api.routes.documents import router  as document_router

app = FastAPI(
    title="RAG Admin Assistant",
    description="Assistant administratif basé sur RAG",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}



app.include_router(chat_router)
app.include_router(document_router)
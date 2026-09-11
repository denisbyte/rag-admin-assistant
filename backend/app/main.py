from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes.chat import router as chat_router
from backend.app.api.routes.documents import router  as document_router

app = FastAPI(
    title="RAG Admin Assistant",
    description="Assistant administratif basé sur RAG",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}



app.include_router(chat_router)
app.include_router(document_router)
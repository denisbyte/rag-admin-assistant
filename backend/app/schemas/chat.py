from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Question de l'utilisateur"
    )

class Source(BaseModel):
    document: str
    page: int | None = None
    title: str | None = None
    url: str | None = None

class ChatResponse(BaseModel):
    answer: str
    sources : list[Source] = Field(default_factory=list)
    #Indique si la réponqe a été recupéré depuis notre serveur de cache Redis
    cached: bool = False
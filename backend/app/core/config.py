from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ Paramètres de configuration et du pipeline RAG"""

    app_name: str = "RAG Admin Assistant"
    app_version: str = "1.0.0"

    documents_path: str = "data/docuements"
    chroma_path: str = "data/chroma"

    embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "deepseek-r1:7b"
    redis_url: str = "redis://localhost:6379"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="uft-8",
        extra="ignore"

    )
settings = Settings()


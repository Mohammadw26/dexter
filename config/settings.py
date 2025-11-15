from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Kubernetes
    KUBE_CONFIG_PATH: Optional[str] = None
    DEFAULT_NAMESPACE: str = "default"

    # MCP
    MCP_SECRET: Optional[str] = None

    # Ollama
    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3"

    # Chroma
    CHROMA_DB_DIR: str = "./chroma_db"

    # Embeddings
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    # LangSmith
    LANGSMITH_API_KEY: Optional[str] = None

    # App
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

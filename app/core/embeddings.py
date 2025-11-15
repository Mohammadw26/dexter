import numpy as np
from sentence_transformers import SentenceTransformer

from config.settings import settings


class EmbeddingService:
    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or settings.EMBEDDING_MODEL
        self._model = None

    def _ensure(self):
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)

    def embed(self, texts: list[str]) -> list[list[float]]:
        self._ensure()
        arr = self._model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
        return [a.astype(np.float32).tolist() for a in arr]


# singleton
_embedding_service = EmbeddingService()


def get_embedding_service():
    return _embedding_service

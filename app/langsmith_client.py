# Minimal LangSmith wrapper placeholder — replace with official SDK usage
import logging
import os

from config.settings import settings

logger = logging.getLogger(__name__)


class LangSmithClient:
    def __init__(self):
        self.api_key = settings.LANGSMITH_API_KEY

    def log(self, name: str, payload: dict):
        if not self.api_key:
            logger.debug("LangSmith disabled — no API key")
            return
        # In production, call official LangSmith client to create run/log events
        logger.info("LangSmith log: %s - %s", name, payload)


langsmith = LangSmithClient()

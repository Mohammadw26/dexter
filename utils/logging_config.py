import logging

from config.settings import settings

LOG_LEVEL = settings.LOG_LEVEL


def configure_logging():
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


configure_logging()

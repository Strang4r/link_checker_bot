import logging
import pathlib
from logging.handlers import RotatingFileHandler

from app.pkg.settings import settings

_log_format = (
    "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%("
    "funcName)s(%(lineno)d) - %(message)s "
)


def get_file_handler(file_name: pathlib.Path) -> RotatingFileHandler:
    file_name.absolute().parent.mkdir(exist_ok=True, parents=True)
    file_handler = RotatingFileHandler(
        filename=file_name,
        maxBytes=5242880,
        backupCount=10,
    )
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler() -> logging.StreamHandler:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(get_file_handler(file_name=settings.LOGGER_FILE_PATH))
    logger.addHandler(get_stream_handler())
    logger.setLevel(settings.LOGGER_LEVEL)
    return logger

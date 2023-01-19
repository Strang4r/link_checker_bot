from functools import lru_cache
from pathlib import Path

from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings


class _Settings(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True


class Settings(_Settings):
    # Telegram
    TELEGRAM_BOT_TOKEN: str

    # Bot settings
    SCREENSHOTS_FOLDER: Path

    # Browser settings
    WEBDRIVER_PATH: Path
    BROWSER_EXEC_PATH: Path

    # logs
    LOGGER_FILE_PATH: Path
    LOGGER_LEVEL: str


@lru_cache()
def get_settings(env_file: str = ".env") -> Settings:
    return Settings(_env_file=find_dotenv(env_file))

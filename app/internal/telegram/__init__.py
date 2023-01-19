import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dependency_injector import containers, providers

from app.pkg.settings import settings


class Telegram(containers.DeclarativeContainer):
    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    bot = providers.Singleton(aiogram.Bot, token=configuration.TELEGRAM_BOT_TOKEN)

    dispatcher = providers.Singleton(
        aiogram.Dispatcher,
        bot=bot,
        storage=MemoryStorage(),
    )

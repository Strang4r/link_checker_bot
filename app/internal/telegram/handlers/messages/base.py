import logging
from abc import abstractmethod

import aiogram
from dependency_injector.wiring import Provide, inject

from app.internal.telegram import Telegram
from app.pkg.settings.logger import get_logger

__all__ = ["BaseHandler"]


class BaseHandler:
    dispatcher: aiogram.Dispatcher
    bot: aiogram.Bot
    logger: logging.Logger

    @inject
    def __init__(
            self,
            dispatcher: aiogram.Dispatcher = Provide[Telegram.dispatcher],
            bot: aiogram.bot = Provide[Telegram.bot],
    ):
        self.dispatcher = dispatcher
        self.bot = bot
        self.logger= get_logger("BaseHandler")

    @abstractmethod
    def register_methods(self):
        """Function for register handlers in object."""
        raise NotImplementedError()

    @staticmethod
    async def _normalize_message(message: str) -> str:
        return message.translate({ord(c): f"\\{c}" for c in ".!@#%^"})

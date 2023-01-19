import logging

import aiogram
from aiogram.utils.exceptions import BotBlocked
from dependency_injector.wiring import Provide, inject

from app.internal.telegram import Telegram
from app.pkg.settings.logger import get_logger

__all__ = ["Messages"]


class Messages:
    bot: aiogram.Bot
    logger: logging.Logger = get_logger("send_message")

    @inject
    def __init__(self, bot: aiogram.Bot = Provide[Telegram.bot]):
        self.bot = bot

    async def answer_user(self, chat_id: int, text: str):
        try:

            await self.bot.send_message(
                text=text,
                parse_mode="Markdown",
                chat_id=chat_id)

        except BotBlocked as err:
            self.logger.error(f"Unable to send message {err}")

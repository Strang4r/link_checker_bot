import textwrap

import aiogram
from aiogram.types import InputFile
from dependency_injector.wiring import inject

from app.internal.clients.link_checker import BaseClient
from app.internal.pkg.repository.exceptions import InvalidLink, UnreachableLink
from app.internal.telegram.handlers.messages.base import BaseHandler
from app.internal.telegram.handlers.normalizers.messages import normalize_message

__all__ = ["MainHandlers"]


class MainHandlers(BaseHandler):
    @inject
    def __init__(self):
        super().__init__()

    def register_methods(self):
        self.dispatcher.register_message_handler(
            self.start,
            commands=["start"],
        )
        self.dispatcher.register_message_handler(
            self.check_user_link,
        )
        self.dispatcher.register_message_handler(self.ignoring_non_callback_messages)

    async def start(
            self,
            message: aiogram.types.Message,
    ):
        await self.bot.send_message(
            chat_id=message.chat.id,
            text=textwrap.dedent(
                await normalize_message(
                    """Автор: ||t.me/strang4r|| """,
                ),
            ),
            parse_mode="MarkdownV2",
        )

    async def check_user_link(self, message: aiogram.types.Message, ):
        base_cli = BaseClient()
        try:
            print('starting check_user_link')
            translated_link = await base_cli.translate_link(message.text)
            print('done translated')

            response = await base_cli.check_link(message.text, translated_link)

            photo = InputFile(f'C:\PyProj\link_checker_bot\screenshots\{translated_link}.png')
            await self.bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption=str(response)
            )
            print('message sent back')
        except InvalidLink:
            await self.bot.send_message(chat_id=message.chat.id,
                                        text='Неверная ссылка, попробуй в таком формате http://your_link.com')
        except UnreachableLink:
            await self.bot.send_message(chat_id=message.chat.id,
                                        text='Невозможно получить доступ к странице ')
        except Exception as err:
            print(err)

    @staticmethod
    async def ignoring_non_callback_messages(message: aiogram.types.Message):
        """Delete non-callback messages."""

        await message.delete()

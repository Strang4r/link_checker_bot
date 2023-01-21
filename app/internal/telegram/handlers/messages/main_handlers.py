import textwrap

import aiogram
from aiogram.types import InputFile
from dependency_injector.wiring import inject

from app.internal.clients.base_client import BaseClient
from app.internal.clients.browser_client import BaseBrowserClient
from app.internal.pkg.repository.exceptions import UnreachableLink
from app.internal.telegram.handlers.messages.base import BaseHandler
from app.internal.telegram.handlers.normalizers.messages import normalize_message

__all__ = ["MainHandlers"]

from app.pkg.settings import settings


class MainHandlers(BaseHandler):
    browser_cli: BaseBrowserClient
    base_cli: BaseClient

    @inject
    def __init__(self):
        self.browser_cli = BaseBrowserClient()
        self.base_cli = BaseClient()
        super().__init__()

    def register_methods(self):
        self.dispatcher.register_message_handler(
            self.start,
            commands=["start"],
        )
        self.dispatcher.register_message_handler(
            self.check_user_link,
        )

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
        await self.bot.send_message(
            chat_id=message.chat.id,
            text=textwrap.dedent(
                await normalize_message(
                    """Отправь мне ссылку в формате http://your_link.com или your_link.com""",
                ),
            ),
            parse_mode="MarkdownV2",
        )

    async def check_user_link(self, message: aiogram.types.Message, ):
        if '.' not in message.text:
            await self.bot.send_message(chat_id=message.chat.id,
                                        text='Не похоже на ссылку. Попробуй в таком формате: http://your_link.com или your_link.com')
            return
        if 'http' not in message.text:
            message.text = 'http://' + message.text
        try:
            await self.browser_cli.start_browser()
            filename = await self.base_cli.generate_filename(message.text)
            response = await self.base_cli.check_link(message.text)

            await self.browser_cli.make_screenshot(message.text, filename)
            photo = InputFile(f'{settings.SCREENSHOTS_FOLDER}/{filename}.png')

            await self.bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption=f'Status code: {response}'
            )
            self.logger.debug('screenshot sent back to user')

        except UnreachableLink as err:
            await self.bot.send_message(chat_id=message.chat.id,
                                        text='Невозможно получить доступ к странице, возможно она недоступна ')
            self.logger.warning(f'UnreachableLink: {err}')
        except Exception as err:
            self.logger.error(f'Unknown error {err}')

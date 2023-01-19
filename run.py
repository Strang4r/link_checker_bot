import asyncio

import aiogram
from aiogram import executor
from dependency_injector.wiring import Provide, inject

from app.internal.telegram import Telegram
from app.internal.telegram.handlers.messages import __handlers__
from app.pkg.containter_dispatcher import register_container


@inject
def bot_polling(
        dispatcher: aiogram.Dispatcher = Provide[Telegram.dispatcher],
):
    __handlers__.allocate()

    loop = asyncio.get_event_loop()
    executor.start_polling(dispatcher, loop=loop)


def main():
    register_container(__name__)
    asyncio.run(bot_polling())


if __name__ == "__main__":
    main()

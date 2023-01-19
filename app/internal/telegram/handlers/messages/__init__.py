from app.internal.telegram.handlers.messages.main_handlers import MainHandlers
from app.pkg.models import TelegramHandler

__handlers__ = TelegramHandler(
    handler=[
        MainHandlers,


    ],
)

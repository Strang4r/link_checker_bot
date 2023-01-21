__all__ = [
    "InvalidLink",
    "UnreachableLink"
]

from app.pkg.models.base.exception import BaseBotException


class InvalidLink(BaseBotException):
    message = "Неверная ссылка"


class UnreachableLink(BaseBotException):
    message = "Site can’t be reached"

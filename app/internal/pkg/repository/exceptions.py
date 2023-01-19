__all__ = [
    "EmptyResult",
    "DriverError",
]

from app.pkg.models.base.exception import BaseBotException


class EmptyResult(BaseBotException):
    message = "Не найдено."


class DriverError(BaseBotException):
    message = "Внутренняя ошибка."


class InvalidLink(BaseBotException):
    message = "Неверная ссылка"


class UnreachableLink(BaseBotException):
    message = "Site can’t be reached"

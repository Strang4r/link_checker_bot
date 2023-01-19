__all__ = ["BaseBotException"]


class BaseBotException(Exception):
    def __init__(self, message: str = None):
        if message:
            self.message = message

    def __str__(self):
        return self.message

    message: str

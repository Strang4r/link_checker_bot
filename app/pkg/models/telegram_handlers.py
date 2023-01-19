from dataclasses import dataclass
from typing import List


@dataclass
class TelegramHandler:
    handler: List

    def allocate(self):
        for handler in self.handler:
            handler().register_methods()

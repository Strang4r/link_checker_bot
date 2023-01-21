import logging
import time

import requests

from app.internal.pkg.repository import UnreachableLink
from app.pkg.settings.logger import get_logger


class BaseClient:
    logger: logging.Logger

    def __init__(self):
        self.logger = get_logger("BaseClient")

    async def generate_filename(self, url: str) -> str:
        if '://' in url:
            link = url.split('://')[1]
        else:
            link = url
        for char in ':/?*"':
            link = link.replace(char, '_')
        time_now=time.strftime("%Y-%m-%d_%H_%M")
        filename = f'{time_now}_{link}'
        self.logger.debug(f'filename generated: {filename}')
        return filename

    async def check_link(self, link: str) -> int:
        try:
            response = requests.get(link)
        except Exception:
            raise UnreachableLink
        self.logger.debug(f'Response: {response.status_code}')
        return response.status_code

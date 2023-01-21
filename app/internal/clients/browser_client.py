import logging
from copy import deepcopy

from undetected_chromedriver import Chrome
from xvfbwrapper import Xvfb

from app.pkg.settings import settings
from app.pkg.settings.browser_driver_settings import chrome_options
from app.pkg.settings.logger import get_logger

__all__ = ["BaseBrowserClient"]


class BaseBrowserClient:
    logger: logging.Logger
    browser: Chrome
    vdisplay: Xvfb

    def __init__(self):
        self.logger = get_logger("BaseBrowserClient")

    async def start_browser(self) -> None:
        current_options = deepcopy(chrome_options)
        self.vdisplay = Xvfb(width=settings.DISPLAY_WIDTH, height=settings.DISPLAY_HEIGHT)
        self.vdisplay.start()

        self.browser = Chrome(
            options=current_options,
            headless=False,
            driver_executable_path=settings.WEBDRIVER_PATH,
            browser_executable_path=settings.BROWSER_EXEC_PATH,
        )
        self.logger.debug('browser started')
        self.browser.delete_all_cookies()

    async def make_screenshot(self, link: str, filename: str) -> None:
        self.logger.debug('opening link...')

        self.browser.get(link)
        screen_path = f'{settings.SCREENSHOTS_FOLDER}/{filename}.png'
        self.browser.implicitly_wait(1)

        self.browser.save_screenshot(screen_path)
        self.logger.debug('screenshot saved')

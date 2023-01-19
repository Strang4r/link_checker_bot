import logging
import time
from copy import deepcopy

import requests
from selenium import webdriver
from undetected_chromedriver import Chrome

from app.internal.pkg.repository.exceptions import UnreachableLink
from app.pkg.settings import settings
from app.pkg.settings.browser_driver_settings import chrome_options
from app.pkg.settings.logger import get_logger

__all__ = ["BaseClient"]


class BaseClient:
    logger: logging.Logger = get_logger("BaseClient")
    browser: webdriver.Chrome
    driver: webdriver.Chrome

    def __init__(self):
        # current_options = deepcopy(chrome_options)
        # current_options.binary_location = "/usr/bin/google-chrome-stable"

        print('trying initialize driver')
        self.browser = Chrome(
            options=chrome_options,
            # driver_executable_path="/usr/bin/chromedriver",
            driver_executable_path="C:\Program Files\Google\Chrome\Application\chromedriver",
            # browser_executable_path="/usr/bin/google-chrome",
            browser_executable_path="C:\Program Files\Google\Chrome\Application\chrome",
        )
        print('browser started')
        self.browser.delete_all_cookies()
        # self.browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    @staticmethod
    async def generate_filename(url):
        if '://' in url:
            link = url.split('://')[1]
        else:
            link = url
        for char in ':/?*"':
            link = link.replace(char, '_')

        print(f'get link:{link}')
        date_string = time.strftime("%Y-%m-%d_%H_%M")
        filename = f'{date_string}_{link}'
        print(f'full path:{filename}')
        return filename

    async def check_link(self, link, translated_link):
        if 'http' not in link:
            link = 'http://' + link
        try:
            response = requests.get(link)
            print(response)
        except Exception as err:
            print(err, 'url unreachable')
            raise UnreachableLink
        self.browser.get(link)
        screen_path = f'{settings.SCREENSHOTS_FOLDER}/{translated_link}.png'
        print('screenshot saved')
        self.browser.save_screenshot(screen_path)

        print(response)
        if self.browser is not None:
            self.browser.quit()
        return response
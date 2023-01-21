import pytest

from app.internal.clients.base_client import BaseClient

cli = BaseClient()


@pytest.mark.parametrize("link", ['https://www.youtube.com/watch?v=1HtEPEn4-LY',
                                  'https://leetcode.com',
                                  'https://yandex.ru/pogoda/moscow?utm_medium=web&utm_source=home&utm_content=main_informer&utm_campaign=informer&utm_term=title&lat=55.753215&lon=37.622504',
                                  'https://onlinetimer.ru/#!/set-time?seconds=3600',
                                  'twitch.tv',
                                  'yandex.ru',
                                  'https://httpbin.org/status/404',
                                  'https://httpbin.org/status/500'
                                  ])
async def test_filename_generator(link):
    assert ('?' or '/' or ':' or '*') not in await cli.generate_filename(link)

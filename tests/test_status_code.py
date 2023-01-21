import pytest

from app.internal.clients.base_client import BaseClient
from app.internal.pkg.repository import UnreachableLink

pytest_plugins = ('pytest_asyncio',)
cli = BaseClient()


@pytest.mark.asyncio
@pytest.mark.parametrize("link,expected_result", [('https://www.youtube.com/watch?v=1HtEPEn4-LY', 200),
                                                  ('https://leetcode.com', 200),
                                                  (
                                                          'https://yandex.ru/pogoda/moscow?utm_medium=web&utm_source=home&utm_content=main_informer&utm_campaign=informer&utm_term=title&lat=55.753215&lon=37.622504',
                                                          200),
                                                  ('https://onlinetimer.ru/#!/set-time?seconds=3600', 200),
                                                  ('https://twitch.tv', 200),
                                                  ('https://yandex.ru', 200),
                                                  ('https://httpbin.org/status/404', 404),
                                                  ('https://httpbin.org/status/500', 500),
                                                  ])
async def test_status_code(link, expected_result):
    assert await cli.check_link(link) == expected_result


@pytest.mark.asyncio
async def test_unreachable_link():
    with pytest.raises(UnreachableLink) as e_info:
        await cli.check_link('https://linkedin.com')

import pytest

from app.internal.clients.link_checker import BaseClient

@pytest.mark.parametrize("link",['https://www.youtube.com/watch?v=1HtEPEn4-LY',
                                 'https://leetcode.com',
                                 'https://yandex.ru/pogoda/moscow?utm_medium=web&utm_source=home&utm_content=main_informer&utm_campaign=informer&utm_term=title&lat=55.753215&lon=37.622504',
                                 'https://onlinetimer.ru/#!/set-time?seconds=3600',
                                 ])
def test_link_translater(link):
    cli=BaseClient()
    assert '?' or '/' or ':' not in cli.translate_link(link)
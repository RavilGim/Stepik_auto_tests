import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: ru, en, ... (etc.)')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(3)
    browser.quit()

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    language=request.config.getoption("language")
    if language=="es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
        yield browser
        # ожидание чтобы визуально оценить что браузер открылся на испанском языке!
        time.sleep(10)
        print("\nquit browser..")
        browser.quit()


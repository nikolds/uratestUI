import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # headless если не нужно отображение
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe',
                              options=options)  # директория где находится драйвер браузера
    return driver


@pytest.fixture(scope='function')  # новое окно. если session все в одном браузере
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://ura.news/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()  # закрывает вкладку. для закрытия всего окна driver.quite()

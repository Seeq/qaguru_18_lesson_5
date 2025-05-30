import os
import pytest
from selene import browser
from selenium import webdriver


# from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.window_height = 800
    browser.config.window_width = 1280
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def file_path():
    return os.path.join(os.path.dirname(__file__), 'files', 'meme.png')

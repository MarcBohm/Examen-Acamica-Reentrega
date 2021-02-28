import pytest
from selenium import webdriver
import os


@pytest.fixture
def browser():
    # Setup faze.
    driver_path = os.environ.get('ChromeDriver')
    browser = webdriver.Chrome(driver_path)

    browser.implicitly_wait(15)

    browser.maximize_window()

    yield browser

    # Cleanup faze.
    browser.close()
    browser.quit()


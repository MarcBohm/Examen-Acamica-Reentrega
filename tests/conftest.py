import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # Setup faze.
    browser = webdriver.Chrome(executable_path='C:/Devtools/Chrome Driver/chromedriver.exe')

    browser.implicitly_wait(15)

    browser.maximize_window()

    yield browser

    # Cleanup faze.
    browser.close()
    browser.quit()


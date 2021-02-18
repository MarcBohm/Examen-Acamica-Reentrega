import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Setup faze.
    browser = webdriver.Chrome(executable_path=r"C:\Users\marcb\Downloads\chromedriver_win32\chromedriver.exe")

    browser.implicitly_wait(15)

    browser.maximize_window()

    yield browser

    # Cleanup faze.
    browser.close()
    browser.quit()


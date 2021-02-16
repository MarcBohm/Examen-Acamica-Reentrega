from selenium.webdriver.common.by import By
import time


class DepartureFlightPage:
    offers_listing = (By.CSS_SELECTOR, "li[data-test-id='offer-listing']")
    select_button = (By.CSS_SELECTOR, "button[data-test-id='select-button']")
    select_fare_button = (By.XPATH, "//li[@data-test-id='offer-listing']//div[@class='basic-economy-footer uitk-grid "
                                    "all-grid-align-end']//button")

    def __init__(self, browser):
        self.browser = browser

    def select_first_flight(self):
        self.browser.find_element(*self.select_button).click()
        if self.browser.find_element(*self.select_fare_button).is_displayed():
            time.sleep(1)
            self.browser.find_element(*self.select_fare_button).click()

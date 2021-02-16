from selenium.webdriver.common.by import By


class ReturnFlightPage:
    offers_listing = (By.CSS_SELECTOR, "li[data-test-id='offer-listing']")
    select_button = (By.CSS_SELECTOR, "button[data-test-id='select-button']")
    select_fare_button = (By.XPATH, "//li[@data-test-id='offer-listing'][3]//div[@class='basic-economy-footer "
                                    "uitk-grid all-grid-align-end']//button")

    def __init__(self, browser):
        self.browser = browser

    def select_third_flight(self):
        flight_list = self.browser.find_elements(*self.offers_listing)
        flight_list[2].find_element(*self.select_button).click()
        if flight_list[2].find_element(*self.select_fare_button).is_displayed():
            flight_list[2].find_element(*self.select_fare_button).click()

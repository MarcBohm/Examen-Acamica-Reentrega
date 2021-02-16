from selenium.webdriver.common.by import By


class CruiseReservationPage:
    # ERROR IN SELECTOR: Even when the selector is unique, Selenium won't find it. Tried locating by CSS and Xpath.
    cruise_information = (By.XPATH, "//section[@class='col main-content']//div[@class='box "
                                    "infosite-sailing-playback-container']")

    def __init__(self, browser):
        self.browser = browser

    def information_is_shown(self):
        return self.browser.find_element(*self.cruise_information).is_displayed()

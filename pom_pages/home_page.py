from selenium.webdriver.common.by import By


class HomePage:
    URL = 'https://www.travelocity.com/'
    packages_tab = (By.CSS_SELECTOR, "a[aria-controls='wizard-package-pwa']")
    flight_tab = (By.CSS_SELECTOR, "a[aria-controls='wizard-flight-pwa']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

        if self.browser.current_url != self.URL:
            raise Exception('The page that was loaded is not the correct one, please re-run the test')

    def switch_to_packages_tab(self):
        self.browser.find_element(*self.packages_tab).click()

    def switch_to_flight_tab(self):
        self.browser.find_element(*self.flight_tab).click()

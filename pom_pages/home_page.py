from selenium.webdriver.common.by import By
from pom_pages.base_page import BasePage


class HomePage(BasePage):
    packages_tab = (By.CSS_SELECTOR, "a[aria-controls='wizard-package-pwa']")
    flight_tab = (By.CSS_SELECTOR, "a[aria-controls='wizard-flight-pwa']")

    def switch_to_packages_tab(self):
        self.browser.find_element(*self.packages_tab).click()

    def switch_to_flight_tab(self):
        self.browser.find_element(*self.flight_tab).click()

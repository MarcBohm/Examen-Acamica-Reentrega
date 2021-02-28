from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.provider import Provider
from pom_pages.base_tab import BaseTab


class FlightTab(BaseTab):
    # Locators
    leaving_from_button = (By.CSS_SELECTOR, "button[data-stid='location-field-leg1-origin-menu-trigger']")
    leaving_from_input = (By.ID, "location-field-leg1-origin")
    going_to_button = (By.CSS_SELECTOR, "button[data-stid='location-field-leg1-destination-menu-trigger']")
    going_to_input = (By.ID, "location-field-leg1-destination")

    leaving_from_data = Provider.convertir_json_a_dict("data/datasource.json", "flight departures")

    def complete_leaving_from_field(self):
        self.browser.find_element(*self.leaving_from_button).click()
        self.browser.find_element(*self.leaving_from_input).send_keys(self.leaving_from_data[0] + Keys.RETURN)

    going_to_data = Provider.convertir_json_a_dict("data/datasource.json", "flight destinations")

    def complete_going_to_field(self):
        self.browser.find_element(*self.going_to_button).click()
        self.browser.find_element(*self.going_to_input).send_keys(self.going_to_data[0] + Keys.RETURN)

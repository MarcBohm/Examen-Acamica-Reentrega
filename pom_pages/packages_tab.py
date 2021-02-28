from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.provider import Provider
from pom_pages.base_tab import BaseTab


class PackagesTab(BaseTab):
    # Locators
    leaving_from_button = (By.CSS_SELECTOR, "button[data-stid='location-field-origin-menu-trigger']")
    leaving_from_input = (By.ID, "location-field-origin")
    going_to_button = (By.CSS_SELECTOR, "button[data-stid='location-field-destination-menu-trigger']")
    going_to_input = (By.ID, "location-field-destination")
    travelers_dropdown_button = (By.CSS_SELECTOR, "a[data-testid='travelers-field']")
    adult_minus_button = (By.XPATH, "//*[@id='adaptive-menu']/div[2]/div/section/div[1]/div[1]/div/button[1]")
    travelers_dropdown_done_button = (By.CSS_SELECTOR, "button[data-testid='guests-done-button']")
    accommodations_button = (By.ID, "package-partial-stay")
    check_in_error_message = (By.ID, "d1-partial-error")
    check_out_error_message = (By.ID, "d2-partial-error")

    leaving_from_data = Provider.convertir_json_a_dict("data/datasource.json", "flight departures")

    def complete_leaving_from_field(self):
        self.browser.find_element(*self.leaving_from_button).click()
        self.browser.find_element(*self.leaving_from_input).send_keys(self.leaving_from_data[0] + Keys.RETURN)

    going_to_data = Provider.convertir_json_a_dict("data/datasource.json", "flight destinations")

    def complete_going_to_field(self):
        self.browser.find_element(*self.going_to_button).click()
        self.browser.find_element(*self.going_to_input).send_keys(self.going_to_data[0] + Keys.RETURN)

    def one_less_adult(self):
        self.browser.find_element(*self.travelers_dropdown_button).click()

        # Unreachable button. Tried by CSS selector and various XPath
        self.browser.find_element(*self.adult_minus_button).click()

        self.browser.find_element(*self.travelers_dropdown_done_button).click()

    def accommodations_click(self):
        self.browser.find_element(*self.accommodations_button).click()

    def check_in_error(self):
        return self.browser.find_element(*self.check_in_error_message).is_displayed()

    def check_out_error(self):
        return self.browser.find_element(*self.check_out_error_message).is_displayed()

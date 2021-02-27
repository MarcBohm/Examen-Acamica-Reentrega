from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.provider import Provider
import time


class TravelocityHomePage:
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


class PackagesTab:
    # Locators
    leaving_from_button = (By.CSS_SELECTOR, "button[data-stid='location-field-origin-menu-trigger']")
    leaving_from_input = (By.ID, "location-field-origin")
    going_to_button = (By.CSS_SELECTOR, "button[data-stid='location-field-destination-menu-trigger']")
    going_to_input = (By.ID, "location-field-destination")
    travelers_dropdown_button = (By.CSS_SELECTOR, "a[data-testid='travelers-field']")
    adult_minus_button = (By.XPATH, "//*[@id='adaptive-menu']/div[2]/div/section/div[1]/div[1]/div/button[1]")
    travelers_dropdown_done_button = (By.CSS_SELECTOR, "button[data-testid='guests-done-button']")
    date_picker_departing_button = (By.ID, "d1-btn")
    date_picker_next_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][2]")
    date_picker_check_in_button = (By.ID, "d1-partial-btn")
    date_picker_previous_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][1]")
    second_week_first_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[2]/td[1]")
    third_week_seventh_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[3]/td[7]")
    date_picker_done_button = (By.CSS_SELECTOR, "button[data-stid='apply-date-picker']")
    accommodations_button = (By.ID, "package-partial-stay")
    search_button = (By.CSS_SELECTOR, "button[data-testid='submit-button']")
    check_in_error_message = (By.ID, "d1-partial-error")
    check_out_error_message = (By.ID, "d2-partial-error")

    def __init__(self, browser):
        self.browser = browser

    leaving_from_data = Provider.convertir_json_a_dict("data/datasource.json", "flight departures")

    def complete_leaving_from_field(self):
        self.browser.find_element(*self.leaving_from_button).click()
        self.browser.find_element(*self.leaving_from_input).send_keys(self.leaving_from_data[0] + Keys.RETURN)

    going_to_data = Provider.convertir_json_a_dict("data/datasource.json", "flight destinations")

    def complete_going_to_field(self):
        self.browser.find_element(*self.going_to_button).click()
        self.browser.find_element(*self.going_to_input).send_keys(self.going_to_data[0] + Keys.RETURN)

    def set_valid_dates(self):
        self.browser.find_element(*self.date_picker_departing_button).click()
        # couldn't set an explicit wait for item to be clickable
        time.sleep(1)
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.second_week_first_day).click()
        self.browser.find_element(*self.third_week_seventh_day).click()
        self.browser.find_element(*self.date_picker_done_button).click()

    def one_less_adult(self):
        self.browser.find_element(*self.travelers_dropdown_button).click()

        # Unreachable button. Tried by CSS selector and various XPath
        self.browser.find_element(*self.adult_minus_button).click()

        self.browser.find_element(*self.travelers_dropdown_done_button).click()

    def accommodations_click(self):
        self.browser.find_element(*self.accommodations_button).click()

    def set_invalid_dates(self):
        self.browser.find_element(*self.date_picker_check_in_button).click()
        # couldn't set an explicit wait for previous_month to be clickable
        time.sleep(1)
        self.browser.find_element(*self.date_picker_previous_month).click()
        self.browser.find_element(*self.second_week_first_day).click()
        self.browser.find_element(*self.third_week_seventh_day).click()
        self.browser.find_element(*self.date_picker_done_button).click()

    def click_search(self):
        self.browser.find_element(*self.search_button).click()

    def check_in_error(self):
        return self.browser.find_element(*self.check_in_error_message).is_displayed()

    def check_out_error(self):
        return self.browser.find_element(*self.check_out_error_message).is_displayed()


class FlightTab:
    leaving_from_button = (By.CSS_SELECTOR, "button[data-stid='location-field-leg1-origin-menu-trigger']")
    leaving_from_input = (By.ID, "location-field-leg1-origin")
    going_to_button = (By.CSS_SELECTOR, "button[data-stid='location-field-leg1-destination-menu-trigger']")
    going_to_input = (By.ID, "location-field-leg1-destination")
    date_picker_departing_button = (By.ID, "d1-btn")
    date_picker_next_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][2]")
    date_picker_check_in_button = (By.ID, "d1-partial-btn")
    date_picker_previous_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][1]")
    second_week_first_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[2]/td[1]")
    third_week_seventh_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[3]/td[7]")
    date_picker_done_button = (By.CSS_SELECTOR, "button[data-stid='apply-date-picker']")
    search_button = (By.CSS_SELECTOR, "button[data-testid='submit-button']")

    def __init__(self, browser):
        self.browser = browser

    leaving_from_data = Provider.convertir_json_a_dict("data/datasource.json", "flight departures")

    def complete_leaving_from_field(self):
        self.browser.find_element(*self.leaving_from_button).click()
        self.browser.find_element(*self.leaving_from_input).send_keys(self.leaving_from_data[0] + Keys.RETURN)

    going_to_data = Provider.convertir_json_a_dict("data/datasource.json", "flight destinations")

    def complete_going_to_field(self):
        self.browser.find_element(*self.going_to_button).click()
        self.browser.find_element(*self.going_to_input).send_keys(self.going_to_data[0] + Keys.RETURN)

    def set_valid_dates(self):
        self.browser.find_element(*self.date_picker_departing_button).click()
        # couldn't set an explicit wait for item to be clickable
        time.sleep(1)
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.second_week_first_day).click()
        self.browser.find_element(*self.third_week_seventh_day).click()
        self.browser.find_element(*self.date_picker_done_button).click()

    def click_search(self):
        self.browser.find_element(*self.search_button).click()

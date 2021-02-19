from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FlightSearchPage:
    sort_by_dropdown = (By.ID, "sortDropdown")
    option_duration_shortest = (By.CSS_SELECTOR, "option[data-opt-id='sort-DURATION_INCREASING']")
    flight_card = (By.CSS_SELECTOR, "div[data-test-id='listing-main']")
    select_button = (By.CSS_SELECTOR, "button[data-test-id='select-button']")
    flight_duration = (By.CSS_SELECTOR, "span[data-test-id='duration']")
    details_and_baggage_fees = (By.CSS_SELECTOR, "span[class='show-flight-details']")

    def __init__(self, browser):
        self.browser = browser

    def validate_sort_dropdown_is_visible(self):
        self.browser.find_element(*self.sort_by_dropdown).is_displayed()

    def results_validations(self):
        # This function validates steps 2 b), c), d).
        for i in self.browser.find_elements(*self.flight_card):
            assert i.find_element(*self.select_button).is_displayed()
            assert i.find_element(*self.flight_duration).is_displayed()
            assert i.find_element(*self.details_and_baggage_fees).is_displayed()

    def sort_by_duration_shorter(self):
        self.browser.find_element(*self.sort_by_dropdown).click()
        self.browser.find_element(*self.option_duration_shortest).click()

    def transform_duration_to_min(self, duration):
        amount = 0
        if "h" in duration:
            no_spaces_duration = duration.replace(" ", "")

            # Separate in a list the hours from minutes when 'h' appears.
            duration_split = no_spaces_duration.split("h")
            amount += int(duration_split[0]) * 60

            # Replace the 'h' and 'm' from the second part of the list, and transform to integer.
            minutes = duration_split[1].replace("h", "")
            minutes = minutes.replace("m", "")
            amount += int(minutes)
            return amount
        else:
            minutes = duration.replace("m", "")
            return int(minutes)

    def validate_duration_sorted_correctly(self):
        previous_value = self.browser.find_element(*self.flight_duration).text
        previous_value = self.transform_duration_to_min(previous_value)

        for i in self.browser.find_elements(*self.flight_duration):
            new_value = i.text
            new_value = self.transform_duration_to_min(new_value)

            if new_value < previous_value:
                raise Exception("Sorting by price did not work properly")
            else:
                previous_value = new_value


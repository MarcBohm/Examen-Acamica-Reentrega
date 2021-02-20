from selenium.webdriver.common.by import By


class TripReviewPage:
    trip_total = (By.CSS_SELECTOR, "span[class='packagePriceTotal']")
    hidden_flight_info_text = (By.CSS_SELECTOR, "h3[class='visuallyhidden']")
    price_guarantee = (By.CSS_SELECTOR, "div[class='priceGuarantee']")
    booking_button = (By.ID, "bookButton")
    who_travels_container = (By.CSS_SELECTOR, "fieldset[class='allTravelerDetails']")
    first_name_input = (By.ID, "firstname[0]")
    last_name_input = (By.ID, "lastname[0]")
    gender_select = (By.CSS_SELECTOR, "fieldset[class='group-validation gender-select']")
    date_of_birth = (By.CSS_SELECTOR, "fieldset[class='group-validation date-of-birth-select']")

    def __init__(self, browser):
        self.browser = browser

    def verify_trip_details(self):
        # For some reason each element appears twice with the same selector, in each case the second
        # appearance is the one shown in the page.
        trip_total_list = self.browser.find_elements(*self.trip_total)
        assert trip_total_list[1].is_displayed()

        price_guarantee_list = self.browser.find_elements(*self.hidden_flight_info_text)
        assert price_guarantee_list[1].is_displayed()

        # In the case of the flight info text, both cases shared the selector but the text contained changed.
        hidden_texts = self.browser.find_elements(*self.hidden_flight_info_text)
        assert hidden_texts[0].text == "Departure" and hidden_texts[1].text == "Return"

    def continue_booking(self):
        self.browser.find_element(*self.booking_button).click()

    def validate_who_travelling(self):
        assert self.browser.find_element(*self.who_travels_container).is_displayed()
        assert self.browser.find_element(*self.first_name_input).is_displayed()
        assert self.browser.find_element(*self.last_name_input).is_displayed()
        assert self.browser.find_element(*self.gender_select).is_displayed()
        assert self.browser.find_element(*self.date_of_birth).is_displayed()


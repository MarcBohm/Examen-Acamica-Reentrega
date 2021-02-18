from selenium.webdriver.common.by import By


class ReviewBookPage:
    flight = (By.CSS_SELECTOR, "h3[class='module-subtitle'] span:nth-of-type(1)")
    hotel = (By.CSS_SELECTOR, "div[class='hotel-traveler-info-header traveler-info-header'] :first-child")
    first_name_label = (By.CSS_SELECTOR, "label[class*='first-name']")
    last_name_label = (By.CSS_SELECTOR, "label[class*='last-name']")
    phone_number_label = (By.CSS_SELECTOR, "label[class*='phone-number']")
    gender_select = (By.CSS_SELECTOR, "fieldset[class='traveler-gender group-validation']")
    date_birth_select = (By.CSS_SELECTOR, "fieldset[class='traveler-dob group-validation']")

    def __init__(self, browser):
        self.browser = browser

    def validate_trip_details(self, picked_hotel_data):
        assert self.browser.find_element(*self.flight).text == "Las Vegas (LAS) to Los Angeles (LAX)"
        assert self.browser.find_element(*self.hotel).text in picked_hotel_data

    def validate_who_travelling(self):
        assert self.browser.find_element(*self.first_name_label).is_displayed()
        assert self.browser.find_element(*self.last_name_label).is_displayed()
        assert self.browser.find_element(*self.phone_number_label).is_displayed()
        assert self.browser.find_element(*self.gender_select).is_displayed()
        assert self.browser.find_element(*self.date_birth_select).is_displayed()

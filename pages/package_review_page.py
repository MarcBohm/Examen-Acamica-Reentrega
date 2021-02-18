from selenium.webdriver.common.by import By


class PackageReviewPage:
    add_car_button = (By.CSS_SELECTOR, "button[class='btn-secondary btn-sub-action  gt-add-btn']")
    trip_flight_to = (By.ID, "trip-flight-to")
    trip_flight_from = (By.ID, "trip-flight-from")
    hotel_name = (By.ID, "trip-summary-hotel-title")
    hotel_location = (By.XPATH, "//div[@class='hotel']//div[@class='location-info']")
    vehicle_info = (By.XPATH, "//div[@class='package-summary-dx Transp']//div[@class='ticket-traveler-info']")
    continue_button = (By.CSS_SELECTOR, "button[class='btn-primary btn-action']")

    def __init__(self, browser):
        self.browser = browser

    def add_a_car(self):
        self.browser.find_element(*self.add_car_button).click()

    def validate_trip_review(self, picked_hotel_data):
        assert self.browser.find_element(*self.trip_flight_to).text == "Las Vegas (LAS)"
        assert self.browser.find_element(*self.trip_flight_from).text == "Los Angeles (LAX)"
        assert self.browser.find_element(*self.hotel_name).text in picked_hotel_data
        assert self.browser.find_element(*self.hotel_location).text in picked_hotel_data
        assert self.browser.find_element(*self.vehicle_info).text == "1 Vehicle"

    def press_continue(self):
        self.browser.find_element(*self.continue_button).click()

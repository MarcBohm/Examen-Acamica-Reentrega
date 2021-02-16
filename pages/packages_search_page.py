from selenium.webdriver.common.by import By


class PackagesSearchPage:
    departure_button = (By.CSS_SELECTOR, "button[data-stid='trip-origin-dialog-trigger']")
    destination_button = (By.CSS_SELECTOR, "button[data-stid='hotels-destination-dialog-trigger']")
    direct_flight_checkbox = (By.ID, "directFlights")
    accommodations_checkbox = (By.ID, "partialStayCheckbox")
    sort_by_dropdown = (By.ID, "sort")
    sort_by_price_option = (By.CSS_SELECTOR, "option[value='PRICE_LOW_TO_HIGH']")
    hotel_card = (By.CSS_SELECTOR, "li[data-stid='property-listing']")
    hotel_price = (By.CSS_SELECTOR, "span[data-stid='content-hotel-lead-price']")
    hotel_rating = (By.CSS_SELECTOR, "span[data-stid='content-hotel-reviews-rating']")
    hotel_link = (By.CSS_SELECTOR, "a[data-stid='open-hotel-information']")
    hotel_name = (By.CSS_SELECTOR, "h3[data-stid='content-hotel-title']")
    hotel_location = (By.CSS_SELECTOR, "div[data-test-id='content-hotel-neighborhood']")

    def __init__(self, browser):
        self.browser = browser

    def validate_departure(self):
        departures = ['Las Vegas, United States of America (LAS-All Airports)', 'Las Vegas, NV, United States of '
                                                                                'America (LAS-All Airports)']
        if self.browser.find_element(*self.departure_button).text in departures:
            assert True
        else:
            assert False

    def validate_destination(self):
        destinations = ['Los Angeles (and vicinity), California, United States of America']

        if self.browser.find_element(*self.destination_button).text in destinations:
            assert True
        else:
            assert False

    def direct_flight_checkbox_value(self, value):
        assert self.browser.find_element(*self.direct_flight_checkbox).get_attribute('value') == value

    def only_accommodations_checkbox_value(self, value):
        assert self.browser.find_element(*self.accommodations_checkbox).get_attribute('value') == value

    def sort_by_price(self):
        self.browser.find_element(*self.sort_by_dropdown).click()
        self.browser.find_element(*self.sort_by_price_option).click()

    def validate_sort_by_price(self):
        previous_value = self.browser.find_element(*self.hotel_price).text
        previous_value = int(previous_value.replace("$", ""))

        for i in self.browser.find_elements(*self.hotel_price):
            new_value = i.text
            new_value = int(new_value.replace("$", ""))

            if new_value < previous_value:
                raise Exception("Sorting by price did not work properly")
            else:
                previous_value = new_value

    def select_first_three_star_hotel(self):
        for i in self.browser.find_elements(*self.hotel_card):
            hotel_rating = i.find_element(*self.hotel_rating).text
            hotel_rating = float(hotel_rating.replace("/5", ""))

            if hotel_rating >= 3.0:
                name = i.find_element(*self.hotel_name).text
                location = i.find_element(*self.hotel_location).text
                i.click()
                return [name, location]

    def focus_on_hotel_page(self):
        self.browser.switch_to.window(self.browser.window_handles[1])





from selenium.webdriver.common.by import By
import time


class ThreeStarHotelPage:
    hotel_name = (By.CSS_SELECTOR, "h1[class='uitk-type-display-700']")
    hotel_location = (By.XPATH, "//section//h3[@class='uitk-type-heading-500']")
    room_reserve_button = (By.CSS_SELECTOR, "button[data-stid='submit-hotel-reserve']")

    def __init__(self, browser):
        self.browser = browser

    def validate_correct_hotel(self, picked_hotel_data):
        """
        Due to various inconsistencies in the hotel page compared with the hotel card from the search, only 2 items
        could be validated from the card information.
        """
        assert self.browser.find_element(*self.hotel_name).text in picked_hotel_data
        assert self.browser.find_element(*self.hotel_location).text in picked_hotel_data

    def select_first_room(self):
        room_url = self.browser.current_url
        self.browser.find_element(*self.room_reserve_button).click()

        # In some cases the button will be clicked but remain in the page.
        time.sleep(2)
        if self.browser.current_url == room_url:
            self.browser.find_element(*self.room_reserve_button).click()


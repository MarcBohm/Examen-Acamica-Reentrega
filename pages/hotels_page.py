from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.provider import Provider

class TravelocityHotelsPage:
    URL = "https://www.travelocity.com/Hotels"
    going_to_button = (By.CSS_SELECTOR, "button[data-stid='location-field-destination-menu-trigger']")
    going_to_input = (By.ID, "location-field-destination")
    search_button = (By.CSS_SELECTOR, "button[data-testid='submit-button']")
    results_listing = (By.CSS_SELECTOR, "li[data-stid='property-listing']")
    ad_text_in_listing = (By.CSS_SELECTOR, "span[class='uitk-badge-text']")
    member_discount_text = (By.CSS_SELECTOR, "div[class='messaging-card__subtitle uitk-type-300']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

        if self.browser.current_url != self.URL:
            raise Exception('The page that was loaded is not the correct one, please re-run the test')

    search_hotel_data = Provider.convertir_json_a_dict("data/datasource.json", "hotel destinations")

    def search_hotel(self):
        self.browser.find_element(*self.going_to_button).click()
        self.browser.find_element(*self.going_to_input).send_keys(self.search_hotel_data[0] + Keys.RETURN)
        self.browser.find_element(*self.search_button).click()

    def first_result_from_listing(self):
        links = self.browser.find_elements(*self.results_listing)
        return links[0].find_element(*self.ad_text_in_listing).text

    def member_discount(self):
        return self.browser.find_element(*self.member_discount_text).text

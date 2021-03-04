from selenium.webdriver.common.by import By
from pom_pages.base_page import BasePage


class HotelSearchPage(BasePage):
    results_listing = (By.CSS_SELECTOR, "li[data-stid='property-listing']")
    ad_text_in_listing = (By.CSS_SELECTOR, "span[class='uitk-badge-text']")
    member_discount_text = (By.CSS_SELECTOR, "div[class='messaging-card__subtitle uitk-type-300']")

    def first_result_from_listing(self):
        links = self.browser.find_elements(*self.results_listing)
        return links[0].find_element(*self.ad_text_in_listing).text

    def member_discount(self):
        return self.browser.find_element(*self.member_discount_text).text


from selenium.webdriver.common.by import By


class TravelocityCruisesPage:
    URL = "https://www.travelocity.com/Cruises"
    going_to_dropdown_select = (By.ID, "cruise-destination")
    dropdown_europe_item = (By.CSS_SELECTOR, "option[value='europe']")
    search_button = (By.CSS_SELECTOR, "button[data-testid='submit-button']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

        if self.browser.current_url != self.URL:
            raise Exception('The page that was loaded is not the correct one, please re-run the test')

    def select_europe(self):
        self.browser.find_element(*self.going_to_dropdown_select).click()
        self.browser.find_element(*self.dropdown_europe_item).click()

    def search(self):
        self.browser.find_element(*self.search_button).click()


class CruisesSearchPage:
    destination_select = (By.ID, "destination-select")
    cruise_filters = (By.CSS_SELECTOR, "aside[class*='cruise-filters']")
    cruise_filter_length_10_14 = (By.ID, "length-10-14-ember1123-label")
    results_price_area = (By.XPATH, "//div[@class='flex-area-secondary']")
    price_without_discount = (By.XPATH, "//div[@class='ember-view']//span[@class='strikeout-price-card']//s")
    cruise_price = (By.XPATH, "//div[@class='flex-area-secondary']//span[@class='card-price']")
    results_with_discount = (By.XPATH, "//div[@class='flex-area-secondary']//div[@class='message-flag flex-flag']")
    # ERROR IN SELECTOR: It's not unique so it selects the first continue button.
    cruise_continue_button = (By.CSS_SELECTOR, "a[class='btn btn-secondary btn-action select-sailing-button']")

    def __init__(self, browser):
        self.browser = browser

    def destination_filter_text(self):
        return self.browser.find_element(*self.destination_select).text

    def cruises_filter_is_shown(self):
        return self.browser.find_element(*self.cruise_filters).is_displayed()

    def cruise_length_10_14(self):
        self.browser.find_element(*self.cruise_filter_length_10_14).click()

    def price_with_discount_is_shown(self):
        return self.browser.find_element(*self.price_without_discount).is_displayed()

    def calculate_percentage(self, old_value, new_value):
        difference = old_value - new_value
        percentage = difference/old_value
        return percentage

    def most_discount_cruise(self):
        cruise_with_most_discount = [-11111, None]

        for i in self.browser.find_elements(*self.results_with_discount):
            price_area = i.find_element(*self.results_price_area)

            # Process to obtain float value of original price.
            original_amount_container = price_area.find_element(*self.price_without_discount)
            original_amount = original_amount_container.find_element(*self.price_without_discount).text
            original_amount = original_amount.replace("$", "")
            original_amount = original_amount.replace(",", ".")
            original_amount = float(original_amount)

            # Process to obtain float value of discounted price.
            discount_amount = price_area.find_element(*self.cruise_price).text
            discount_amount = discount_amount.replace("$", "")
            discount_amount = discount_amount.replace(",", ".")
            discount_amount = float(discount_amount)

            discount_percentage = self.calculate_percentage(original_amount, discount_amount)

            if discount_percentage > cruise_with_most_discount[0]:
                cruise_with_most_discount[0] = discount_percentage
                cruise_with_most_discount[1] = price_area.find_element(*self.cruise_continue_button)

        cruise_with_most_discount[1].click()

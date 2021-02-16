from selenium.webdriver.common.by import By


class PackageReviewPage:
    add_car_button = (By.CSS_SELECTOR, "button[class='btn-secondary btn-sub-action  gt-add-btn']")

    def __init__(self, browser):
        self.browser = browser

    def add_a_car(self):
        self.browser.find_element(*self.add_car_button).click()

    def validate_trip_review(self):
        pass

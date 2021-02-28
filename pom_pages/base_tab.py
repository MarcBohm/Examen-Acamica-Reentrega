from selenium.webdriver.common.by import By
import time


class BaseTab:
    # Locators
    date_picker_departing_button = (By.ID, "d1-btn")
    date_picker_next_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][2]")
    date_picker_check_in_button = (By.ID, "d1-partial-btn")
    date_picker_previous_month = (By.XPATH, "//button[@data-stid='date-picker-paging'][1]")
    second_week_first_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[2]/td[1]")
    third_week_seventh_day = (By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]/table/tbody/tr[3]/td[7]")
    date_picker_done_button = (By.CSS_SELECTOR, "button[data-stid='apply-date-picker']")
    search_button = (By.CSS_SELECTOR, "button[data-testid='submit-button']")

    def __init__(self, browser):
        self.browser = browser

    def set_valid_dates(self):
        self.browser.find_element(*self.date_picker_departing_button).click()
        # couldn't set an explicit wait for item to be clickable
        time.sleep(1)
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.date_picker_next_month).click()
        self.browser.find_element(*self.second_week_first_day).click()
        self.browser.find_element(*self.third_week_seventh_day).click()
        self.browser.find_element(*self.date_picker_done_button).click()

    def set_invalid_dates(self):
        self.browser.find_element(*self.date_picker_check_in_button).click()
        # couldn't set an explicit wait for previous_month to be clickable
        time.sleep(1)
        self.browser.find_element(*self.date_picker_previous_month).click()
        self.browser.find_element(*self.second_week_first_day).click()
        self.browser.find_element(*self.third_week_seventh_day).click()
        self.browser.find_element(*self.date_picker_done_button).click()

    def click_search(self):
        self.browser.find_element(*self.search_button).click()

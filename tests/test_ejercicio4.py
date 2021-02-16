from pages.home_page import TravelocityHomePage
from pages.home_page import PackagesTab


def test_error_message_displayed(browser):
    home_page = TravelocityHomePage(browser)
    packages_page = PackagesTab(browser)
    home_page.load()

    # Step 1
    home_page.switch_to_packages_tab()

    # Step 2
    packages_page.complete_leaving_from_field("LAX")
    packages_page.complete_going_to_field("LAS")
    packages_page.set_valid_dates()

    # Step 3
    packages_page.accommodations_click()

    # Step 4
    packages_page.set_invalid_dates()
    packages_page.click_search()

    # Step 5
    check_in_error_message = packages_page.check_in_error()
    check_out_error_message = packages_page.check_out_error()
    assert check_in_error_message and check_out_error_message

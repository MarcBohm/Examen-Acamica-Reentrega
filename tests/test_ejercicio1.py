from pages.home_page import TravelocityHomePage
from pages.home_page import FlightTab
from pages.flight_search_page import FlightSearchPage


def test_booking_a_flight(browser):
    home_page = TravelocityHomePage(browser)
    home_page.load()
    home_page.switch_to_flight_tab()

    # Step 1
    flight_tab = FlightTab(browser)
    flight_tab.complete_going_to_field("LAS")
    flight_tab.complete_leaving_from_field("LAX")
    flight_tab.set_valid_dates()
    flight_tab.click_search()

    # Step 2 a)
    flight_search_page = FlightSearchPage(browser)
    flight_search_page.validate_sort_dropdown_is_visible()

    # Step 2 b) c) d)
    flight_search_page.results_validations()



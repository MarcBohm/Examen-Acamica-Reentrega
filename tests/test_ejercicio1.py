from pages.home_page import TravelocityHomePage
from pages.home_page import FlightTab
from pages.flight_search_page import FlightSearchPage
from pages.trip_review_page import TripReviewPage
import time


def test_booking_a_flight(browser):
    home_page = TravelocityHomePage(browser)
    home_page.load()
    home_page.switch_to_flight_tab()

    # Step 1
    flight_tab = FlightTab(browser)
    flight_tab.complete_going_to_field()
    flight_tab.complete_leaving_from_field()
    flight_tab.set_valid_dates()
    flight_tab.click_search()

    # Step 2 a)
    flight_search_page = FlightSearchPage(browser)
    flight_search_page.validate_sort_dropdown_is_visible()

    # Step 2 b) c) d)
    flight_search_page.results_validations()

    # Step 3
    flight_search_page.sort_by_duration_shorter()
    time.sleep(1)
    flight_search_page.validate_duration_sorted_correctly()

    # Step 4
    flight_search_page.select_first_flight()

    # Step 5
    time.sleep(1)
    flight_search_page.select_third_flight()
    time.sleep(1)
    flight_search_page.reject_hotel_offer()

    # Step 6
    flight_search_page.focus_on_trip_review()
    trip_review_page = TripReviewPage(browser)
    trip_review_page.verify_trip_details()

    # Step 7
    trip_review_page.continue_booking()

    # Step 8
    time.sleep(1)
    trip_review_page.validate_who_travelling()

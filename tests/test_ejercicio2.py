from pages.home_page import TravelocityHomePage
from pages.home_page import PackagesTab
from pages.packages_search_page import PackagesSearchPage
from pages.three_star_hotel_page import ThreeStarHotelPage
from pages.departure_flight_page import DepartureFlightPage
from pages.return_flight_page import ReturnFlightPage
from pages.package_review_page import PackageReviewPage
import time


def test_flight_with_hotel_and_car(browser):
    home_page = TravelocityHomePage(browser)
    packages_page = PackagesTab(browser)
    home_page.load()

    # Step 1
    home_page.switch_to_packages_tab()

    # Step 2
    packages_page.complete_leaving_from_field("LAS")
    packages_page.complete_going_to_field("LAX")
    packages_page.set_valid_dates()
    packages_page.click_search()

    # Step 3
    packages_search_page = PackagesSearchPage(browser)
    packages_search_page.validate_departure()
    packages_search_page.validate_destination()
    packages_search_page.direct_flight_checkbox_value("false")
    packages_search_page.only_accommodations_checkbox_value("false")

    # Step 4
    packages_search_page.sort_by_price()
    time.sleep(1)
    packages_search_page.validate_sort_by_price()

    # Step 5
    picked_hotel_data = packages_search_page.select_first_three_star_hotel()
    packages_search_page.focus_on_hotel_page()

    # Step 6
    three_star_hotel_page = ThreeStarHotelPage(browser)
    three_star_hotel_page.validate_correct_hotel(picked_hotel_data)

    # Step 7
    three_star_hotel_page.select_first_room()

    # Step 8
    departure_flight_page = DepartureFlightPage(browser)
    departure_flight_page.select_first_flight()

    # Step 9
    time.sleep(1)
    return_flight_page = ReturnFlightPage(browser)
    return_flight_page.select_third_flight()

    # Step 10
    package_review_page = PackageReviewPage(browser)
    package_review_page.add_a_car()

    # Step 11
    package_review_page.validate_trip_review(picked_hotel_data)

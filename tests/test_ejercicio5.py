from pages.cruises_page import TravelocityCruisesPage
from pages.cruises_page import CruisesSearchPage
from pages.cruise_reservation_page import CruiseReservationPage
import time


def test_cruises_discount_is_displayed(browser):
    # Step 1
    cruises_page = TravelocityCruisesPage(browser)
    cruises_page.load()

    # Step 2
    cruises_page.select_europe()

    # Step 3 - By default the page sets a 'depart as late as' of approximately one month.
    cruises_page.search()

    # Step 4
    cruises_search_page = CruisesSearchPage(browser)
    assert cruises_search_page.destination_filter_text() == "Europe"

    # Step 5
    assert cruises_search_page.cruises_filter_is_shown()
    cruises_search_page.cruise_length_10_14()

    # Step 6
    assert cruises_search_page.price_with_discount_is_shown()

    # Step 7
    time.sleep(2)
    cruises_search_page.most_discount_cruise()

    """
    #Step 8
    cruise_reservation = CruiseReservationPage(browser)
    assert cruise_reservation.information_is_shown()
    """


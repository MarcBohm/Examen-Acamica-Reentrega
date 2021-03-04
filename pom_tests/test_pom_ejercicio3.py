from pom_pages.hotels_page import HotelPage
from pom_pages.hotels_search_page import HotelSearchPage


def test_search_by_hotel_name(browser):
    # Step 1
    hotel_page = HotelPage(browser)
    hotel_page.load("https://www.travelocity.com/Hotels")

    # Step 2
    hotel_page.search_hotel()

    # Step 3
    hotel_search_page = HotelSearchPage(browser)
    hotel_search_page.first_result_from_listing()
    hotel_search_page.member_discount()

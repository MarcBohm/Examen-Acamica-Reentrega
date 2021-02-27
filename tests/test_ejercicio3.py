from pages.hotels_page import TravelocityHotelsPage


def test_search_by_hotel_name(browser):
    # Step 1
    hotel_page = TravelocityHotelsPage(browser)
    hotel_page.load()

    # Step 2
    hotel_page.search_hotel()

    # Step 3.a
    assert hotel_page.first_result_from_listing() == "Ad"

    # Step 3.b
    assert "Member Discounts" in hotel_page.member_discount()

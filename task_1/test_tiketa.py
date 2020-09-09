import pytest
from selenium.webdriver import Chrome

from pages.search import TiketaSearch
from pages.event import TiketaEvent
from pages.select import TiketaSelect


@pytest.fixture
def browser():
    driver = Chrome("../chromedriver")
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


def test_select_and_buy_a_ticket_on_tiketa(browser):
    # test case data
    keyword = "Forum"
    date_from = "2020-09-01"
    date_to = "2020-12-31"

    # load Tiketa and search for the given keyword and dates
    search_page = TiketaSearch(browser)
    search_page.load_page()
    search_page.search(keyword)
    search_page.select_city()
    search_page.select_dates(date_from, date_to)
    search_page.initiate_search()

    # verify the results appear and move to the next page
    assert search_page.count_results() > 0
    search_page.initiate_buying()

    # initialize the event page and verify our search keyword is in the
    # event title
    event_page = TiketaEvent(browser)
    assert keyword in event_page.find_event_title()

    # move on buying the ticket, without login
    event_page.continue_buying_the_ticket()
    event_page.continue_without_registration()

    select_page = TiketaSelect(browser)
    # verify we are on the right page
    assert select_page.find_panel_title() == "Select tickets"

    # Here is where the test fails because of the captcha
    select_page.select_ticket_price()
    assert select_page.find_total_price() == "41,20 €"

    select_page.select_event_sector()
    select_page.find_tickets()

    assert select_page.find_total_cart_sum() == "41,20 €"

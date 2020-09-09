from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TiketaSearch:
    url = "https://www.tiketa.lt/EN/search"
    search_input = (By.NAME, "sf_TextFilter")
    city_dropdown = (By.ID, "dropdownMenu3")
    kaunas_item = (By.CSS_SELECTOR, "[data-id='2']")
    from_date = (By.NAME, "sf_DateFrom")
    to_date = (By.NAME, "sf_DateTo")
    search_button = (By.CSS_SELECTOR,
                     "#advSearchForm > div.advanced-search-submit-btn.col-xs-12.text-right > button")
    results = (By.CLASS_NAME, "article")
    buy_button_1 = (By.ID, "btnBuy-23125")

    def __init__(self, browser):
        self.driver = browser

    def load_page(self):
        self.driver.get(self.url)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.search_input)
        search_input.send_keys(phrase + Keys.TAB)

    def select_city(self):
        city_dropdown = self.driver.find_element(*self.city_dropdown)
        city_dropdown.click()
        kaunas_item = self.driver.find_element(*self.kaunas_item)
        kaunas_item.click()

    def select_dates(self, beginning_date, end_date):
        from_date_field = self.driver.find_element(*self.from_date)
        from_date_field.send_keys(beginning_date)
        to_date_field = self.driver.find_element(*self.to_date)
        to_date_field.send_keys(end_date)

    def initiate_search(self):
        submit_button = self.driver.find_element(*self.search_button)
        submit_button.click()

    def count_results(self):
        events = self.driver.find_elements(*self.results)
        return len(events)

    def initiate_buying(self):
        buy_button = self.driver.find_element(*self.buy_button_1)
        buy_button.click()
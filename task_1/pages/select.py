from selenium.webdriver.common.by import By


class TiketaSelect:
    select_tickets = (By.ID, "accTickets")
    select_price = (By.ID, "rb_Price252067")
    total_price = (By.ID, "tot_PriceTotal")
    select_sector = (By.ID, "rb_Sector578392")
    find_tickets = (By.ID, "btnFindTickets")
    total_cart_sum = (By.ID, "sdTotMain")

    def __init__(self, browser):
        self.driver = browser

    def find_panel_title(self):
        panel_title = self.driver.find_element(*self.select_tickets)
        return panel_title.text

    def select_ticket_price(self):
        price = self.driver.find_element(*self.select_price)
        price.click()

    def find_total_price(self):
        total_price = self.driver.find_element(*self.total_price)
        return total_price.text

    def select_event_sector(self):
        sector = self.driver.find_element(*self.select_sector)
        sector.click()

    def find_tickets(self):
        find_tickets_button = self.driver.find_element(*self.find_tickets)
        find_tickets_button.click()

    def find_total_cart_sum(self):
        total_cart = self.driver.find_element(*self.total_cart_sum)
        return total_cart.text
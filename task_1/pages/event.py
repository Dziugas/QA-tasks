from selenium.webdriver.common.by import By


class TiketaEvent:
    buy_button_2 = (By.XPATH, "//*[@id='main-container']/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[4]/div/div/a")
    no_registration_link = (By.XPATH, "//*[@id='btnNoLogin']")
    title = (By.CLASS_NAME, "title")

    def __init__(self, browser):
        self.driver = browser

    def find_event_title(self):
        event_title = self.driver.find_element(*self.title)
        return event_title.text

    def continue_buying_the_ticket(self):
        ticket = self.driver.find_element(*self.buy_button_2)
        ticket.click()

    def continue_without_registration(self):
        no_registration = self.driver.find_element(*self.no_registration_link)
        no_registration.click()
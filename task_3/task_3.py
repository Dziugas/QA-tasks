import time
from selenium.webdriver import Chrome


class ChallengingDom:
    url = "http://the-internet.herokuapp.com/challenging_dom"

    def __init__(self):
        self.driver = Chrome("../chromedriver")
        self.driver.implicitly_wait(10)

    def load_page(self):
        self.driver.get(self.url)

    def quit_driver(self):
        self.driver.quit()

    def highlight(self, element, seconds):
        """Highlights a Selenium Webdriver element for a given amount of time"""
        driver = element._parent
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)
        original_style = element.get_attribute("style")
        apply_style("background: blue; border: 2px solid black;")
        time.sleep(seconds)
        apply_style(original_style)

    def get_index_of_a_given_column_name(self, column_name):
        """Returns the index of a column where we want to find elements"""
        head_columns = self.driver.find_elements_by_tag_name("th")
        for count, column in enumerate(head_columns, start=0):
            if column.text == column_name:
                return count

    def find_a_row_by_a_given_value(self, value):
        """Returns a row element in which the value is situated"""
        table_rows = self.get_table_rows_without_head()
        for count, row in enumerate(table_rows, start=0):
            cells_in_row = row.find_elements_by_tag_name("td")
            for cell in cells_in_row:
                if cell.text == value:
                    return table_rows[count]

    def get_table_rows_without_head(self):
        """Returns all table rows without the head row"""
        table_body = self.driver.find_element_by_tag_name("tbody")
        table_rows_without_head = table_body.find_elements_by_tag_name("tr")
        return table_rows_without_head

    def highlight_the_element_in_a_given_row_and_column_for_given_time(self, column, row, time):
        # cells in the given row
        table_rows = self.get_table_rows_without_head()
        cells_in_row = table_rows[row-1].find_elements_by_tag_name("td")

        # find index of the given column
        index = self.get_index_of_a_given_column_name(column)

        wanted_element = cells_in_row[index]
        self.highlight(wanted_element, time)

    def highlight_the_action_button_in_the_row_of_the_given_value(self, value, action, seconds):
        wanted_row = self.find_a_row_by_a_given_value(value)
        wanted_col_index = self.get_index_of_a_given_column_name("Action")

        cells_in_row = wanted_row.find_elements_by_tag_name("td")
        action_cel = cells_in_row[wanted_col_index]

        if action == "delete":
            action_button = action_cel.find_elements_by_tag_name("a")[1]
        elif action == "edit":
            action_button = action_cel.find_elements_by_tag_name("a")[0]

        self.highlight(action_button, seconds)

    def highlight_text_element_for_a_given_time(self, value, time):
        wanted_row = self.find_a_row_by_a_given_value(value)
        cells_in_row = wanted_row.find_elements_by_tag_name("td")
        for cell in cells_in_row:
            if cell.text == value:
                    self.highlight(cell, time)

    def highlight_the_green_button(self):
        """Locates the button frame and the green button in it and clicks"""
        buttons = self.driver.find_element_by_class_name("large-2")
        green_button = buttons.find_elements_by_tag_name("a")[2]
        green_button.click()

table = ChallengingDom()
table.load_page()
table.highlight_the_element_in_a_given_row_and_column_for_given_time("Diceret", 3, 2)
table.highlight_the_action_button_in_the_row_of_the_given_value("Apeirian7", "delete", 2)
table.highlight_the_action_button_in_the_row_of_the_given_value("Apeirian2", "edit", 2)
table.highlight_text_element_for_a_given_time("Definiebas7", 2)
table.highlight_text_element_for_a_given_time("Iuvaret7", 2)
table.highlight_the_green_button()
table.quit_driver()
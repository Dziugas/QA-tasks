import time

from selenium import webdriver


def highlight(element, seconds):
    """Highlights a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute("style")
    apply_style("background: blue; border: 2px solid black;")
    time.sleep(seconds)
    apply_style(original_style)

driver = webdriver.Chrome("../chromedriver")

driver.get("http://the-internet.herokuapp.com/challenging_dom")
driver.implicitly_wait(10)

# find the table
table = driver.find_element_by_tag_name("table")

table_head = table.find_element_by_tag_name("thead")
head_columns = table_head.find_elements_by_tag_name("th")

# find indexes of each column where we want to find elements
for count, column in enumerate(head_columns, start=0):
    if column.text == "Diceret":
        diceret_col = count
    if column.text == "Action":
        action_col = count
    if column.text == "Ipsum":
        ipsum_col = count
    if column.text == "Sit":
        sit_col = count
    if column.text == "Lorem":
        lorem_col = count

table_body = table.find_element_by_tag_name("tbody")
# get all rows in the table body
table_rows = table_body.find_elements_by_tag_name("tr")

# cells in the 3rd row
cells_3rd_row = table_rows[2].find_elements_by_tag_name("td")
# find element wanted in "Diceret" column
diceret_element = cells_3rd_row[diceret_col]
highlight(diceret_element, 2)

# cells in the 7th row
cells_7th_row = table_rows[7].find_elements_by_tag_name("td")
# find element wanted in "Action" column
action_cel = cells_7th_row[action_col]
delete = action_cel.find_elements_by_tag_name("a")[1]
highlight(delete, 2)

# cells in the 2nd row
cells_2nd_row = table_rows[2].find_elements_by_tag_name("td")
# find element wanted in "Action" column
action_cel = cells_2nd_row[action_col]
edit = action_cel.find_elements_by_tag_name("a")[0]
highlight(edit, 2)

# we already have the cells from the 7th row
definiebas7 = cells_7th_row[sit_col]
# find element wanted in "Lorem" column
iuvaret7 = cells_7th_row[lorem_col]
highlight(definiebas7, 2)
highlight(iuvaret7, 2)

# select the button frame and the green button in it
buttons = driver.find_element_by_class_name("large-2")
green_button = buttons.find_elements_by_tag_name("a")[2]
green_button.click()



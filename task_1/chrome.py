from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


headless_options = Options()
headless_options.add_argument("--headless")

driver = webdriver.Chrome("../chromedriver", options=headless_options)
driver.implicitly_wait(10)

driver.get("https://www.tiketa.lt/EN/search")

actions = ActionChains(driver)

# getting the whole search box
advanced_search = driver.find_element_by_class_name("advanced-search-block")

# enter what we're looking for in a search bar
search_name = advanced_search.find_element_by_class_name("search-name")
search_field = search_name.find_element_by_class_name("twitter-typeahead")
search_inputs = search_field.find_elements_by_tag_name("input")
caption_field = search_inputs[1]
caption_field.send_keys("Forum")
search_inputs[1].send_keys(Keys.TAB)

# look up the city
city_search = advanced_search.find_element_by_id("search-city")
city_dropdown = city_search.find_element_by_id("dropdownMenu3")
city_dropdown.click()
kaunas_item = city_search.find_element_by_css_selector("[data-id='2']")
kaunas_item.click()

# select dates
date_search = advanced_search.find_element_by_class_name("search-time")
calendars = date_search.find_elements_by_class_name("calendar")
from_date_field = calendars[0]
from_date_field.send_keys("2020-09-01")
to_date_field = calendars[1]
to_date_field.send_keys("2020-12-31")

# initiate search
search_submit = advanced_search.find_element_by_class_name("advanced-search-submit-btn")
submit_button = search_submit.find_element_by_tag_name("button")
submit_button.click()

# wait for the results to load, locate the wanted event and select buy
wait = WebDriverWait(driver, 10)
buy_button = wait.until(EC.element_to_be_clickable((By.ID, ("btnBuy-23125"))))
actions.move_to_element(buy_button).click().perform()

# locate the wanted event and select "buy"
ticket = driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[4]/div/div/a')
ticket.click()

# go further without logging in
no_registration = driver.find_element_by_xpath('//*[@id="btnNoLogin"]')
no_registration.click()

# This is wheere I get a google captcha...
# ...and the below code does not work

# prices = driver.find_elements_by_class_name("price-container-block")
# prices[-1].click()

driver.close()
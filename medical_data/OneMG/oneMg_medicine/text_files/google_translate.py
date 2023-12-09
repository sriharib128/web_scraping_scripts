from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://translate.google.co.in/")

########################## select Document Translation

# div_class = driver.find_element(By.CLASS_NAME,"hgbeOc.EjH7wc")
button = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Document translation"]')
button.click()

########################## select english
# div_class = driver.find_element(By.CLASS_NAME,"hgbeOc.EjH7wc")
button = driver.find_element(By.CSS_SELECTOR,'button[aria-label="More source languages"]')
button.click()
# Find the parent div element that contains the dropdown options
dropdown_parent = driver.find_element(By.CLASS_NAME, 'dykxn.MeCBDd.j33Gae')  # Replace with the actual class
desired_language_code = 'en'
# Construct a CSS selector that targets the div with the specific data-language-code
css_selector = f'div[data-language-code="{desired_language_code}"]'
# Locate the specific div element within the dropdown
option_to_select = dropdown_parent.find_element(By.CSS_SELECTOR, css_selector)
option_to_select.click()

########################### select telugu
button = driver.find_element(By.CSS_SELECTOR,'button[aria-label="More target languages"]')
button.click()
# Find the parent div element that contains the dropdown options
dropdown_parent = driver.find_element(By.CLASS_NAME, 'dykxn.MeCBDd.j33Gae')  # Replace with the actual class
desired_language_code = 'te'
# Construct a CSS selector that targets the div with the specific data-language-code
css_selector = f'div[data-language-code="{desired_language_code}"]'
# Locate the specific div element within the dropdown
option_to_select = dropdown_parent.find_element(By.CSS_SELECTOR, css_selector)
option_to_select.click()

########################### select input file
file_input = driver.find_element(By.ID,"ucj-20")  # Replace with the actual element locator for the file input field
file_input.send_keys("path/to/your/file.txt")

############################ click on translate
button = driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.nCP5yc.AjY5Oe.LQeN7.sWFiQe")  # Replace with the actual class name
button.click()

############################ select translate
translate_button = driver.find_element(By.ID,"translate_button_id")  # Replace with the actual element locator for the Translate button
translate_button.click()

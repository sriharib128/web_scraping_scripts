import requests
from bs4 import BeautifulSoup
import pprint
import re
from selenium import webdriver
import pickle
from selenium.webdriver.common.by import By  # Import the locating strategy

def is_single_letter(s):
    return len(s) == 1

def get_text(temp_url,a,b):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)

    # Open the URL
    driver.get(temp_url)

    # Find and print the main content of the page
    # main_content = driver.find_element("class name", "col-6.marginTop-16")
    main_content = driver.find_element(By.CLASS_NAME, "col-6.marginTop-16")

    with open(f'corpus_{a}_{b}.txt', 'a') as file:
        file.write(main_content.text)

    # Close the browser
    driver.quit()

# Open the file in binary mode
with open('disease.pkl', 'rb') as file:
    # Call load method to deserialze
    disease_links = pickle.load(file)

with open('letter.pkl', 'rb') as file:
    # Call load method to deserialze
    letter_links = pickle.load(file)


for a in range(len(letter_links)):
    print (f"==> {a}")
    for b in range(len(disease_links[a])):
        get_text(disease_links[a][b],a,b)
        print(f" b - {disease_links[a][b]}")
    print("---------------")
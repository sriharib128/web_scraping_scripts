import re
import requests
import pickle
import pprint
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the locating strategy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time  # Import the time module for adding delays

global_time = time.time()

def get_text(driver):

    categories = [["overview","DrugOverview__content___22ZBX"],["uses_and_benefits","ShowMoreArray__tile___2mFZk"],["faq","Faqs__tile___1B58W"]]

    # OverView:
    category = categories[0]
    try :
        main_content = driver.find_element(By.ID, category[0])
        div_class = main_content.find_elements(By.CLASS_NAME,category[1])
        temp_text=""
        for element in div_class:
            temp_text += element.text
        temp_text = re.sub(r'\n+', '\n', temp_text)
        temp_text = re.sub(r'\. ', '.\n', temp_text)
        result = '\n'.join(temp_text.split('\n')[:-3])
        text = result + "\n=\n"
        with open(f"./category_text/{category[0]}.txt","a") as file:
            print(text,file = file)
    except NoSuchElementException:
        return 1

    # Benefits and Uses:
    category = categories[1]
    try:
        main_content = driver.find_element(By.ID, category[0])
        try:
            # Locate and click the "Show more" button if it exists
            show_more_button = main_content.find_element(By.CLASS_NAME, 'ShowMoreArray__toggle___3yZBW.ShowMoreArray__more___YceZH')
            show_more_button.click()

            # Wait for the new content to load
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ShowMoreArray__content___2OHDK')))
        except NoSuchElementException:
            pass
        div_class = main_content.find_element(By.CLASS_NAME,category[1])
        temp_text = div_class.text
        temp_text = re.sub(r'\n+', '\n', temp_text)
        temp_text = re.sub(r'\. ', '.\n', temp_text)
        result = '\n'.join(temp_text.split('\n')[:-1])
        text = result + "\n=\n"
        # Using "a" mode
        try:
            with open(f"./category_text/{category[0]}.txt","a") as file:
                print(text,file = file)
        except FileNotFoundError:
            with open(f"./category_text/{category[0]}.txt","w") as file:
                print(text,file = file)

    except NoSuchElementException:
        pass

    # FAQs:
    category = categories[2]
    try:
        main_content = driver.find_element(By.ID, category[0])
        div_class = main_content.find_element(By.CLASS_NAME,category[1])
        try:
            # Locate and click the "Show more" button if it exists
            show_more_button = main_content.find_element(By.CLASS_NAME, 'Faqs__toggle___2u7v1.Faqs__more___2iZTr')
            show_more_button.click()

            # Wait for the new content to load
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Faqs__content___2_NYj')))

        except NoSuchElementException:
            pass
        temp_text = div_class.text
        temp_text = re.sub(r'\n+', '\n', temp_text)
        temp_text = re.sub(r'\. ', '.\n', temp_text)
        temp_sentences = temp_text.split("\n")[:-1]
        sentences = [sentence for sentence in temp_sentences if len(sentence.split()) > 5]
        result = '\n'.join(sentences)
        text = result + "\n=\n"
        try:
            with open(f"./category_text/{category[0]}.txt","a") as file:
                print(text,file = file)
        except FileNotFoundError:
            with open(f"./category_text/{category[0]}.txt","w") as file:
                print(text,file = file)
    except NoSuchElementException:
        pass
    driver.quit()
    return None

def get_text_with_retry(temp_url, proxy_url, a, max_retries=1, retry_delay=60):

    start = time.time()
    chrome_options = webdriver.ChromeOptions()
    
    if proxy_url is not None:
        chrome_options.add_argument(f'--proxy-server={proxy_url}')
    
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(temp_url)
# proxy_url = '103.159.46.10:83'
proxy_url = None
with open("./links_10_0.txt") as file:
    links = file.readlines()
a=0
# for temp_url in links:
temp_url = "https://www.1mg.com/drugs/a-125-suspension-461268"
get_text_with_retry(temp_url, proxy_url,a, max_retries=1, retry_delay=60)
a+=1
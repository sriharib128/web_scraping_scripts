import pickle
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests

source = "en"
lang = "te"
def get_text(temp_url,a):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)

    # Open the URL
    driver.get(temp_url)
    time.sleep(10)
    # Find and print the main content of the page
    heading = driver.find_element("class name", "DrugHeader__title-content___2ZaPo")
    # list = ["overview",""]
    # main_content = driver.find_elements("id", "Benefits of Chymoral Tablet-0")
    main_content = driver.find_elements("class name", "DrugOverview__content___22ZBX")

    with open(f'corpus_{a}.txt', 'a') as file:
        file.write(heading.text)
        input = ""
        for content in main_content:
            input += content.text +"\n"
        driver.get("https://translate.google.co.in/?sl="+source+"&tl="+lang+"&text="+input+"&op=translate")
        time.sleep(6)
        output = driver.find_element("class name","HwtZe").text
        print(output)
    # Close the browser
    driver.quit()

# for a in range(26):
a=2
with open(f'medicine_links_{a}.pkl', 'rb') as file:
    medical_links = pickle.load(file)
    print(medical_links[a])
    get_text(medical_links[a],a)
    # get_text("https://www-1mg-com.translate.goog/drugs/chymoral-forte-tablet-145310?_x_tr_sl=en&_x_tr_tl=te&_x_tr_hl=en-US&_x_tr_pto=wapp",a)
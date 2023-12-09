from selenium import webdriver
from selenium.webdriver.common.by import By  
import time 

def get_text_with_retry(temp_url,file):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(temp_url)
    main_content = driver.find_element(By.ID,"MiddleColumn_internal")
    div_text = main_content.text
    print("\n",file)
    print(div_text,file)

with open("./vikas_all_links.txt") as file:
    links = file.readlines()
with open("./temp.txt","w") as file:
    a=0
    for temp_url in links:
        get_text_with_retry(temp_url,file)
        print(a)
        a+=1

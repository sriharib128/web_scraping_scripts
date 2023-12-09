import requests
from bs4 import BeautifulSoup
import pprint
import re
# from selenium import webdriver
import pickle

def is_single_letter(s):
    return len(s) == 1

# def get_text(temp_url,a,b):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
#     driver = webdriver.Chrome(options=options)

#     # Open the URL
#     driver.get(url)

#     # Find and print the main content of the page
#     main_content = driver.find_element("class name", "col-6.marginTop-16")

#     with open('corpus.txt', 'a') as file:
#         file.write((f'({main_content}_{a}_{b})').txt)

#     # Close the browser
#     driver.quit()

rows = 26

# Create an empty 2D array by initializing rows with empty lists
disease_links = [[] for _ in range(rows)]

# URL of the webpage to scrape
url = 'https://www.1mg.com/all-diseases'
urlbase='https://www.1mg.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

letter_links=[] #A to Z links

# Disease links are contained within <a> elements with class 'a-link-disease'\

disease_elements = soup.find_all('a', class_='a-link-disease')

all_links = soup.find_all('a')

# below for loop is for all diseases starting from A
for link in all_links:
    link_text = link.get_text()
    temp=link['href']
    if (is_single_letter(link_text)):
        letter_links.append(urlbase+temp)
    else:
        if(temp !='/' and temp!='/searchsuggestion' and temp!='/cart'):
            disease_links[0].append(urlbase+temp)

# below for loop is form all diseases from B to Z   
for a in range(1,len(letter_links)):
    disease_response = requests.get(letter_links[a])
    disease_soup = BeautifulSoup(disease_response.content, 'html.parser')
    temp_disease_elements = disease_soup.find_all('a', class_='a-link-disease')

    temp_all_links = disease_soup.find_all('a')
    for link in temp_all_links:
        link_text = link.get_text()
        temp=link['href']
        if (is_single_letter(link_text) != 1):
            if(temp !='/' and temp!='/searchsuggestion' and temp!='/cart'):
                disease_links[a].append(urlbase+temp)

with open('disease.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(disease_links, file)
with open('letter.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(letter_links, file)

sum=0

for a in range(len(letter_links)):
    print (f"==> {a}")
    sum+=len(disease_links[a])
    for b in range(len(disease_links[a])):
        # get_text(disease_links[a][b],a,b)
        print(f" b - {disease_links[a][b]}")
    print("---------------")
print(f'sum = {sum}')
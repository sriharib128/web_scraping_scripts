import requests
from bs4 import BeautifulSoup
import pprint
import re

def is_single_letter(s):
    return len(s) == 1

def get_text(temp_url):
    t_response = requests.get(temp_url)
    t_soup = BeautifulSoup(t_response.content, 'html.parser')
    p_tags = t_soup.find_all('p')

    corpus = ""

    for p in p_tags:
        line = p.get_text(separator=' ')
        corpus += re.sub(r'\.', '.\n', line)  # Add a newline after each period

    with open('corpus.txt', 'a') as file:
        file.write(corpus)

rows = 26

# Create an empty 2D array by initializing rows with empty lists
disease_links = [[] for _ in range(rows)]

# URL of the webpage to scrape
url = 'https://www.1mg.com/drugs-all-medicines'
# url = 'https://www.1mg.com/all-diseases?label=b'
urlbase='https://www.1mg.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

letter_links=[] #A to Z links

# Disease links are contained within <a> elements with class 'a-link-disease'\

# disease_elements = soup.find_all('a', class_='button-text.style__flex-row___2AKyf style__flex-1___A_qoj.style__product-name___HASYw')
disease_elements = soup.find_all('div', class_='style__width-100p___2woP5.style__flex-row___m8FHw')

# print(disease_elements)
i=0
# all_links = soup.find_all('a')
for link in disease_elements:
    print(link.prettify())
    # link_text = link.get_text()
    # temp=link['href']
    # # if (is_single_letter(link_text)):
    # letter_links.append(urlbase+temp)
    # print(letter_links[i])
    # i+=1
    # else:
    #     if(temp !='/' and temp!='/searchsuggestion' and temp!='/cart'):
    #         disease_links[0].append(urlbase+temp)

# for a in range(1,len(letter_links)):
#     disease_response = requests.get(letter_links[a])
#     disease_soup = BeautifulSoup(disease_response.content, 'html.parser')
#     temp_disease_elements = disease_soup.find_all('a', class_='a-link-disease')

#     temp_all_links = disease_soup.find_all('a')
#     for link in temp_all_links:
#         link_text = link.get_text()
#         temp=link['href']
#         if (is_single_letter(link_text) != 1):
#             if(temp !='/' and temp!='/searchsuggestion' and temp!='/cart'):
#                 disease_links[a].append(urlbase+temp)


sum=0
# Print the empty 2D array
# for a in range(len(letter_links)):
#     sum += len(disease_links[a])
#     print(f"{a} ==> {len(disease_links[a])}")
#     print(f" > {letter_links[a]}")
#     print(disease_links[a])
#     print("------------------")

# print(sum)

# for a in range(len(letter_links)):
#     print (f"==> {a}")
#     for b in range(len(disease_links[a])):
#         get_text(disease_links[a][b])
#         print(f" b - {disease_links[a][b]}")
#     print("---------------")
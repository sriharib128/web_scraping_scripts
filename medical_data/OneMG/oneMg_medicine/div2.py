from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = 'https://www.1mg.com/diseases/back-pain-943'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific <div> element that contains the nested <div> elements
parent_div = soup.find('div', class_='col-6.marginTop-16')  # Replace with the appropriate class or other attribute
print(parent_div)
# Find all <div> elements that are children of the parent <div>
# nested_divs = parent_div.find_all('div')

# # Print the text content of nested <div> elements
# for div in nested_divs:
    # print(div.get_text())

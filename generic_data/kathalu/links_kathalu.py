from bs4 import BeautifulSoup
import requests


url = "https://kathalu.wordpress.com/%e0%b0%a8%e0%b1%80%e0%b0%a4%e0%b0%bf-%e0%b0%95%e0%b0%a5%e0%b0%b2%e0%b1%81/"
# Parse the HTML content of the page using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

div_element = soup.find('div',class_= "entry-content")

# Find all <a> tags with the specified class
p_tags = div_element.find_all("p")

text = ""

for p_tag in p_tags:
    text =text+"\n"+ p_tag.text

with open("text.txt",'w') as fi:
    print(text,file = fi)

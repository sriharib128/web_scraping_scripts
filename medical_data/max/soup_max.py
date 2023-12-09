import requests
from bs4 import BeautifulSoup
import os
import time
import pickle

links = []

url = f"https://www.maxhealthcare.in/top-procedures"  # Replace with the actual URL

# Maximum number of retries
max_retries = 3

# Delay between retries (in seconds)
retry_delay = 5

retry_failed =1
for _ in range(max_retries):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find('section', class_='row no-gutters mx-n05 mx-lg-n10 speciality-box')

            # Find all <a> tags with the specified class
            a_tags = section.find_all("a")

            # Print the href attribute values (links) of the <a> tags
            for a_tag in a_tags:
                link = a_tag.get("href")
                if link:
                    links.append(link)
            retry_failed = 0
            # Break out of the loop if successful
            break
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))
    print("Retrying...")
    # Retry after a delay
    time.sleep(retry_delay)
if(retry_failed == 1):
    print(f"retry failed for link =>{url}")

with open(f'max_procedures_links.pkl', 'wb') as file:
        pickle.dump(links,file)
print(links)
print(len(links))
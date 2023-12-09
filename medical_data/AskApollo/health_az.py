import requests
from bs4 import BeautifulSoup
import os
import time
import pickle
links = []
filename = 'hot_blogs_links.pkl'

# Check if the file exists
if os.path.exists(filename):
    # If the file exists, load its contents into a variable
    with open(filename, 'rb') as file:
        links = pickle.load(file)

# Maximum number of retries
max_retries = 3

# Delay between retries (in seconds)
retry_delay = 5

retry_failed =1
for i in range(1,54):
    url = f"https://healthlibrary.askapollo.com/telugu/category/health-a-z/page/{i}"
    for _ in range(max_retries):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")

                div_element = soup.find('div', class_="td-ss-main-content")
                div_class = div_element.find_all('div',class_="td-module-thumb")
                
                #div class = "td-ss-main-content"
                    #div class = "td-module-thumb"
                        # ahref


                # Find all <a> tags with the specified class
                for div in div_class:
                    a_tags = div_element.find_all("a")
                    # Print the href attribute values (links) of the <a> tags
                    for a_tag in a_tags:
                        link = a_tag.get("href")
                        if link:
                            if link not in links:
                                links.append(link)
                retry_failed = 0
                print("one page done")
                # Break out of the loop if successful
                break
            elif(response.status_code == 404):
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

with open(f'hot_az_links.pkl', 'wb') as file:
        pickle.dump(links,file)
print(links)
print(len(links))

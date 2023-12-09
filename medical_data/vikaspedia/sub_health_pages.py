import requests
from bs4 import BeautifulSoup
import os
import time
import pickle
requests.packages.urllib3.disable_warnings() 

urlbase = f"https://te.vikaspedia.in"

# pages_links = []
# with open("./vikas_page_links.txt",'r') as fi:
#     for line in fi:
#         pages_links.append(line.strip())
all_links= []
# for url in pages_links:
# Maximum number of retries
max_retries = 3

# Delay between retries (in seconds)
retry_delay = 5
retry_failed =1
url = "https://te.vikaspedia.in/health/వ్యాధులు-మరియు-రుగ్మతలు"
for _ in range(max_retries):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url,verify=False)
        # print(1)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            div_element = soup.find('div', id="MiddleColumn_internal")

            # Find all <a> tags with the specified class
            a_tags = div_element.find_all("a")

            # Print the href attribute values (page_links) of the <a> tags
            for a_tag in a_tags:
                link = a_tag.get("href")
                if link:
                    all_links.append(urlbase+link)
            retry_failed = 0
            # Break out of the loop if successful
            break
        elif(response.status_code == 404):
            break
        else:
            print(f"{url}Failed to retrieve the web page. Status code:", response.status_code)
    except Exception as e:
        print(f"{url}An error occurred:", str(e))
    print(f"Retrying...{url}")
    # Retry after a delay
    time.sleep(retry_delay)
if(retry_failed == 1):
    print(f"retry failed for link =>{url}")
print(all_links)
# with open(f'vikas_all_links.txt', 'a',encoding="utf-8") as file:
#     for link in all_links:
#         file.write(link)
#         file.write("\n")

import requests
from bs4 import BeautifulSoup
import time
import pickle
import numpy as np
import sys


with open("max_procedures_links.pkl","rb") as fi:
    links  = pickle.load(fi)
print(links[58],links[59],links[60],links[61])
# sys.exit(1)

with open(f'./max_procedures.txt', 'a') as f:
    start_global = time.time()
    for i in range(60,len(links)):
        link = links[i]
        start = time.time()
        # URL of the web page you want to scrape
        url = link  # Replace with the actual URL

        # Maximum number of retries
        max_retries = 3

        # Delay between retries (in seconds)
        retry_delay = 5

        retry_failed = 1
        for _ in range(max_retries):
            try:
                # Send an HTTP GET request to the URL
                response = requests.get(url)

                # Check if the request was successful
                if response.status_code == 200:
                    # Parse the HTML content of the page using BeautifulSoup
                    soup = BeautifulSoup(response.text, "html.parser")

                    # Find all <a> tags with the specified class
                    div_with_class = soup.find("div", class_="sticky-top")

                    # Find all <a> tags with the specified class
                    p_tags = div_with_class.find_all("p")

                    # Print the href attribute values (links) of the <a> tags
                    for p_tag in p_tags:
                        # print(p_tag.text)
                        print(p_tag.text, file=f)

                    retry_failed = 0
                    # Break out of the loop if successful
                    break
                else:
                    print("Failed to retrieve the web page. Status code:", response.status_code)
            except Exception as e:
                print("An error occurred:", str(e))
            print(f"Retrying page {link}...")
            # Retry after a delay
            time.sleep(retry_delay)
        if retry_failed == 1:
            print(f"Retry failed for link => {url}")
            with open("temp_links.txt","a") as t:
                print(link,file =t)
        else:
            print(f"==> {i}th linkdone ==> {time.time()-start}s ==> total_elapsed = {(time.time() - (start_global))/60}min")



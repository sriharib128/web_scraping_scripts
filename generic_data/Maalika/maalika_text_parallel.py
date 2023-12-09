import requests
from bs4 import BeautifulSoup
import time
import pickle
import concurrent.futures
import numpy as np
import sys

# The class you want to target
target_class = "more-link"  # Replace with the actual class name
with open("maalika_links.pkl","rb") as fi:
    links  = pickle.load(fi)

# writing every 10 links into a text file
links_ten=[]
i=0
while i<len(links):
    links_ten.append(links[i:i+10])
    i+=10
start_global = time.time()

def scrape_page(pages_10_number):
    pages_10 = links_ten[pages_10_number]
    start = time.time()
    with open(f'./text_files/links_ten_{pages_10_number}.txt', 'w') as f:
        for page_link in pages_10:
            # URL of the web page you want to scrape
            url = page_link  # Replace with the actual URL

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
                        div_with_class = soup.find("div", class_="entry-content")

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
                print(f"Retrying page {page_link}...")
                # Retry after a delay
                time.sleep(retry_delay)
            if retry_failed == 1:
                print(f"Retry failed for link => {url}")
    
    print(f"==> {pages_10_number} (10 links) done ==> {time.time()-start}s ==> total_elapsed = {(time.time() - (start_global))/60}min")

# Number of threads for parallelization (you can adjust this)
num_threads = 8
pages_10_number = range(len(links_ten))
# Using a ThreadPoolExecutor to parallelize the scraping
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(scrape_page, pages_10_number)


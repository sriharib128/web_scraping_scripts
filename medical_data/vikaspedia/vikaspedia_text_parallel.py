import requests
from bs4 import BeautifulSoup
import time
import pickle
import concurrent.futures
import numpy as np
import sys
requests.packages.urllib3.disable_warnings() 

# The class you want to target
target_class = "more-link"  # Replace with the actual class name
links = []
with open("./vikas_all_links.txt",'r') as fi:
    for line in fi:
        links.append(line.strip())

# writing every 10 links into a text file
links_30=[]
i=0
while i<len(links):
    links_30.append(links[i:i+30])
    i+=30
start_global = time.time()

def scrape_page(pages_30_number):
    pages_30 = links_30[pages_30_number]
    start = time.time()
    with open(f'./vikaspedia_text_files/medyblog_10_{pages_30_number}.txt', 'w') as f:
        for page_link in pages_30:
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
                    response = requests.get(url,verify=False)

                    # Check if the request was successful
                    if response.status_code == 200:
                        # Parse the HTML content of the page using BeautifulSoup
                        soup = BeautifulSoup(response.text, "html.parser")
                        div_with_id = soup.find("div",id ='MiddleColumn_internal')
                        # Get the entire text from the <div> element
                        div_text = div_with_id.text
                        print(div_text, file=f)
                        retry_failed = 0
                        # Break out of the loop if successful
                        break
                    elif response.status_code == 404:
                        print(f"{url} - 404")
                        break
                    elif response.status_code == 400:
                        print(f"{url} - 400")
                        break
                    elif response.status_code == 429:
                        print(f"{url} - {pages_30_number} - 429")
                        time.sleep(60)
                    else:
                        print("Failed to retrieve the web page. Status code:", response.status_code)
                except Exception as e:
                    print(f"{url}-{pages_30_number}-An error occurred:", str(e))
                print(f"{url}-{pages_30_number}-Retrying page {page_link}...")
                # Retry after a delay
                time.sleep(retry_delay)
            if retry_failed == 1:
                print(f"{url}-{pages_30_number}-Retry failed for link")
    
    print(f"==> {pages_30_number} (10 links) done ==> {time.time()-start}s ==> total_elapsed = {(time.time() - (start_global))/60}min")

# Number of threads for parallelization (you can adjust this)
num_threads = 8
pages_30_number = range(len(links_30))
# Using a ThreadPoolExecutor to parallelize the scraping
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(scrape_page, pages_30_number)


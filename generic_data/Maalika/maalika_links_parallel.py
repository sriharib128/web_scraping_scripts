import requests
from bs4 import BeautifulSoup
import time
import pickle
import concurrent.futures

# The class you want to target
target_class = "more-link"  # Replace with the actual class name
links = []

def scrape_page(page_number):
    # URL of the web page you want to scrape
    url = f"http://maalika.org/magazine/page/{page_number}/"  # Replace with the actual URL

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
                a_tags = soup.find_all("a", class_=target_class)

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
        print(f"Retrying page {page_number}...")
        # Retry after a delay
        time.sleep(retry_delay)
    if retry_failed == 1:
        print(f"Retry failed for link => {url}")
    print(f"==> Page {page_number} done")

# Number of pages to scrape in parallel
page_numbers = range(1, 290)

# Number of threads for parallelization (you can adjust this)
num_threads = 8
for page_number in range(page_numbers):
    scrape_page(page_number)

# Using a ThreadPoolExecutor to parallelize the scraping
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(scrape_page, page_numbers)

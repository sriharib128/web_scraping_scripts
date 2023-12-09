import requests
from bs4 import BeautifulSoup
import time
import pickle

url = "http://maalika.org/magazine/2011/02/04/%e0%b0%ae%e0%b0%bf%e0%b0%b7%e0%b0%a8%e0%b1%8d-%e0%b0%a8%e0%b0%bf%e0%b0%a6%e0%b1%8d%e0%b0%b0/"
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

            div_with_class = soup.find("div", class_="entry-content")

            # Find all <a> tags with the specified class
            p_tags = div_with_class.find_all("p")

            # Print the href attribute values (links) of the <a> tags
            for p_tag in p_tags:
                print(p_tag.text)
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

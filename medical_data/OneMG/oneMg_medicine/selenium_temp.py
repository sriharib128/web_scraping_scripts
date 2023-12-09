from selenium import webdriver

# Initialize the ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)
temp_link = "https://www.1mg.com/drugs-all-medicines?page=43"

print(temp_link + " ")

driver.get(temp_link)
medicine_links=[]
# scraping medicine links in current page

div_element = driver.find_element('css selector', '.style__inner-container___3BZU9.style__product-grid___3noQW.style__padding-top-bottom-12px___1-DPF')
links = div_element.find_elements('tag name', 'a')
for temp_links in links:
    medicine_links.append(temp_links.get_attribute('href'))

print(medicine_links)
# finding the next link
div_element = driver.find_element('css selector', '.style__inner-container___3BZU9.style__white-bg___1qNti')
links = div_element.find_elements('tag name', 'a')
next_link = links[len(links) - 1].get_attribute('href')
print(next_link)
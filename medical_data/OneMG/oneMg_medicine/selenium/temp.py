from selenium import webdriver

# Specify the URL to scrape
url = "https://www.1mg.com/diseases/back-pain-943"

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

# Open the URL
driver.get(url)

# Find and print the main content of the page
main_content = driver.find_element("class name", "col-6.marginTop-16")

print(main_content.text)

# Close the browser
driver.quit()

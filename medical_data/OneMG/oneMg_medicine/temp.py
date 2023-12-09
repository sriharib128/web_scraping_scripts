from selenium import webdriver
# 

def get_text(url):
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
# Example usage
url = 'https://www.1mg.com/diseases/back-pain-943'
get_text(url)

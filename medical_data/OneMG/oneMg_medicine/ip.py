from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the proxy or VPN server address and port
proxy_url = '179.48.15.160:80'

# Create Chrome options with the proxy settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy_url}')
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Set up the Chrome WebDriver with the proxy
driver = webdriver.Chrome(options=chrome_options)

# Access a service like "httpbin.org" to get your public IP address
driver.get('https://httpbin.org/ip')

# Extract and print the public IP address
ip_element = driver.find_element(By.XPATH, '//pre')
public_ip = ip_element.text
print(f'Your Public IP Address: {public_ip}')

# When done, close the WebDriver
driver.quit()

from selenium import webdriver
import pickle
import os.path
import time

max_retries = 3
delay_between_retries = 5  # in seconds

# Initialize the ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

program_start = time.time()
if(not os.path.exists('./letters_links.pkl')):
    # Navigate to the URL
    url = 'https://www.1mg.com/drugs-all-medicines'
    driver.get(url)

    # A-Z
    div_element = driver.find_element('css selector', '.style__chips___2T95q')
    links = div_element.find_elements('tag name', 'a')

    letters_links=[]
    for link in links:
        letters_links.append(link.get_attribute('href')) # https://www.1mg.com/drugs-all-medicines?label=b
    with open('letters_links.pkl', 'wb') as file:
        pickle.dump(letters_links, file)
else:
    with open('letters_links.pkl', 'rb') as file:
        letters_links = pickle.load(file)
        print(f"loaded {file}")

a=0
if(os.path.exists('./a.pkl')):
    with open('a.pkl', 'rb') as file:
        a = pickle.load(file)
        print(f"a={a}")
for link in letters_links[a:]:
    temp_link = link
    medicine_links=[]
    start = time.time()
    while (True):
        if(temp_link is not None):
            print("==> "+temp_link + " " + str(len(medicine_links)))
            retries = 0
            err = False
            while retries < max_retries:
                try:
                    driver.get(temp_link)
                    # scraping medicine links in current page
                    div_element = driver.find_element('css selector', '.style__inner-container___3BZU9.style__product-grid___3noQW.style__padding-top-bottom-12px___1-DPF')
                    links = div_element.find_elements('tag name', 'a')
                    err = False
                    break  # Exit the retry loop if successful
                except Exception as e:
                    print(f"Error: {e}. Retrying...")
                    retries += 1
                    time.sleep(delay_between_retries)
                    err = True
            if (err is False):
                for temp_links in links:
                    medicine_links.append(temp_links.get_attribute('href'))
                # print(f"medicine links in letter {a} till now ==> {len(medicine_links)}")
            # if(len(medicine_links)>= 200):
            #     with open(f'medicine_links_{a}.pkl', 'wb') as file:
            #         pickle.dump(medicine_links,file)
            #     with open('a.pkl', 'wb') as file:
            #         pickle.dump(a,file)
            #     break
            # finding the next link
            retries=0
            err = False
            while retries < max_retries:
                try:
                    div_element = driver.find_element('css selector', '.style__inner-container___3BZU9.style__white-bg___1qNti')
                    links = div_element.find_elements('tag name', 'a')
                    err = False
                    break  # Exit the retry loop if successful
                except Exception as e:
                    print(f"Error: {e}. Retrying...")
                    retries += 1
                    err = True
                    time.sleep(delay_between_retries)
            if (err is False):
                next_link = links[len(links) - 1].get_attribute('href')
                temp_link = next_link
            else:
                temp_link = None
        else:
            break
    with open(f'medicine_links_{a}.pkl', 'wb') as file:
        pickle.dump(medicine_links,file)
    with open('a.pkl', 'wb') as file:
        pickle.dump(a,file)
    a+=1
    duration = (start - time.time())/60
    program_duration = (program_start-time.time())/60
    print(f'==========\n{link} ==> done in {duration} minutes ==> total elapsed = {program_duration} ==>\n=================')

print(f"ALL 26 Letters are done in {program_duration}")
    
# with open(f'medicine_links_{a}.pkl', 'wb') as file:
#     pickle.dump(medicine_links,file)
# Close the browser
driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import csv
from getpass import getpass #this is to hide the password entries on the portal

#here we are trying to scrape the website details from all the pages at the url

url = "https://quotes.toscrape.com/"
file_csv = "webscraping_via_selenium.csv"

#calling the service class passing driver manager file
service_obj = Service(executable_path="/usr/lib/chromium-browser/chromedriver")

# setting options for chromedriver
browser_option = Options()
#browser_option.add_argument("--headless")
browser_option.add_argument("--disable-gpu")
browser_option.add_argument('--start-fullscreen')
browser_option.add_argument("--disable-popup-blocking")

#loading the browser options & services with driver exe path to open the browser
driver = webdriver.Chrome(service=service_obj,options=browser_option)

#pushing the driver to launch the url
driver.get(url)

#finding the login & user name, password elements

login_btn = driver.find_element(By.LINK_TEXT,"Login")
login_btn.click()
user_name = driver.find_element(By.ID,"username")
user_name.send_keys("admin")
password = driver.find_element(By.ID,"password")
my_pswd = getpass() #the command/terminal waits for the user's password entry here
password.send_keys(my_pswd)
submit_btn = driver.find_element(By.XPATH,'//input[@type="submit"]')
submit_btn.click()

file = open(file_csv, "a")
writer = csv.writer(file)
writer.writerow(["Sl.No", "Author Name", "Quotes"])
serial_counter = 1
while True:
    authors = driver.find_elements(By.XPATH,'//span[@class="text"]')
    quotes = driver.find_elements(By.XPATH,'//small[@class="author"]')
    for i in range(0, len(authors)):
        writer.writerow([serial_counter, authors[i].text, quotes[i].text])
        serial_counter+=1
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        next_button.click()
        serial_counter += 1
    except NoSuchElementException:
        print("Scraping the website is done !!! ")
        break

file.close()
driver.quit()


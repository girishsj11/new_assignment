from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def main():
    data = dict() #to store the counties , capital & its currencies
    url = "https://catking.in/list-of-countries-capitals-currencies-of-the-world"
    service_obj = Service(executable_path="/usr/lib/chromium-browser/chromedriver") #with selenium4 we need to user Servcice class to initiate the driver exe path
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5) #applying implicit wait to load the all elements which is needed
    driver.get(url)
    tbody = driver.find_element(By.XPATH,'//tbody[@data-start="2340"]') #locating the table body
    data.update({'Country':('Capital','Currency')})

    for tr in tbody.find_elements(By.XPATH,'//tr'): #traversing to each rows with help of table body
        row = [item.text for item in tr.find_elements(By.XPATH,'.//td')] #traversing to each content in each row
        #print(f"Country :  capital , currency {row}")
        data[row[0]]= (row[1],row[2])

    print(data)
    print(len(data)-1) #ignoring the header row
    driver.quit()


if __name__ == "__main__":
    main()

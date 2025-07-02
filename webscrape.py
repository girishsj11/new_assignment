from bs4 import BeautifulSoup as bs
import requests

url = "https://quotes.toscrape.com/"
page_2_scrape = requests.get(url)
soup = bs(page_2_scrape.text,"html.parser")

quotes = soup.find_all("span",attrs={"class":"text"})
authors = soup.find_all("small",attrs={"class":"author"})

for i in range(0,len(quotes)):
    print(f"Author : {authors[i].text} \nQuotes : {quotes[i].text}\n")

from bs4 import BeautifulSoup as bs
import requests
import csv

url = "https://quotes.toscrape.com/"
file_csv = "authors_quotes.csv"
page_2_scrape = requests.get(url)
soup = bs(page_2_scrape.text,"html.parser")

quotes = soup.find_all("span",attrs={"class":"text"})
authors = soup.find_all("small",attrs={"class":"author"})

with open(file_csv,"w") as file:
    writer = csv.writer(file)
    writer.writerow(["Sl.No", "Author Name", "Quotes"])
    for i in range(0,len(authors)):
        writer.writerow([i+1,authors[i].text,quotes[i].text])

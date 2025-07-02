from bs4 import BeautifulSoup
import requests
import csv

url = "https://quotes.toscrape.com/"
file_csv = "authors_quotes.csv"
page_2_scrape = requests.get(url)
soup = BeautifulSoup(page_2_scrape.text,"html.parser")

quotes = soup.find_all("span",attrs={"class":"text"})
authors = soup.find_all("small",attrs={"class":"author"})

with open(file_csv,"w") as file:
    writer = csv.writer(file)
    writer.writerow(["Sl.No", "Author Name", "Quotes"])
    for i in range(0,len(authors)):
        writer.writerow([i+1,authors[i].text,quotes[i].text])

#This will writes only the first page at web page
'''
output  : 
1,Albert Einstein,“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
2,J.K. Rowling,"“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
3,Albert Einstein,“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
4,Jane Austen,"“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”"
5,Marilyn Monroe,"“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”"
6,Albert Einstein,“Try not to become a man of success. Rather become a man of value.”
7,André Gide,“It is better to be hated for what you are than to be loved for what you are not.”
8,Thomas A. Edison,"“I have not failed. I've just found 10,000 ways that won't work.”"
9,Eleanor Roosevelt,“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
10,Steve Martin,"“A day without sunshine is like, you know, night.”"
'''
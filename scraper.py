import requests
from bs4 import BeautifulSoup
import random
from emoji import demojize

page = requests.get("http://randomest.blogspot.com/")
soup = BeautifulSoup(page.content, 'html.parser')

headlines = soup.find_all('p')
#print(headlines)
#headline = headlines[0]
#true_headline = list(headline.children)[0]


def write_that_down():
    with open('bloggy.txt', 'w') as writer:
        for p in soup.find_all("p"):
            paragraph = p.get_text()
            paragraph = paragraph.demojize()
            writer.write(p.get_text() + "\n")

write_that_down()

#//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/div/div[2]/h3
import requests
import codecs
#import bs4
from bs4 import BeautifulSoup


def parse_table(table):
    f = codecs.open("./data/testout.html", 'w', 'utf-8')
    for tr in table.find_all('tr'):
        f.write(tr.prettify())
    f.close()

minion_page = requests.get("http://hearthstone.gamepedia.com/Minion")

soup = BeautifulSoup(minion_page.text)
for n in soup.find_all(class_="narrowonly"):
    n.decompose()
cards = soup.find(class_="cardtable")
parse_table(cards)



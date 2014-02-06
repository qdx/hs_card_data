import requests
import codecs
#import bs4
from bs4 import BeautifulSoup

minion_page = requests.get("http://hearthstone.gamepedia.com/Minion")

soup = BeautifulSoup(minion_page.text)
for n in soup.find_all(class_="narrowonly"):
    n.decompose()
cards = soup.find(class_="cardtable")
f = codecs.open("./testout.html",'w','utf-8')
f.write(cards.prettify())
f.close()


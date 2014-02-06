import requests
import codecs
#import bs4
from bs4 import BeautifulSoup

# okay, this code may looks like a giant mess, let's wrap it up:
# 1. create classes that have class variables and main entrance
# 2. classes need to be created includes CellParser, TableParser
# 3. make use of first tier functions to build instances of
#    CellParser dynamically, not sure TableParser should be done
#    in the same way

'''
Html table structure analyzed:
    Name        : td > a > TEXT
    Rarity      : td > (span > TEXT + span > TEXT)
    Subtype     : td > TEXT | td > span > TEXT
    Class       : td > (span > (img + span > TEXT) )
    Cost        : td > (TEXT + img)
    Atk         : td > (TEXT + img)
    HP          : td > (TEXT + img)
    Description : td > (b > TEXT | i > TEXT | TEXT)*
'''


#def init_cell_parser(head_list):


def get_clean_cardtable(soup):
    soup_table = soup.find(class_="cardtable")
    for n in soup.find_all(class_="narrowonly"):
        n.decompose()
    return soup_table


def parse_table_head(tr):
    table_head = []
    for th in tr.find_all('th'):
        table_head.append(th.string.strip())
        return table_head


#def parse_table_row(tr):


def parse_table(table):
    f = codecs.open("./data/testout.html", 'w', 'utf-8')
    # parse and write table head
    f.write(','.join(parse_table_head(table.tr)) + '\n')
    # delete the table head in order to keep parsing
    table.tr.decompose()
    for tr in table.find_all('tr'):
        f.write(tr.td.a.text + "\n")
        f.close()

minion_page = requests.get("http://hearthstone.gamepedia.com/Minion")
soup = BeautifulSoup(minion_page.text)
cards = get_clean_cardtable(soup)
parse_table(cards)

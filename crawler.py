import requests
import codecs
import CellParser
from bs4 import BeautifulSoup


def get_clean_cardtable(soup):
    soup_table = soup.find(class_="cardtable")
    for n in soup.find_all(class_="narrowonly"):
        n.decompose()

    return soup_table


def parse_table_head(tr):
    return [th for th in tr.stripped_strings]


def strip_cell_parser(td):
    return " ".join([str for str in td.stripped_strings])


# discard the info content in description
def description_parser(td):
    for i in td.find_all('i'):
        i.decompose()
    return strip_cell_parser(td)


def rarity_parser(td):
    td.span.decompose()
    return td.span.text.strip()


def parse_table(table, path, parser):
    # open output file
    f = codecs.open(path, 'w', 'utf-8')
    # parse table head
    table_head = parse_table_head(table.tr)
    # write table head
    f.write('&'.join(table_head) + '\n')
    # delete the table head from the DOM tree in order to keep parsing
    table.tr.decompose()
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) != len(table_head):
            continue
        indexed_tds = zip(table_head, tds)
        row = [parser.parse_cell(i[0], i[1]) for i in indexed_tds]
        f.write('&'.join(row) + '\n')
    f.close()


def get_hs_gamepedia_parser():
    # construct the cell parser
    parser = CellParser.CellParser()
    parser.add_cell_parser('Name', strip_cell_parser)
    parser.add_cell_parser('Rarity', rarity_parser)
    parser.add_cell_parser('Subtype', strip_cell_parser)
    parser.add_cell_parser('Class', strip_cell_parser)
    parser.add_cell_parser('Cost', strip_cell_parser)
    parser.add_cell_parser('Atk', strip_cell_parser)
    parser.add_cell_parser('HP', strip_cell_parser)
    parser.add_cell_parser('Description', description_parser)
    return parser


def fetch_parse_data(url, path, parser):
    minion_page = requests.get(url)
    soup = BeautifulSoup(minion_page.text)
    cards = get_clean_cardtable(soup)
    parse_table(cards, path, parser)


parser = get_hs_gamepedia_parser()
fetch_parse_data("http://hearthstone.gamepedia.com/Minion",
                 "./data/minions.csv", parser)
fetch_parse_data("http://hearthstone.gamepedia.com/Spell_cards",
                 "./data/spell.csv", parser)
fetch_parse_data("http://hearthstone.gamepedia.com/Equipment_cards",
                 "./data/weapon.csv", parser)

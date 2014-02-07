import codecs
from Models import *


def import_csv_to_db(path, card_type):
    db.connect()
    f = codecs.open(path, 'r', 'utf-8')
    head = f.readline().strip().split(',')
    for row in f:
        row_data = row.strip().split(',')
        data_pair = zip(head, row_data)
        card = Card()
        for i in data_pair:
            if i[0] in ['Cost', 'Atk', 'HP']:
                v = int(i[1]) if len(i[1]) != 0 else 0
                card.assign_value(i[0], v)
            else:
                card.assign_value(i[0], i[1])
        card.Type = card_type
        card.save()
        db.commit()
    db.close()


#Card.create_table()
import_csv_to_db("./data/minions.csv", "minion")
import_csv_to_db("./data/spell.csv", "spell")
import_csv_to_db("./data/weapon.csv", "weapon")

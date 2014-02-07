from peewee import *
from switch import switch
import ConfigParser

'''
Data

Table Card:
    Name        : String
    Rarity      : Enum(None, Free, Common, Rare, Epic, Lengendary)
    Subtype     : Enum(Beast, Demon, Dragon, Murloc, Pirate, Totem, General)
    Class       : Enum(Mage, Warlock, Paladin, Rogue, Warrior, Hunter, Shaman, Druid, Priest)
    Cost        : Int
    Atk         : Int
    HP          : Int
    Description : String
    Type        : Enum(minion, spell, weapon)
'''


config = ConfigParser.RawConfigParser()
config.read('local.cfg')
db = MySQLDatabase(config.get('mysql', 'hs_db'),
                   host   = config.get('mysql', 'host'),
                   port   = config.getint('mysql', 'port'),
                   user   = config.get('mysql', 'user'),
                   passwd = config.get('mysql', 'passwd'))


class BaseModel(Model):
    class Meta:
        database = db


class Card(BaseModel):
    Name        = CharField()
    Rarity      = CharField()
    Subtype     = CharField()
    Class       = CharField()
    Cost        = IntegerField()
    Atk         = IntegerField()
    HP          = IntegerField()
    Description = CharField()
    Type        = CharField()

    def assign_value(self, name, value):
        for case in switch(name):
            if case('Name'):
                self.Name = value
                break
            if case('Rarity'):
                self.Rarity = value
                break
            if case('Subtype'):
                self.Subtype = value
                break
            if case('Class'):
                self.Class = value
                break
            if case('Cost'):
                self.Cost = value
                break
            if case('Atk'):
                self.Atk = value
                break
            if case('HP'):
                self.HP= value
                break
            if case('Description'):
                self.Description = value
                break
            if case('Type'):
                self.Type = value
                break

class TableParser:

    def __init__(self):
        self.parser = dict()
        print "init here"

    def add_cell_parser(self, name, func):
        self.parser[name] = func

    def parse_cell(self, cell, name):
        return self.parser[name](cell)

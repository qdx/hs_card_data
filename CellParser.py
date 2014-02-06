class CellParser:

    def __init__(self):
        self.parser = dict()

    def add_cell_parser(self, name, func):
        self.parser[name] = func

    def parse_cell(self, name, cell, cell_filter=None):
        if cell_filter is not None:
            return cell_filter(cell)
        else:
            return self.parser[name](cell)

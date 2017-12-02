class Table:
    tables = []
    def __init__(self, tblnumber):
        self.tblnumber = tblnumber
        self.chairs = []
        Table.tables.append(tblnumber)

    def assignSeat(self, name):
        self.chairs.append(name)

    def displayTable(self):
        return self.chairs

    def displayNumber(self):
        return self.tblnumber
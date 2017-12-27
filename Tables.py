class Table:
    tables = []

    def __init__(self, tblnumber):
        self.tblnumber = tblnumber
        self.chairs = []
        self.generation = 1
        Table.tables.append(tblnumber)

    def assignSeat(self, name):
        self.chairs.append(name)

    def displayTable(self):
        return self.chairs

    def setOffSpring(self, offspring):
        self.chairs = offspring

    def newGeneration(self,g):
        self.generation+=g

    def displayNumber(self):
        return self.tblnumber

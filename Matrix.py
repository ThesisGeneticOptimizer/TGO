import csv
class GuestPair:
    totalPair = 0
    def __init__(self, guest1, guest2, points):
        self.guest1 = guest1
        self.guest2 = guest2
        self.points = points
        GuestPair.totalPair+=1

    def getPoints(g1, g2):
        with open('relational_keys.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if((row[0]==g1 and row[1]==g2) or (row[0]==g2 and row[1]==g1)):
                    return row[2]
                    break

    def getTotal(self):
        return GuestPair.totalPairs



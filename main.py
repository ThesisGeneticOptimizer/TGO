

from Guests import Guest
from Tables import Table
from gen_al import GeneticAlgorithm
import csv

#entities
guest = []
table = []

#reads csv, eliminate duplicates
with open('relational_keys.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    lastR = ""
    tempG = []
    for row in readCSV:
        if(len(tempG)==0):
            tempG.append(row[0])
            guest.append(Guest(row[0]))
        else:
            if (row[0] in tempG):
                pass
            else:
                tempG.append(row[0])
                guest.append(Guest(row[0]))
        lastR = row[1]
    tempG.append(lastR)
    guest.append(Guest(lastR))

#train two tables(sample)
table.append(Table("1"))
table.append(Table("2"))

#GENETIC ALGORITHM GOES HERE
GeneticAlgorithm.initialization(guest,table)
GeneticAlgorithm.evaluation(table,1,0)
GeneticAlgorithm.crossover(table,0)
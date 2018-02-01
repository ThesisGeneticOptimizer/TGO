import csv
from Guests import Guest
import RGA

#Variables
filename = "guest41"
closenessKeys = [9,7,5,3,2,1,0]
guest = []
listGuest = []
fitness = []

#Reads the name of the guest
with open(filename+".csv") as csvfile:
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

for name in guest:
    #print(name.displayName())
    listGuest.append(name.displayName())

#Getting their fitness values
with open(filename+".csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x = 0
    for row in readCSV:
        fitness.append([])
        fitness[x].append(row[0])
        fitness[x].append(row[1])
        fitness[x].append(row[2])
        x = x + 1

#GeneticAlgorithm
RGA.Knapsack(listGuest)
RGA.Initalization(listGuest,fitness,filename,closenessKeys)
RGA.Filterization()

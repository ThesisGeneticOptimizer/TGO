import itertools
from time import gmtime, strftime
from tqdm import tqdm
from Guests import Guest
import math
import csv

guest = []
listGuest = []
fitness = []
countCrossover = 0
crossoverMutate = []
crossCount = 0
#Reads the name of the guest
with open('fitnesss.csv') as csvfile:
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

for g in guest:
    print(g.displayName())
    listGuest.append(g.displayName())

#Generate the possible crossovers
#letters = ["a","b","c","d","e"]
print("The total number of guest is ", len(listGuest))
numGuest = input("How many guest per table:")
startTime = strftime("%H:%M:%S", gmtime())
crossoverCombination = list(itertools.combinations(listGuest, int(numGuest)))
numTable = len(listGuest) / int(numGuest)
result = math.ceil(numTable)
print("\nThe guest per table is", numGuest ,".")
print("The total number of table is ", result ,".")
#print("The total number of crossovers is", len(crossoverCombination))
##for i in crossoverCombination:
##    print(i)


#Getting their fitness values
with open('fitnesss.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x = 0
    for row in readCSV:
        fitness.append([])
        fitness[x].append(row[0])
        fitness[x].append(row[1])
        fitness[x].append(row[2])
        x = x + 1
#for h in fitness:
   # print(h)

   
#Calculates the mutation per crossovers
crossoverMutate.append([])
for load in tqdm(range(len(crossoverCombination))):
    crossoverMutation = list(itertools.permutations(crossoverCombination[load]))
    count = 1
    maximum = 0
    mute = 0
    highestSet = []
    highestTotals = []

    #Getting the all possible set(5! = 120(Mutation))
    for x in crossoverMutation:
        pair = []
        mutate = x
        mutation = []
        mutationPair = []
        counting = 0
        total = 0
        check = True
        highestTotal = []

        #Getting the first 5 set posible pair
        for y in range(len(mutate)):
            pair.append([])
            first = y + len(mutate) - 1
            if first > len(mutate)-1:
                first = first - (len(mutate))
            second = y
            pair[y].append(mutate[first])
            pair[y].append(mutate[second])
        #Getting the second 5 set posible pair
        for e in range(len(mutate)):
            pair.append([])
            focus = e - 1
            if focus < 0:
                focus = len(mutate)-1
            first = focus - 1
            if first < 0:
                first = len(mutate) - 1
            second = focus + 1
            if second > len(mutate)-1:
                second = 0
            pair[len(mutate) + e].append(mutate[first])
            pair[len(mutate) + e].append(mutate[second])

        #Getting its Fitness Value of the pair
        for a in range(len(pair)):
            for b in range(len(fitness)):
                if pair[a][0] == fitness[b][0] and pair[a][1] == fitness[b][1]:
                    mutation.append(fitness[b][2])
                if pair[a][0] == fitness[b][1] and pair[a][1] == fitness[b][0]:
                    mutation.append(fitness[b][2])
                    
        #Calculating the first pair like (1+2)-(3+4)+(5+6)-(7+8)
        for c in range(int(len(mutation)/2)):
            first = mutation[c + counting]
            counting = counting+1
            second = mutation[c + counting]
            highestTotal.append(first)
            highestTotal.append(second)
            mutationPair.append(int(first) + int(second))

        #Calculating the whole Fitness Value like 3 - 7 + 11 - 15
        for d in range(len(mutationPair)):
            if check:
                total = total + mutationPair[d]
                check = False
            else:
                total = total - mutationPair[d]
                check = True
                
        #print("Mutation", count," : ",pair, " Fitness : ", total)
        if maximum < total:
            maximum = total
            mute = count
            highestSet = pair
            highestTotals = highestTotal
            
        count = count+1
    num = 0
    for n in highestSet:
        if num < int(numGuest):
            crossoverMutate[crossCount].append(n[0])
        else:
            break
        #print(n[0],"-",n[1]," => ",highestTotals[num])
        num = num + 1
    crossoverMutate[crossCount].append(maximum)
    crossoverMutate.append([])
    crossCount = crossCount + 1

print("Time Start:", startTime)
print("Time End:", strftime("%H:%M:%S", gmtime()))

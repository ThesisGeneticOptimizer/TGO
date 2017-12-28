import itertools
import csv

fitness = []
with open('fitness.csv') as csvfile:
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

arr = list(itertools.permutations(["David Brownlee","Deborah Dean","Gene Otsea","Dan Lyford","Debbie Brownlee"]))
count = 1
maximum = 0
mute = 0
highestSet = []
highestTotals = []

for x in arr:
    pair = []
    mutate = x
    mutation = []
    mutationPair = []
    counting = 0
    total = 0
    check = True
    highestTotal = []
    
    
    
    for y in range(len(mutate)):
        pair.append([])
        first = y + len(mutate) - 1
        if first > len(mutate)-1:
            first = first - (len(mutate))
        second = y
        pair[y].append(mutate[first])
        pair[y].append(mutate[second])
        
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
        
    for a in range(len(pair)):
        for b in range(len(fitness)):
            if pair[a][0] == fitness[b][0] and pair[a][1] == fitness[b][1]:
                mutation.append(fitness[b][2])
            if pair[a][0] == fitness[b][1] and pair[a][1] == fitness[b][0]:
                mutation.append(fitness[b][2])
    for c in range(int(len(mutation)/2)):
        first = mutation[c + counting]
        counting = counting+1
        second = mutation[c + counting]
        highestTotal.append(first)
        highestTotal.append(second)
        mutationPair.append(int(first) + int(second))
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
print("Maximum : ",maximum)
print("Mutation : ",mute)
num = 0
for n in highestSet:
    print(n[0],"-",n[1]," => ",highestTotals[num])
    num = num + 1

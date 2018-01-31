#Libraries, Modules
import itertools
import click
import math
import csv
from tqdm import tqdm
from time import gmtime, strftime

#Variables
mutate = []
iteration = 0
startTime = 0
maximum = 10000
filename = ''

def GetFilename(name):
    global filename
    filename = name

def initialization(guest,fitness):
    global mutate,startTime
    print("The total number of guest is ", len(guest))
    numGuest = input("How many guest per table:")
    startTime = strftime("%H:%M:%S", gmtime())
    crossover(guest,numGuest,fitness)
    mutate.sort(key=lambda x: x[int(numGuest)], reverse=True)
    for value in range(len(mutate)):
        mutate[value] = mutate[value][:-1]
    selection(guest,numGuest,mutate)

def evaluation(guestCrossover,mutate,total):
    global iteration
    for name in guestCrossover:
        mutate[iteration].append(name)
    mutate[iteration].append(total)
    iteration = iteration + 1

def crossover(guest,numGuest,fitness):
    crossoverCombination = list(itertools.combinations(guest, int(numGuest)))
    numberOfArray = len(crossoverCombination)/maximum
    results = math.ceil(numberOfArray)
    iteration = 0
    listArray = []
    check = False
    for count in range(results):
        if check:
            break
        listArr = []
        listArray.append(listArr)      
        for i in range(maximum):
            if iteration == len(crossoverCombination):
                check = True
                break
            listArr.append(crossoverCombination[iteration])
            iteration = iteration + 1
    numTable = len(guest) / int(numGuest)
    result = math.ceil(numTable)
    print("\nThe guest per table is", numGuest ,".")
    print("The total number of table is ", result ,".")
    print("The total generation generated :",len(listArray))
    increment = 0
    for nex in range(len(listArray)):
        print("Generation", nex + 1 , "\b")
        for combination in tqdm(listArray[nex]):
            mutation(combination,fitness)

def mutation(guestCrossover,fitness):
    global mutate
    mutationCombination = list(itertools.combinations(guestCrossover,2))
    total = 0
    mutate.append([])
    for count in range(len(mutationCombination)):
        for fit in range(len(fitness)):
            if mutationCombination[count][0] == fitness[fit][0] and mutationCombination[count][1] == fitness[fit][1]:
                total = total + int(fitness[fit][2])
            if mutationCombination[count][0] == fitness[fit][1] and mutationCombination[count][1] == fitness[fit][0]:
                total = total + int(fitness[fit][2])
    evaluation(guestCrossover,mutate,total)

def selection(checkListGuest,numGuest,mutate):
    stopper = True
    counter = 0
    tableCount = 0
    tabled = []
    while stopper:
        if len(checkListGuest) >=  int(numGuest):
            if int(counter) == len(mutate):
                stopper = False
            if not tabled:
                tabled.append(mutate[counter])
                for a in tabled[tableCount]:
                    checkListGuest.remove(a)
                counter = counter + 1
                tableCount = tableCount + 1
            else:
                tempCount = 0
                for b in mutate[counter]:
                    if b in checkListGuest:
                        tempCount = tempCount + 1
                if int(tempCount) == int(numGuest):
                    tabled.append(mutate[counter])
                    for c in tabled[tableCount]:
                        checkListGuest.remove(c)
                    tableCount = tableCount + 1
                counter = counter + 1
                
        else:
            tempArr = []
            for d in range(int(numGuest)):
                if len(checkListGuest) != 0:
                    tempArr.append(checkListGuest[0])
                    checkListGuest.remove(checkListGuest[0])
                else:
                    tempArr.append("Vacant Seat")
            tabled.append(tempArr)
        if len(checkListGuest) == 0:
            stopper = False
    display(tabled)
def display(tabled):
    global filename
    optimize = []
    tableNum = 1
    index = 0
    for z in tabled:
        optimize.append([])
        tableName = "Table " + str(tableNum)
        optimize[index].append(tableName)
        print(tableName,":")
        for x in z:
            optimize[index].append(x)
            print("\t",x)
        index = index + 1
        tableNum = tableNum + 1
    myFile = open("Optimized/"+filename+"_Optimized.csv", 'w')  
    with myFile:  
       writer = csv.writer(myFile)
       for item in optimize:
           writer.writerow(item)
    print("Optimized!!!")
    print("Time Start:", startTime)
    print("Time End:", strftime("%H:%M:%S", gmtime()))
    
        
    

#Library/Module
import random
import itertools

#Variables
listGuest = []
fitness = []
filename = ""
closenessKeys = []
arrGuest = []
arrayState = []
state = 0

def Knapsack(listGuest):
    global arrGuest
    numGuest = len(listGuest)    
    values = [6,5]
    total = 0
    running = True
    while running:
        ran = random.randint(0,len(values)-1)   
        if total <= int(numGuest):
            arrGuest.append(values[ran])
            total = total + int(values[ran])
        else:
            total = 0
            arrGuest = []
        if total == int(numGuest):
            running = False
    arrGuest.sort()
    print(arrGuest)
    
def Initalization(lists,fit,file,keys):
    global listGuest,fitness,filename,closenessKeys
    listGuest = lists
    fitness = fit
    filename = file
    closenessKeys = keys

def Filterization():
    #pairing = list(itertools.combinations(arrayState,2))
    global fitness,arrayState,state,closenessKeys
    for b in fitness:
        if int(b[2]) == int(closenessKeys[state]):
            arrayState.append(b[0])
            arrayState.append(b[1])
    pairing = list(itertools.combinations(arrayState,2))
    arrayState = []
    for c in range(len(pairing)):
        for d in range(len(fitness)):
            if pairing[c][0] == fitness[d][0] and pairing[c][1] == fitness[d][1]:
                arrayState.append(list(pairing[c]))
                arrayState[c].append(fitness[d][2])
            if pairing[c][0] == fitness[d][1] and pairing[c][1] == fitness[d][0]:
                arrayState.append(list(pairing[c]))
                arrayState[c].append(fitness[d][2])
    for e in arrayState:
        print(e)
    
    
    

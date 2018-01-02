import random
import time

arr = ["a","b","c","d","e","f","g","h","i","j"]
numberGuest = len(arr)
numberOfGeneration = int(((numberGuest-1)*numberGuest)/2)

print("Number of Guest :",numberGuest)
print("Number of Generations :",numberOfGeneration,"\n")
textSuggest = "Suggested Number of Table : "
tempNumberGuest = numberGuest
for q in range(0, len(arr)):
    if numberGuest%tempNumberGuest == 0:       
        textSuggest = textSuggest + str(tempNumberGuest) + " "
    tempNumberGuest = tempNumberGuest - 1
print(textSuggest)
numberTable = input("Enter number of Table :")
numberOfGuest = int(int(numberGuest)/int(numberTable))
print(numberOfGuest,"Guest per table")

numberTable = numberOfGuest
count = 1
lenghtCounter = 0
switch = True
setGen = []
generation = []
trigger = 0
available = 0
found = False

tempArr = []     
generation.append([])
tempArr2 = random.sample(range(0,(numberGuest)), int(numberTable))
for x in range(int(numberTable)):
    tempArr.append(arr[tempArr2[x]])
for w in range(int(numberTable)):
    generation[0].append(tempArr[w])
generation.append([])

while count < numberOfGeneration: #Number of Generation
    
    tempArr2 = random.sample(range(0,(numberGuest)), int(numberTable))
    while switch: #Save the new set of generation
        for y in range(len(generation)):#Number of 2 dimensional array
            if found:
                tempArr2 = random.sample(range(0,(numberGuest)), int(numberTable))
                found = False
                break
            lenghtCounter = 0
            tempArr = []
            for x in range(int(numberTable)):#Random Set
                tempArr.append(arr[tempArr2[x]])
            setGen = generation[y]
            if not setGen:
                pass
            else:
                for z in range(int(numberTable)):#check if array exist
                    if tempArr[z] not in setGen:
                        lenghtCounter = lenghtCounter + 1
                if lenghtCounter > 0:
                    trigger = 1
                if lenghtCounter == 0:
                    trigger = 0
                    found = True
                    break
        if trigger == 1:
            switch = False
            generation.append([])    
            for w in range(int(numberTable)):
                generation[count].append(tempArr[w])
            count = count + 1
    switch = True
num = 0
for a in generation:
    print(a," : ",num)
    num = num + 1        

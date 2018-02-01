import random


numGuest = input("How many guest : ")
arrGuest = []
values = []
total = 0
running = True
check = True
print("Type '0' to end")
while check:
    inp = input("Input : ")
    if inp != "0":
        values.append(inp)
    else:
        check = False
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

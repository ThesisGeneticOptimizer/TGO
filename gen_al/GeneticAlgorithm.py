import random
import re
from Matrix import GuestPair

parents = []
offsprings = []
def initialization(guest, table):
    print("====INITIALIZATION====\nRandom seating assignments")
    for t in range(0,len(table)):
        print("Table %s:" %(table[t].displayNumber()))
        for i in range(0,5):
            try:
                g = random.choice(guest)
                print("==Chair %d: %s " % (i + 1, g.displayName()))
                table[t].assignSeat(g.displayName())
                guest.remove(g)
            except:
                pass

def evaluation(table, nexts, keys):
    print("\n\n====EVALUATION====")
   
    for t in range(0, len(table)):
        print("Table",(t+1))
        for i in range(0, len(table[t].chairs)-1):
            for j in range(nexts, len(table[t].chairs)):
                print("-> ",table[t].chairs[i],"-",table[t].chairs[j]," = ",GuestPair.getPoints(table[t].chairs[i],table[t].chairs[j]))
                keys+=str((GuestPair.getPoints(table[t].chairs[i],table[t].chairs[j])))
            nexts+=1
        nexts = 1
        calculateFitness(keys,0,0,[],0,["-","+"])
        keys = ""

def crossover(table,i):
    print("\n\n====CROSSOVER====")
    while i < len(table):
        print("-> selected parents:",table[i].chairs,table[i+1].chairs)
        offSpring1 = table[i].chairs[:int(len(table[i].chairs)/2)+1] + table[i+1].chairs[int(len(table[i].chairs)/2)+1:]
        offSpring2 = table[i].chairs[int(len(table[i].chairs) / 2)+1:] + table[i + 1].chairs[:int(len(table[i].chairs)/2)+1]
        table[i].setOffSpring(offSpring1)
        table[i+1].setOffSpring(offSpring2)
        print("= produced offspring",offSpring1,offSpring2)
        i+=2
    evaluation(table,1,"")
    mutation(table,offSpring1,offSpring2)

def mutation(table,offSpring1,offSpring2):
    print("\n\n===MUTATION===")
    x = random.randint(0,len(offSpring1)-1)
    y = random.randint(0,len(offSpring1)-1)
    offSpring1[x],offSpring1[y] = offSpring1[y] , offSpring1[x]

    x = random.randint(0,len(offSpring2)-1)
    y = random.randint(0,len(offSpring2)-1)
    offSpring2[x],offSpring2[y] = offSpring2[y] , offSpring2[x]

    
    print(offSpring1)
    print(offSpring2)
     
    table[0].setOffSpring(offSpring1)
    table[1].setOffSpring(offSpring2)

    evaluation(table,1,"")
    
def calculateFitness(keys,i,s,temp,final,operator):
    try:    
        if(len(keys)%2==1):
            keys+="0"
        while i < len(keys):
            temp.append(int(keys[i]) + int(keys[i+1]))
            i+=2

        print(temp,keys)
        final+=int(temp[0]);
        for j in range(1, len(temp)):
            if(s==0):
                final-=int(temp[j])
                s = 1
            else:
                final+=int(temp[j])
                s = 0
        
        print(str(final))
    except Exception as e:
        print(e)
    

import random
from Matrix import GuestPair

parents = []
offsprings = []

optimal = []

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

def evaluation(table, next, keys):
    try:
        print("\n\n====EVALUATION====")
        for t in range(0, len(table)):
            print("Table",(t+1),"("+str(table[t].generation)+")")
            for i in range(0, len(table[t].chairs)-1):
                for j in range(next, len(table[t].chairs)):
                    print("-> ",table[t].chairs[i],"-",table[t].chairs[j]," = ",GuestPair.getPoints(table[t].chairs[i],table[t].chairs[j]))
                    keys+=str(GuestPair.getPoints(table[t].chairs[i], table[t].chairs[j]))
                next+=1
            next = 1
            calculateFitness(keys,0,0,[],0)
            keys = ""
    except:
        pass

def crossover(table,i):
    try:
        print("\n\n====CROSSOVER====")
        while i < len(table):
            print("-> selected parents:",table[i].chairs, table[i+1].chairs)
            offSpring1 = table[i].chairs[:int(len(table[i].chairs)/2)+1] + table[i+1].chairs[int(len(table[i].chairs)/2)+1:]
            offSpring2 = table[i].chairs[int(len(table[i].chairs) / 2)+1:] + table[i+1].chairs[:int(len(table[i].chairs)/2)+1]
            table[i].setOffSpring(offSpring1)
            table[i+1].setOffSpring(offSpring2)
            print("= produced offspring",offSpring1,offSpring2)
            i+=2
        evaluation(table,1,"")
    except:
        pass


def calculateFitness(keys, i, s, temp, final):
    try:
        if (len(keys) % 2 == 1):
            keys += "0"
        while i < len(keys):
            temp.append(int(keys[i]) + int(keys[i + 1]))
            i += 2

        print(temp, keys)
        final += int(temp[0])
        for j in range(1, len(temp)):
            if (s == 0):
                final -= int(temp[j])
                s = 1
            else:
                final += int(temp[j])
                s = 0
        print(str(final))
    except Exception as e:
        print(e)

def shuffled(x):
    y = x[:]
    random.shuffle(y)
    return y


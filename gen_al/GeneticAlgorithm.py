import random
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

def evaluation(table, next, fitness):
    print("\n\n====EVALUATION====")
    global parents
    for t in range(0, len(table)):
        print("Table",(t+1))
        for i in range(0, len(table[t].chairs)-1):
            for j in range(next, len(table[t].chairs)):
                print("-> ",table[t].chairs[i],"-",table[t].chairs[j]," = ",GuestPair.getPoints(table[t].chairs[i],table[t].chairs[j]))
                fitness+=int(GuestPair.getPoints(table[t].chairs[i],table[t].chairs[j]))
            next+=1
        next = 1
        parents.append(fitness)
        fitness = 0
    print("FITNESS",parents)

def crossover(table,i,next,fitness):
    print("\n\n===CROSSOVER===")
    while i < len(table):
        print("-> selected parents:",table[i].chairs,table[i+1].chairs)
        offSpring1 = table[i].chairs[:int(len(table[i].chairs)/2)+1] + table[i+1].chairs[int(len(table[i].chairs)/2)+1:]
        offSpring2 = table[i].chairs[int(len(table[i].chairs) / 2) + 1:] + table[i + 1].chairs[:int(len(table[i].chairs)/2)+1]
        print("= produced offspring",offSpring1,offSpring2)
        i+=2

    for t in range(0, len(table)):
        for i in range(0, len(table[t].chairs)-1):
            for j in range(next, len(table[t].chairs)):
                #print(table[0].chairs[:int(len(table[0].chairs)/2)+1]+table[1].chairs[int(len(table[1].chairs)/2)+1:])
                #print(table[0].chairs[int(len(table[0].chairs)/2)+1:]+table[1].chairs[:int(len(table[1].chairs)/2)+1])
                #DI KO SURE DIRI
                fitness += int(GuestPair.getPoints(table[0].chairs[i],table[1].chairs[j]))
            next+=1
        next = 1
        offsprings.append(fitness)
        fitness = 0
    print("FITNESS",offsprings)

    mutation(offSpring1) #si offspring1 pa lang ako ge test
    
def mutation(offSpring1):
    #exchange mutation : choosing two genes at random and swap them
    print("\n\n===MUTATION===")
    x = random.randint(0,len(offSpring1)-1)
    y = random.randint(0,len(offSpring1)-1)
    offSpring1[x],offSpring1[y] = offSpring1[y] , offSpring1[x]
    print(offSpring1)
            
   

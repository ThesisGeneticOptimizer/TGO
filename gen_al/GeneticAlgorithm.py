import random

def initialization(guest, table):
    for t in range(0,len(table)):
        print("Table %s:" %(table[t].displayNumber()))
        for i in range(0,6):
            try:
                g = random.choice(guest)
                print("==Chair %d: %s " % (i + 1, g.displayName()))
                table[t].assignSeat(g.displayName())
                guest.remove(g)
            except:
                print()


def evaluation(guest, table):
    print("Coming...")

def crossover(guest, table):
    print("Coming...")

def mutation(guest, table):
    print("Coming...")
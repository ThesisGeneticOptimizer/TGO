import csv

with open('Relationship.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    list_of_list = []
    list_of_name = []
    
    line1 = next(spamreader)
    first = line1[0]
    list_ = [line1[2]]
    
    for line in spamreader:
        list_of_name.append(line[0])
        while(line[0] == first):
            list_.append(line[2])
            try:
                line = next(spamreader)
            except :
                break;
        list_of_list.append(list(map(int,list_)))
        list_ = [line[2]]
        first = line[0]
        

maxlen1 = len(max(list_of_name))
print("\t"+"\t".join([str(list_of_name[el]) for el in range(0,maxlen1)])+"\n")
for i in range(len(list_of_list)):
    print(str(list_of_name[i])+"\t"+"\t".join([str(el) for el in list_of_list[i]])+"\n")
    
print (maxlen1)

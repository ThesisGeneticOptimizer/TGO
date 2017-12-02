def ask_input():
    hm_table = input("How many table?")
    hm_guest_table = input("How many guest per table?")

    total_guest = int(hm_table)*int(hm_guest_table)
    print ('Total guest :' ,total_guest)
    ask_for_guest(total_guest)
    
def ask_for_guest(hm):
    list_of_guest = []
    
    for i in range (hm):
        print (i+1,"guest name :")
        add_to_list =  input()
        list_of_guest.append(add_to_list)


    print (list_of_guest)
    ask_for_relationship(list_of_guest)
    
def ask_for_relationship(lg):
    o_csv = open("Relationship.csv","w")
    lg_len = len(lg)
    j = 0
    k = 1
    while j != lg_len:
        for i in range (lg_len-k):
            print ("Relationship between",lg[j],"and",lg[i+k],":")
            rel = input()
            print (j,i+k)
            merge = lg[j],lg[i+k],rel
            conv = str(merge)
            b = "()'"
            for char in b:
                conv = conv.replace(char,"")
                        
            o_csv.write(conv)
            o_csv.write('\n')
            
        k = k+1
        j = j+1
    o_csv.close()
        
        
ask_input()

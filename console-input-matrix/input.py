import csv
import openpyxl

def ask_input():
    hm_table = input("How many table?")
    hm_guest_table = input("How many guest per table?")

    total_guest = int(hm_table)*int(hm_guest_table)
    print ('Total guest :' ,total_guest)
    ask_for_guest(total_guest)
    
def ask_for_guest(hm):
    o_csv = openpyxl.load_workbook('Relationship.xlsx',read_only=False, keep_vba= True)
    sheetname = o_csv.get_sheet_by_name('Sheet1')

    for i in range (hm):
        print (i+1,"guest name :")
        add_to_list =  input()
        sheetname.cell(row=1,column=i+2).value = add_to_list
        sheetname.cell(row=i+2,column=1).value = add_to_list

    for i in range (1,hm+1):
        for j in range (2,hm+1):
            row = sheetname.cell(row=i+1,column=1).value
            col = sheetname.cell(row=1,column=j+1).value
            if i+1 != j+1 and sheetname.cell(row=j+1,column=i+1).value is None:
                print ("Relationship between",row,"and",col,":")
                rel = input()

                merge = int(rel)

                sheetname.cell(row=i+1,column=j+1).value = merge
                sheetname.cell(row=j+1,column=i+1).value = merge
               
    o_csv.save('Matrix_Relationship.xlsm')

       
ask_input()

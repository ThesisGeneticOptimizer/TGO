import tkinter
import csv
from tkinter import filedialog
from tkinter import *

root = tkinter.Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
root.geometry("1000x1000")

Can1 = tkinter.Canvas(root, bg="Gray")
Can1.grid(row=0, column=0)

vsbar = tkinter.Scrollbar(root, orient="vertical", command=Can1.yview)
vsbar.grid(row=0, column=1, sticky=N+S+E+W)
Can1.configure(yscrollcommand=vsbar.set)

hsbar = tkinter.Scrollbar(root, orient="horizontal", command=Can1.xview)
hsbar.grid(row=1, column=0, sticky=N+S+E+W)
Can1.configure(xscrollcommand=hsbar.set)

frame_buttons = tkinter.Frame(Can1, bg="Gray", bd=2, relief=tkinter.GROOVE)
Can1.create_window((0,0), window=frame_buttons,anchor='nw')

def resize(event):
    Can1.configure(scrollregion=Can1.bbox("all"), width=980, height=690)
frame_buttons.bind("<Configure>", resize)

def display_matrix(fname):
    with open(fname,newline="") as file:
       reader = csv.reader(file)

       
       r = 0
       for col in reader:
          c = 0
          for row in col:
        
             label = tkinter.Label(frame_buttons, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)
             if row == "":
                label.config(bg="gray")
             label.grid(row = r, column = c,sticky='news')
             c += 1
          r += 1
      
def browse_file():
    fname = filedialog.askopenfilename(filetypes = (("All files", "*.type"), ("All files", "*")))
    print (fname)
    display_matrix(fname)


filemenu.add_command(label = "Open", command = browse_file)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)



#broButton = tkinter.Button(master = root, text = 'Browse', width = 6, command=browse_file)
#broButton.grid(column=0,row=0)


root.config(menu = menubar)
root.mainloop()

import tkinter
import csv
from tkinter import filedialog
from tkinter import *

root = tkinter.Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)

def display_matrix(fname):
    with open(fname,newline="") as file:
       reader = csv.reader(file)

       
       r = 0
       for col in reader:
          c = 0
          for row in col:
        
             label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)
             if row == "":
                label.config(bg="gray")
             label.grid(row = r, column = c)
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

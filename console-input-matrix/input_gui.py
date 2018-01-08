import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import pandas as pd


class MyWindow:

    def __init__(self, parent):

        self.parent = parent

        self.filename = None
        self.df = None

        self.text = tk.Text(self.parent)
        self.text.pack()

        self.button = tk.Button(self.parent, text='LOAD DATA', command=self.load)
        self.button.pack()

    def load(self):

        name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx','*.xlsm'))])

        if name:
            if name.endswith('.csv'):
                self.df = pd.read_csv(name)
            else:
                self.df = pd.read_excel(name)

            self.filename = name

        if self.df is None:
            self.load()

        if self.df is not None:
            self.text.insert('end', self.filename + '\n')
            self.text.insert('end', str(self.df.head()) + '\n')


if __name__ == '__main__':
    root = tk.Tk()
    top = MyWindow(root)
    root.mainloop()

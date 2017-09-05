from tkinter import *
import tkinter as tk

import select_main
import select_func

def load_gui(self):

    self.srcBut = tk.Button(self.master, text = "Source directory", fg = 'black', command = lambda: select_func.srcDir(self))
    self.srcBut.grid(row = 0, column = 1, sticky = N+E+W+S)

    self.destBut = tk.Button(self.master, text = "Destination Directory", fg = 'black', command = lambda: select_func.destDir(self))
    self.destBut.grid(row = 2, column = 1, sticky = N+E+W+S)

    self.executeBut = tk.Button(self.master, text = "Execute", fg = 'black', command = lambda: select_func.execute(self))
    self.executeBut.grid(row = 4, column = 1, sticky = N+E+W+S)


    self.slbl = tk.Label(self.master, text = "Source:  ", bg = "#E1CEC1", fg = "black")
    self.slbl.grid(row = 0, column = 0, sticky = W)
    self.dlbl = tk.Label(self.master, text = "Destination:  ", bg = "#E1CEC1 ", fg = "black")
    self.dlbl.grid(row = 2, column = 0, sticky = W)
    self.elbl = tk.Label(self.master, text = "Execute:  ", bg = "#E1CEC1", fg = "black")
    self.elbl.grid(row = 4, column = 0, sticky = W)

    self.lab_lastchk = tk.Label(self.master, text="Last Check:")
    self.lab_lastchk.grid(row=6,column=2)

    select_func.create_db(self)
    
if __name__ == "__main__":
    pass

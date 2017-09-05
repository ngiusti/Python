from tkinter import *
import tkinter as tk
import time
import select_gui
import select_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        
        self.master = master
        self.master.resizable(width=True , height=False)
        self.master.title("File selector for transfer")
        self.master.configure(bg = "#E1CEC1")
        
        select_gui.load_gui(self)

if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

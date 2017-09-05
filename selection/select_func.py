import tkinter
from tkinter import filedialog
from tkinter import *
import checkmod
import os
import time
import shutil
import sqlite3

#global variables
source_path = []
destination_path = []
#display messages on the buttons
srcText ='Select Source Directory'
destText = 'Select Destination Directory'
executeText = "Files Transfered"

#the source point for the files to be moved.
def srcDir(self):
    srcName = filedialog.askdirectory()
    self.srcBut["text"]= str(srcName) if srcName else srcText
    source = srcName + "/"
    source_path.append(source)
    print (source)
    
#the destination point for the files to be moved.
def destDir(self):
    destName = filedialog.askdirectory()
    self.destBut["text"] = str(destName) if destName else destText
    destination = destName + "/"
    destination_path.append(destination)
    print (destination)
    
#The execute action for the file transfer
def execute(self):
    checkMod(self)
    print (time.ctime())
    self.executeBut["text"] = str(executeText) if execute else executeText
    

#The function for checking the time since the files have been
#edited/created then moving them.
def checkMod(self):
    
    source = source_path[0]
    dest = destination_path[0]  
    past = (time.time() - 24*60*60)
    files = os.listdir(source)
    for i in files:
        if time.ctime(os.path.getmtime(source + i)) >= time.ctime(past): # added + i to identify the folder. 
            shutil.move(source + i, dest)
            print ("Files have been transfered")
        else:
            print ("Not a new file")

def create_db(self):
    conn = sqlite3.connect('select.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_select( Unix, REAL, Datestamp TEXT);")
        cur.execute("INSERT INTO Select VALUES (?,?)",(self.unix,self.datestamp))
        cur.execute("SELECT MAX(Datestamp) FROM select")
        self.last_datestamp = c.fetchone()
        
        conn.commit()
    conn.close()

def first_timestamp(self):
    try:
        conn = sqlite3.connect('select.db')
        cur = conn.cursor()
        cur.execute("SELECT MAX(Datestamp) FROM select.db")
        self.last_datestamp = cur.fetchone()
        conn.commit()
        conn.close()
        update_ent_lastchk(self)
    except:
        self.ent_lastchk.state(['readonly'])



    
            
if __name__ == "__main__":
    pass

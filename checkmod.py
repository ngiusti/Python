import os
import time
import datetime
import shutil








def moveFiles():
    past = (time.time() - 24*60*60)# this is stating the 24 hour period 
    source = 'C:/Users/Nicholas/Desktop/1/'
    dest = 'C:/Users/Nicholas/Desktop/2/'
    files = os.listdir(source)
    for i in files:
        if time.ctime(os.path.getmtime(source + i)) >= time.ctime(past):
            print (time.ctime(os.path.getmtime(source)))
            print (time.ctime(past))
            shutil.move(source + i, dest)
            print ("Files have been transfered")
        else:
            print ("Nothing New")
            print (time.ctime(os.path.getmtime(source)))
            print (time.ctime(past))


moveFiles()

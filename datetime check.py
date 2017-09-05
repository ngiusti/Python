import time
import datetime

x = datetime.datetime.now()

def openClosed(x):
    if (9 <= x.hour < 21):
        print("This branch is open")
    else:
        print ("This branch is closed")





portlandTime = datetime.datetime.now()
print 'Portland :', portlandTime
openClosed(portlandTime)

newYorkTime = datetime.datetime.now() + datetime.timedelta(hours=3)
print 'New York: ', newYorkTime
openClosed(newYorkTime)

londonTime = datetime.datetime.now() + datetime.timedelta(hours=8)
print 'London: ', londonTime
openClosed(londonTime)


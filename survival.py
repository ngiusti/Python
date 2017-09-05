def start(days=0,train=0,food=3,name=""):
    name = game(name)
    days,train,food,name = survival(days,train,food,name)

def game(name):
    if name != "": 
        print ("\n Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print ("\nYou ready to try and survive {}?!".format(name))
                    print("\nYou will be tested, and we shall see how long you will last")
                    stop = False
    return name

def survival(days,train,food,name):
    stop = True
    while stop:
        showStats(days,train,food,name)
        pick = raw_input("\nWhat will you do? Train, look for food, or risk everything and fight your way out? T/L/F").lower()
        if pick == "t":
            print("You trained for the day, hope you have food to keep going...")
            train = (train + 1)
            food = (food - 1)
            days = (days + 1)
            stop = False
        if pick == "l":
            print("You found a few scraps to eat should last you a day or two...")
            food = (food + 2)
            days = (days + 1)
            stop = False
        if train >= 4:
            print ("Ready to fight")
        if pick == "f":
            fightYourWayOut
            stop = False
        
            
        stats(days,train,food,name)

def showStats(days,train,food,name):
    print ("\n {} You have been here {} days, You have {} days worth of food and you have trained for {} days.".format(name,days,food,train))
    print ("\n Do you think you are ready to fight your way out?")

def stats(days,train,food,name):
    if food < 0:
        died(days,train,food,name)
    if days > 7:
        died2(days,train,food,name)
    if train > 5:
        print ("are you ready for the fight?")
        def  fightYourWayOut (days,train,food,name):
            badGuy = 3
            pick2 = raw_input("\n time to fight! Punch or kick? p\k").lower()
            if pick2 == 'p':
                train = (train - 1)
                badGuy = (badGuy - 1)
            if pick2 == 'k':
                train = (train - 1)
                badGuy = (badGuy - 1)
            survive(days,train,food,name,badGuy)
        
    else:
        survival(days,train,food,name)

def died (days,train,food,name):
    print ("\n You have died, you ran out of food and starved")
    again(days,train,food,name)

    
def died2 (days,train,food,name):
    print ("\n You stayed to long and got killed...")
    again(days,train,food,name)



def survive(days,train,food,name,badGuy):
    if badGuy <= 0:
        gotAway(days,train,food,name)
    if train <= 0:
        died3(days,train,food,name)

def died3(days,train,food,name):
    print ("\nYou died")
    again(days,train,food,name)
    
def gotAway(train,name):
    print ("\nYou escaped good job!")
    again(days,train,food,name)
    
def again(days,train,food,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(days,train,food,name)
        if choice == "n":
            print("\nGoodbye")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'Yes', pr 'n' for 'No' ")

def reset(days,train,food,name):
    days = 0
    train = 0
    food = 3
    start(days,train,food,name)
           
            
start()

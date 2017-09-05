def start(life=100,damage=1,name="",coin=5): #interger assigned to a variable
    name = game(name)
    life,damage,name,coin = fighting(life,damage,name,coin)
    
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
    return name #function that returns a string variable

def fighting(life,damage,name,coin):
    stop = True
    while stop: # while loop used
        showStats(life,damage,name,coin)
        pick = raw_input("\n Attack or increase your damage or search for loot? A/I/L").upper()
        if pick == "A": # if statment used
            print ("\n You attacked!")
            life = (life - damage) # - operator used
            stop = False
        if pick == "I":
            print ("\nYou raised your attack")
            damage = (damage + 1) # + operator used
            stop = False
        if pick == "L":
            pick2 = raw_input("\n would you like to get a better weapon or weaken the monster? W/M").upper()
            if pick2 == "W":
                damage = (damage * float(1.25)) #float assigned to a variable # * operator used
            if pick2 == "M":
                life = (life / float(1.15))# / operator used
            else:
                damage = 1%1 # % operator used
                print("\nyou found nothing and you lost your weapon")
        elif pick == "SECRET": # elif statment used
            life = 0
            secret = "you discovered a secret" #string assigned to a variable 
            print secret
        stats(life,damage,name,coin)
        
def showStats(life,damage,name,coin):
    print ("\n It has {} life and have done {} damage, {}".format(life,damage,name)) #print format function assigned
        
def stats(life,damage,name,coin): 
    if life < 0:
        killed(life,damage,name,coin)
    else: # else statment used
        fighting(life,damage,name,coin)
   
    
def killed(life,damage,name,coin): 
    import random
    print ("\nCongradulations on killing the beast this is what you found on the monster")
    tup1 = ('necklace','bracelet','fur','pants','toothpic')#tuple used (not iterated but Ic ould not find a good way to use it iterated)
    print random.choice(tup1)
    pick3 = raw_input("You killed one want to kill another one? Y/N ").upper()
    if pick3 == "Y":
        coin -= 1 # -= operator used
        print ("coins left {}".format(coin))
        if coin == 0:
            print ("\nout of money start back at the beginning!")
            start(life=100,damage=1,name="",coin=5)
        else:
            again(life,damage,name,coin)
       
    else:
        print ("\nWell to bad you have to!")
        reset(life,damage,name,coin)
   

def again(life,damage,name,coin):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").upper()
        if choice == "Y":
            stop = False
            reset(life,damage,name,coin)
        if choice == "N":
            print("\nGoodbye")
            stop = False
            exit()
        else:
            print("\nSince you can't seem to figure out yes or no, here is a list of animals for your entertainment")
            animals = ['monkey','dog','donkey','cat']
            for index in range(len(animals)): # for loop used # loop iterated through
                print 'Animals! :' , animals[index]
            print ("Please enter 'y' for 'Yes', pr 'n' for 'No' ") 
            again(life,damage,name,coin)
            
def reset(life,damage,name,coin):
    import random
    foo = [1,2,3,4,5]
    life = (100 * random.choice(foo))
    damage += 1 # += operator used
    if (life >= 400) and (damage >= 5): # and logical operator used
        coin = (coin + 5)
    start(life,damage,name,coin) #call a function you defined above


    

start()

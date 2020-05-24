import random


#Username will run the name generation in a command line for demonstration
def username():
    print ("""Welcome to the username selection process.  You will be presented with randomized username options.
If you like the username presented, type 'yes', otherwise, type 'no'.  You will not be able to go backwards.""")
    answer = None
    while answer != 'yes':
        nameoption = random.choice(open("capital_words.txt").read().split()) + " " + random.choice(open("capital_words.txt").read().split())
        nametry = input(nameoption + " ?: ")
        if nametry == 'yes':
            answer = 'yes'
            print ("Welcome, " + nameoption)

    return None

#Fullnamer will send (counter) amount of usernames to a txt file, gets very slow in recursive unique checks after 200k names
def fullnamer():
    counter = 0
    while (counter < 1000000): # <--------- change this number for usernames to generate
        nameoption = random.choice(open("capital_words.txt").read().split()) + " " + random.choice(open("capital_words.txt").read().split())
        with open("fullnames.txt", "r+") as fullnames:
            if nameoption not in fullnames:
                fullnames.write(nameoption + "\n")
                counter += 1
        counter += 0
    print ("All Finished Grant, total names created: " + str(counter))



#simple function to clear out and restart the fullnames doc by overwriting
def restarter():
    with open("fullnames.txt", "w") as fullnames:
        fullnames.write("\n")
    print ("fullnames is now empty")


#uncomment function to run below
#-------------------------------
#restarter()
#fullnamer()
username()

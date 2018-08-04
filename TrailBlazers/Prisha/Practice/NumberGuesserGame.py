#The Number Guesser Game 
from random import randint
x= 6
while True :
    b = randint (1, 21)
    print (" ------ START GAME--------")
    a= int (input (" what is your first guess"))
    if a == b :
        print (" Hooray you won") 
        break
    if a < b :
        print (" too low")
    if a > b:
        print (" too high")
   
    c= int (input (" what is your second guess "))
    if c== b:
        print (" Hooray you won")
        break
    if c < b:
        print (" too low")
    if c > b:
        print (" too high")
    d= int (input (" what is your third guess") )
    if d== b :
        print (" Hooray you won")
        break
    if d < b:
        print (" too low")
    if d > b:
        print (" too high")
    e= int (input (" what is your fourth guess") )
    if e== b:
        print (" Hooray you won")
        break
    if e < b:
        print (" too low")
    if e > b:
        print (" too high")
    f= int (input (" what is your fifth guess") )
    if f== b:
        print (" Hooray you won")
        break
    if f < b:
        print (" too low")
    if f > b:
        print (" too high")
    g= int (input (" what is your sixth guess"))
    if g== b:
        print (" Hooray you won")
        break
    if g < b:
        print (" too low")
    if g > b:
        print (" too high")
    print ("----- GAME OVER------")
    Exit = (" would you like to leave the game ")
    if Exit == "yes" : 
        break 

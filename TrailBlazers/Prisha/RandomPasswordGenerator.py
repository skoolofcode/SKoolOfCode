from random import randint 
range = int (input (" How long do you want your password to be (between 1- 10 ) "))
A= random.choice ("1,2,3,4,5,6,7,8,9,0")
randrange = randint (range , A)
if range==1:
    print (randrange)

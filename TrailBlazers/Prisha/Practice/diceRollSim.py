#dice roll Simulator
#import randint 
from random import randint
#while loop (while true ) 
while True:  
	#ask if you want to roll the dice 
    rollAgain = input (" do you want to roll the dice( say yes if you want to)")
	# if yes generate dice roll
    if rollAgain == "yes" : 
        diceRoll = randint (1,6)
        print (diceRoll)
	#else: break 
    else:
        break 
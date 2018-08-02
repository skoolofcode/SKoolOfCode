import random
import sys
def passwordfunction():
	userinput = (input("Hey! I am a Password Generator. Enter a phrase:"))
	numcmbo = ('1234567890')
	syms = ('!@#$%^&*~-')
	yourpassword = random.choice(numcmbo) + random.choice(numcmbo) + (userinput) + random.choice(syms) + random.choice(numcmbo) + random.choice(numcmbo) 
	print(yourpassword)
	satisfied = (input("Were you satisfied with your password? Enter 1 for YES and 2 for NO:"))
	if satisfied == '1':
		print("Have a nice day!")
	elif satisfied == '2':
		again = (input("Would you like to try again? Enter 1 for YES and 2 for NO:"))
		if again == '1':
			print (passwordfunction())
		elif again == '2':
			print("Sorry for the inconvienence! Have a nice day.")
		else:
			sys.exit("Your input is invalid. Please try again!")
	else:
		sys.exit("Your input is invalid. Please try again!")
passwordfunction()

import random
import sys
def passwordfunction():
	nums = ('123456789')
	color = ('blu3','p!nk','grEen','y3ll0w','or@nge','r3d','purp!e')
	rand = ('~`;:.,<>/?\|[}{] ')
	city = ('seaTtle','anaHiem','toKyo','loNDon','paRis')
	animal = ('zebr@','d0g','!ion','dr@gon','c@t')
	syms = ('!@#$%^&*')
	ask = (input('Do you need a random password generated? Go ahead and enter a number from 1-5:'))
	if ask == '1':
		password1 = random.choice(city) + random.choice(syms) * 2 + random.choice(animal) 
		print (password1)
	elif ask == '2':
		password2 = random.choice(color) + random.choice(syms) + random.choice(rand) + random.choice(animal) 
		print(password2)
	elif ask == '3':
		password3 = random.choice(syms) + random.choice(city) + random.choice(color) + random.choice(syms)
		print(password3)
	elif ask == '4':
		password4 = random.choice(nums) + random.choice(syms) + random.choice(color) + random.choice(syms) + random.choice(nums)
		print(password4)
	elif ask == '5':
		password5 = random.choice(color) + random.choice(rand) + random.choice(syms) + random.choice(nums) + random.choice(city)
		print(password5)
	else:
		sys.exit('Sorry! Your input is invalid please try again.')
	print(input("Were you satisfied with your password:"))
	print("Thank you for your feedback, Enjoy your day!")
passwordfunction()
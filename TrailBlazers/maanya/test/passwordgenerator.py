#SKC : Good job. Works!
#SKC : As a next steps - add a phrase as in problems and make the code more consise.
import random
import sys 
def passwordfunction():
	nums = ('123456789')
	color = ('blu3','p!nk','grEen','y3ll0w','or@nge','r3d','purp!e')
	rand = ('~`;:.,<>/?\|[}{] ')
	city = ('seaTtle','anaHiem','toKyo','loNDon','paRis')
	animal = ('zebr@','d0g','!ion','dr@gon','c@t')
	syms = ('!@#$%^&*')
	ask = (input('Hi! We all know how hard it is to think of a secure password now days, so I am here to help! My name is PasswordBot! Enter a random number from 1-5 that will help determine a password combo for you:'))
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
	satisfied = (input("Were you satisfied with your password? Enter 1 for yes and 2 for no:"))
	if satisfied == '1':
		print("Thank you and Have a wonderful day! :)")
	elif satisfied != '1' or satisfied != '2':
		sys.exit("Your input was invalid. Please try again!")
	elif satisfied == '2':
		sorry = (input("I am sorry to hear that :(! Would you like to try again? Enter 1 for yes and 2 for no:"))
		if sorry == '1':
			passwordfunction()
		elif sorry == '2':
			print('I am sorry for the inconvienience. Have a nice day.')
		elif sorry != '1' or sorry != '2':
			sys.exit("your input was invalid. Please try again")

	return
passwordfunction()

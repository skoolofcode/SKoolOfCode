def thecoolmathgame ():
	print("Hello. I am going to guess your age today! I promise I will not cheat :)")
	startnum = int(input("Pick a number from 1-10:"))
	print("Now I will multiply your chosen number by 2.")
	age = startnum * 2
	print ("Now I will add 5 to the new number.")
	age = age + 5
	print("Now I will multiply this total by 50")
	age = age * 50
	bday = (input("Have you already had your birthday this year? Enter '1 for YES' and '2 for NO':"))
	if bday == '1':
		age = age + 1768
	elif bday == '2':
		age = age + 1767
	else:
		print("Your input is not valid. Go ahead and try again!")
		print(bday)
	byear = int(input("Enter the year you were born:"))
	age = age - byear
	print("Okay. Your age is ready. Keep in mind through out this game you have NOT told me your age.")
	print("      ")
	print("Your number is a three-digit result. The first number (left to right) is the number you choose in the beginning . The second and third numbers (left to right) are your age. ")
	print(age)
	return
thecoolmathgame()

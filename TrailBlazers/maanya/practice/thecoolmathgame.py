def thecoolmathgame ():
	print("Hello. Today you will enter a number. I will guess it. I promise I will not cheat! You have my guarentee! I will explain you each step and you can double check if you want to! Okay, TO THE POWER OF MATH!")
	orignum = (input("Okay. Enter your number: "))
	print("Okay. I do not know what your number is, but let's see if I can figure it out. First, I will multiply it by 2.")
	thenumber = orignum * 2
	print("Now, I will add the new number by 6.")
	thenumber = thenumber + 6
	print("Now I will divide this number by 2.")
	thenumber = thenumber/2
	print("And Finally, I will subtract 6 from this new number.")
	thenumber = thenumber - 6
	print("              ")
	print("Was your original number:",thenumber,"?")
	trueornot = (input("Enter '1 ~ if Yes' and '2 ~ if No':"))
	if trueornot == '1':
		print("It is my friend: The magic of math! Raise a glass to MATH!")
	elif trueornot == '2':
		print("Oh, I am so sorry to hear that! See you next time! Bye.")
	else:
		print("I didn't really catch that, Have a nice day! Bye.")
	return
thecoolmathgame()

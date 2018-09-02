import random
def fortune():
	print("I am the Fortune Teller! Ask me a question about your future. ")
	print("      ")
	theq = input("Ask the question now:")
	theanswers = ('Without a shadow of doubt!','Never','Very Soon','It is impossible','Yes','I will show you everything','Only if you agree','No','Only once','If you choose to','Forever and Always','Not for many years')
	print("   ")
	youranswer = random.choice(theanswers)
	print(youranswer)
	return
fortune()

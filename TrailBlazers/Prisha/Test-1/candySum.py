#SKC : Good Job Prisha. The Logic is right. I love the functions for Squaring and amount cal
#SKC : Do run this. There are some syntax issues that you should resolve.
#SKC : Can u do this without using global. Hint : Return the calcuated value from square function

def Squared ():
	candies = 0
	for i in range (0, 542, 1):
		squaredCandy= i * i 
		sumOfCandies = squaredCandy + candies
		print ( sumOfCandies)
	print ("this is the cost,",sumOfCandies *.10)

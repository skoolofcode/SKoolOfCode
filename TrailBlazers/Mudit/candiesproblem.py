#SKC : Good job. I really like the nice print the say what they are printing.
#SKC : I had to change to right directory and fix the files by add .py to the file. 
#SKC : From the design point of view you should have 2 functions. one for NrofCandies 
# and other for Cost calculations
#SKC : Functions should return value. That way other can use the work that functions do. 
#So dont print in the function. Return value. Print outside the function

#Candies Problem
def candiesproblem():
	totalcandies = 0
	for i in range(0,542):
		sqrcandies = i * i
		totalcandies = totalcandies+sqrcandies
	finalcost = (totalcandies * 0.10)
	print("1. Whats the number of candies he will need? ")
	print("Answer: Mr Tom will need",totalcandies )
	print("2. Given that every candy cost 10 cents whats the total bill?")
	print("Answer: Total cost is", finalcost)
candiesproblem()

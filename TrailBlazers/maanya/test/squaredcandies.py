#SKC : Great Job! Should work great.
#SKC : Functions should return their result so that other can use it. Here make the sqcandies return
#SKC : Add another function to calcualte the cost. It take NrOfCandies as input and output price. 
#It know the price per candy
def sqcandies():
	totalcandies = 0
	for i in range(0,542):
		rollcandies = i * i
		totalcandies = totalcandies + rollcandies
	print("The total number of candies Mr.Tom needs is",totalcandies)
	return
sqcandies()

def candycost():
    totalcost = round(totalcandies * 0.10,2)
    print("The total cost of",totalcandies,"candies is $",totalcost)
    return
candycost()

def sqcandies():
	totalcandies = 0
	for i in range(0,542):
		rollcandies = i * i
		totalcandies = totalcandies + rollcandies
	totalcost = round(totalcandies * 0.10,2)
	print("The total number of candies Mr.Tom needs is",totalcandies)
	print("The total cost of",totalcandies,"candies is $",totalcost)
sqcandies()

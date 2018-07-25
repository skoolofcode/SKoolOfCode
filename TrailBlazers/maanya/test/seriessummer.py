def seriessum():
	summer = int(input("Hello I am The Series Sum Bot. Enter a number which you would like me to sum for you today:"))
	totalsum = 0
	for i in range(1,summer + 1):
		totalsum = totalsum + i 
	print(totalsum)
seriessum()

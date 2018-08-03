#SKC : Great Job! Should work great.
#SKC : Functions should return their result so that other can use it. Consider that and return 
# rather than the value inside the function i.e. can u print the final results from out of function.
#Maanya: SKC, Something like this: // I can not print 'totalsum' outside function because I would have to use Global Variables

def seriessum(summer):
	totalsum = 0
	for i in range(1,summer + 1):
		totalsum = totalsum + i 
		print(totalsum)
		return
summer = int(input("Hello I am The Series Sum Bot. Enter a number which you would like me to sum for you today:"))
seriessum()

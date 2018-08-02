#SKC : Good job!
#SKC : Why while ( 9>sum )? Can u replace this with the right way to do the infinity loop 


while True:
	N = int (input (" enter a positive number "))
	for i in range (1, N+1):
		sum += i
print (sum)
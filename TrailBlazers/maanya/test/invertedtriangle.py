def triangle():
	n=int(input('Enter the number of lines for this triangle: '))
	for i in range(n,0,-1):
		print ((n-i)*' '+i*'* ')
triangle()

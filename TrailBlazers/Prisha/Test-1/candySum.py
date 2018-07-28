#SKC : Good Job Prisha. The Logic is right. I love the functions for Squaring and amount cal
#SKC : Do run this. There are some syntax issues that you should resolve.
#SKC : Can u do this without using global. Hint : Return the calcuated value from square function

def Squared ():
	for i in range (0, 542, 1):
		squaredCandy= i * i 
		global squaredCandy
		print ( squaredCandy)
Squared()
def Amount (squaredCandy):
	print ("this is the cost,",squaredCandy *.10)
Amount(squaredCandy)

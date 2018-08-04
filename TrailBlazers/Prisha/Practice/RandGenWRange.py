#random number generator w/range
n = 0
p = 1
while True:
    print (" ------ new game-----")
    A = int (input (" what number should we start with "))
    Z = int  (input (" what number should we end with"))
    RandGen = randint (A, Z) 
    print (RandGen)
    if n == p:
    	break 
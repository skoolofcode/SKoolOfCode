#SKC : Good job with the logic.
#SKC : Dont use global. Write functions for squaring and cost. Use return.
x = 0

for number in range(1,542,1):
    print("Roll number is ", number)
    can = number * number
    print("This is how many candies roll", number,"will have",can)
    global x 
    y = x + can
    x = y
    
    
cost = x * 0.10
print("The candies will cost", cost)

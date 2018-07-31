x = 0
for number in range(1,542,1):
    print("Roll number is ", number)
    can = number * number
    print("This is how many candies roll", number,"will have",can)
    y = x + can
    x = y

cost = x * 0.10

print("The candies will cost", cost)

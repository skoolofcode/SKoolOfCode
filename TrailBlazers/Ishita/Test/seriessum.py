#SKC : Good job with the logic.
#SKC : Dont use global. Write functions. Use return.

num = int(input("WHat is the number you would like me to tell you the sum of?"))

x = 0
n = num+1
for i in range(1,n):
    ns = i
    global x
    y = x + ns
    x = y
    

print(x)

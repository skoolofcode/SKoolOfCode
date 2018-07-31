def ss():
    num = int(input("WHat is the number you would like me to tell you the sum of from 1 to that number?"))
    x = 0
    n = num+1
    for i in range(1,n):
        ns = i
        y = x + ns
        x = y

    print(x)
ss()

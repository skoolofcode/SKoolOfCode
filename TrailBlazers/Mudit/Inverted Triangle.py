#SKC : Good job. Love that you did the MATH of this problem first. Great!
#SKC : The triangle does not come perfect for odd number. For even number a bit more imperfect.
#But i like your MATH approach to this. Try back again ; You can make it perfect.
#SKC : Encapsutate this to a function.
 
#PROBLEM = INVERTED TRIANGLE
num=int(input('Enter an odd number width: '))
for i in range(num+1, 0, -1) :
    number = int((num - i)/2)
    print(' '* number + '*'*i)

#SKC : Good job with the logic.
#SKC : Write functions.

a= int(input("How many stars on top row?"))

for i in range(a,0,-2):
    print ((a-i)*' '+i*'* ')

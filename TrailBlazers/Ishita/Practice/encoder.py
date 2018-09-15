c = int(input("What is the ninja number?(less than 10)"))
s = input("Hi! What is the messaage? ")

for i in s:
    a = ord(i)
    print('Secret code:')
    b = a + 10 -c
    print(b)
    
print("Give the ninja number and the number of characters(including the spaces) and each of the secret codes to the person you want the message to go to.")
    

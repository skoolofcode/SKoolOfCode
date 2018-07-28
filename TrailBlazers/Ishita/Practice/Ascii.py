c = int(input("What is the ninja number?(less than 10)"))
s = input("Hi! What is the messaage? ")

for i in s:
    a = ord(i)
    print('Secret code:')
    b = a + 10 -c
    print(b)
    
a = int(input("How many characters in the code?"))
e = int(input("Secret number?"))
c = int(input("What is the code?"))
d = c - 10 +e
print(chr(d))
g = a-1

for i in range(g):
    
    b = int(input("Next number?"))
    f = b - 10 +e
    print(chr(f))
            

print("Bye!")


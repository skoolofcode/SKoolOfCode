#Print a decimal number as binary
#"{0:b}".format(number)
j = 45
print("The number j in decimal is ",j)
print("{0:b}".format(j))

#Use ord() to get Ascii codes for a given character
storeACharacter = 'a'
print("I am printing a character ", storeACharacter)
print("The ASCII code for a is ", ord(storeACharacter))

#Lets convert a whole sentence to ascii
tmp = "This is a live coding demo"
for m in tmp:
    print("Ascii for character ", m , "is ", ord(m))
    
    

# Let's write a secret message ;-)
# Part - 1 - Let's just write Ascii
letter = "This is a secret This is a secret This is a secret This is a secret"
count = 0
for m in letter:
    print("",10+ord(m),end='')
    



# Part 2 - Ascii may be too simple and easily infered
# So we will jumble up

# Part 3 - More complex code. Note you have to also decode

#Print a decimal number as binary
i = 255
print("{0:b}".format(i))

#Get the size of a given object
j = 56.45
import sys
print("size of float is", sys.getsizeof(j))


name = "SKoolOfCode is Kool!"
for c in name:
    print(" ",ord(c),end='')
    
print("")
    
# Let's write a secret message ;-)
# Ascii itlsef is a code but that may be too simple!
# So we will jumble up

secretMessage = "SKoolOfCode is Kool!"
randomJumleSeed = 9

for c in secretMessage:
    print(" ", ord(c) + randomJumleSeed,end="")
    

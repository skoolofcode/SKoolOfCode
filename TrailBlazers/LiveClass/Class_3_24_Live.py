#Writing to Files

def myQuickReading(name):
    f = open(name,"r")
    for line in f:
        print(line,end="")
    f.close()
    
print("=== START Write to file === \n")
f = open("data/myWritingFile.txt","w")
f.write("My name is Bla Bla")
f.close()

myQuickReading("data/myWritingFile.txt")
print("\n")
print("=== END Write to a file === \n")

print("=== START Write 10 lines to a file === \n")

i = -20
while(i!=10):
    #f = open("data/my10LineFile.txt","w")
    f = open("data/my10LineFile.txt","a")
    f.write("My name is Bla Bla\n")
    f.close()
    i = i+1

myQuickReading("data/my10LineFile.txt")

print("\n")
print("=== END Write 10 lines to a file === \n")



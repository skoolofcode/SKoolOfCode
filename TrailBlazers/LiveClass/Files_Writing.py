#Writing to a file.
def read_print_file(name):
    f = open(name,"r")
    for line in f:
        print(line)
    f.close()

#The "w" option
print("=== START Write to a file ==\n")
#Let's write 10 lines to a file
f = open("data/newFile.txt","w") # Note : "w"
f.write("My name is Sam!")
f.close()


print("writing to file has finished!")
print("Below is the file content that's read")

read_print_file("data/newFile.txt")

print("=== END Writing a file ==\n")


#The "w" option
print("=== START Writing 10 lines file ==\n")
#Let's write 10 lines to a file
i = 0

while(i !=10):
    f = open("data/newFile.txt","w") # Note : "w"
    f.write("My name is Sam!")
    f.close()
    i = i + 1

print("writing to file has finished!")
print("Below is the file content that's read")

read_print_file("data/newFile.txt")

print("=== END Writing a new file ==\n")

#The "a+" option
print("=== START Writing a new file in append mode ==\n")
i = 0

while(i !=10):
    f = open("data/newFile.txt","a") # Note : "a" and "w"
    f.write("My name is Sam!\n")
    f.close()
    i = i + 1

print("writing to file has finished!")
print("Below is the file content that's read")

read_print_file("data/newFile.txt")
    
print("=== END Writing a new file in append mode ==\n")


#Closing
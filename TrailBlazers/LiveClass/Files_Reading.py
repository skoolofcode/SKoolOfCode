#Opening a file using the required permissions
f = open("data/drSeuss_green_eggs_n_ham.txt","r")

#Reading a file using readline() function
print("== Using for loop to read and print a file line by line ==")

#Default print parameters
for line in f:
    print(line)

#Extra new lines after the every line. Why?

#Specify print parameters for exactly printing as in file
#How to fix that - dont need an extra new line after every line
#Specify the end of line for print function. By default its the "newline".
for line in f:
    print(line,end='')
    
f.close()
    
#Reading a file using readline() function
print("== Read a file using readline() ==")

f = open("data/drSeuss_green_eggs_n_ham.txt","r")
line = f.readline()
print(line)

while(line!=""):
    line = f.readline()
    print(line,end='')
f.close()

#Reading a file with read() function
print("\n === START Read a file using read() ==")
f = open("data/drSeuss_green_eggs_n_ham.txt","r")
txt = f.read(10)
print(txt)
f.close()
print("=== END Read a file using read() ==\n")



#Detour ;-)
#How to get help within from the programming topics. 
#pydocs and help utility in python shell. Demo!


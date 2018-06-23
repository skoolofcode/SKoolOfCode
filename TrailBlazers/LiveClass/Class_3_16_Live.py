#Opening a file using the required mode
f = open("data/drSeuss_green_eggs_n_ham.txt","r")

#Reading a file using readline() function
print("===== START Let's read the file=====")

for line in f:
    print(line)
f.close()
print("===== END Let's read the file=====")
#Default print parameters

#Extra new lines after the every line. Why?
#How to fix extra lines after EOL
print("===== START Let's read the file (no extra  lines)=====")
f = open("data/drSeuss_green_eggs_n_ham.txt","r")

for line in f:
    print(line,end='')

print("===== END Let's read the file===== (no extra  lines)")
f.close()

#Reading a file using readline() function
print("===== START Let's read the file using readline =====")
f = open("data/drSeuss_green_eggs_n_ham.txt","r")

line = f.readline()

while(line!=""):
    line=f.readline()
    print(line, end="")

f.close()
print("===== END Let's read the file using readline =====")


#Reading a file with read() function
print("===== START Let's read the file using read =====")
f = open("data/drSeuss_green_eggs_n_ham.txt","r")

first10Chars = f.read(10)
print(first10Chars,end='')

f.close()

print("===== END Let's read the file using read =====")

#Detour ;-)
#How to get help within from the programming topics. 
#pydocs and help utility in python shell. Demo!


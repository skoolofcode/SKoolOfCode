#Almost eveything in python is a object. 
#Let's a simple example e.g. string

#Dir function to find
myName = "Shiv"
print("Operations supported by object named",myName, dir(myName))

#Note the supported operations are not depedent on the variable name but 
#on the name what type of object is stored in the variables. 
#We had a 'string' stored in myName. Let's store a integer instead

myName = 10
print("====================================")
print("Operations supported by object named",myName, dir(myName))

#Let's look at the String Object in detail
myName = "Bye Bye miss Tyler! See you tomorrow or day after tomorrow"

print("Printing upper case for myName ", myName.upper())
print("Printing lower case for myName ", myName.lower())
#print("Printing length of myName ", len(myName))

print("Numer of occurances of 'Bye'", myName.count('Bye'))



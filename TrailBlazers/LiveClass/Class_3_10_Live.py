#Almost eveything in python is a object. 
#Let's a simple example e.g. string

#Dir function to find
myName = "Shiv Prashant Sood"
print("Interfaces supported by string object are ", dir(myName))

myName = 200
print("Interfaces supported by integer object are ", dir(myName))


#Note the supported operations are not depedent on the variable name but 
#on the name what type of object is stored in the variables. 
#We had a 'string' stored in myName. Let's store a integer instead

myHello = "hello Hello! Class"
print("Let's print the variable myHello", myHello)
print("Let's print in upper case ", myHello.upper())
print("Let's print in lower case ", myHello.lower())
#print("Printing length of myName ", len(myName))
print("Let's print the size of myHello", len(myHello))

print("=============LIST=======================")
#Lists
groceryList = ['milk', 'fruits', 'greens']
print("Print my list ", groceryList)

#I can add to the list
groceryList.append("carrots")
print("Print my list after append ", groceryList)

#Iterating thru the list
itemFound = False
searchItem = 'milk'

print("=============LIST Iteration=======================")
for item in groceryList:
    print(item)
    if(item==searchItem):
        itemFound = True
        break

print("Carrot Found equals ", itemFound)

print("=============LIST Reverse=======================")
print("Print my list after append ", groceryList)
#groceryList.reverse()
print("Print the reversed list",groceryList)

print("=============LIST SORT=======================")
groceryList.sort()
print("Print the sorted list", groceryList)








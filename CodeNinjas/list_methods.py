print("*** Hello - The world of Lists!! ***")

# Creating a list
groceryList = ["Milk", "Oranges", "Cookies", "Bread"]

print("\n*** Printing my list ***")
print(groceryList)

#Appending to list i.e. add a element to a list
print("\n*** Let's add Pizza Dough to the list ***")
groceryList.append("Pizza Dough")
print(groceryList)

#Lenght of list i.e how many elements in the list
print("\n *** Lenght of the list ***")
print(len(groceryList))

#Remove from the list
print("\n *** Remove from list ***")
groceryList.remove("Oranges")
print(groceryList)

#Find position of a item in the list
print("\n *** ind position of a item Cookies in the list ***")
print(groceryList.index("Cookies"))

#Count the number of times a item appears in the list
print("\n *** Number of times Coookies appear in the list", groceryList.count("Cookies"))




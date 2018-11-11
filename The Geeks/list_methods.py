# This file we'll be talking about Lists.

#Create a list
print("\n *** printing the list ***")
groceryList = ['Milk', 'Oranges', "Cookies", "Bread"]
print(groceryList)

#Append to the list. This also means add a item to the list
print("\n*** Add pumpkin to the list")
groceryList.append("pumpkin")
print(groceryList)

#Lenght of the list.
print("\n*** Lenght of the list after adding pumpkin")
print(len(groceryList))

#Remove an item from the list
print("\n*** let's remove pumpkin from the list")
groceryList.remove("pumpkin")
print(groceryList)

#Find the position of a given element
print("\n*** Let's find the position of Oranges in the list")
print(groceryList.index("Oranges"))

#Lets access Orange using its position
print("\n*** Lets access Orange using its position")
element = groceryList[1]
print(element)

#Let's use index to find the position of Oranges and then print it
i = groceryList.index('Oranges')
element = groceryList[i]
print("\n*** Let's use index to find the position of Oranges and then print it")
print(element)


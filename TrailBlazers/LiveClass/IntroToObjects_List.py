#Lists - An unordered sequence of items
groceryList = ['Greens', 'Fruits', 'Milk']
print("My Grocery list is ", groceryList)

#You can iterate over lists. What's Iterate?
#Iterate means go one by one element traverssing the full list

#We may need to iterate the list to take some action on the given item
#e.g. what is we want to check if the list has 'Carrots'. If not add it.
carrotFound = False
for item in groceryList:
    if(item=='Carrots'):
        carrotFound = True
        break

if(carrotFound == False):
    groceryList.append('Carrots')
    
print('Revised grocery list',groceryList)

#Other operations on a list
groceryList.reverse()
print("remove a item ",groceryList)

groceryList.sort()
print("sort a item ",groceryList)



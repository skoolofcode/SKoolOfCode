#Operators : +, *
# We have used operators on simple data structures like integer, strings etc. 
# List is also a data structure. Severral of these operators are relevant for List as well.
# Here we learn the 
# 1. How to use operators on list where relevant (+ and *)
# 2. A new operator that's use to slice i.e create/change sublist from a list

codeNinjas = ['Ranvir', 'Sonakshi','Suhas','Vineel']
thegeeks = ['Prisha', 'Akalsukh','Angad','Prabhgun']

#The + operators appends its 2 operands. in this case the 2 lists.
allstudentList = codeNinjas + thegeeks 

print(codeNinjas)
print(thegeeks)
print(allstudentList)

#Let's see the multiplication operator
three_codeNinjas = codeNinjas * 3
print(three_codeNinjas)

list_of_numbers1 = [1,2,3,4,5]
list_of_numbers2 = [1,2,3,4,5]

#Adding would give me a list which is [2,4,6,8,10]? No
list_final = list_of_numbers1 + list_of_numbers2
print(list_final)

#Multiplication. Should this give answer as [3,6,9,12,15]? No
list_final2 = list_of_numbers1*3
print(list_final2)


#Operators are fun as you get to create new list from existing lists


# + and * operator on list. 



#Slicing operator

#Subset a list - get some portion of a list

#Change a subset of list
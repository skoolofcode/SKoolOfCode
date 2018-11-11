#Loops on list - Why?
#Iterating a list
#Example

num_list = [1,2,3,200,30,23,1]

for y in num_list:
    print("i am the number ", y)

#I want to find the square of each of the numbers in the list
for x in num_list:
    tmp_square = x*x
    print("sqauare of ", x, "is", tmp_square)
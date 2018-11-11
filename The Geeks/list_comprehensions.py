my_list = [ item*item for item in range(0,200) if item % 2 == 0 ]
print(my_list)

#Let's write a table of 7 with list comprehension
my_table_of_7 = [7*item for item in range(1,11)]
print("Table of 7 is",my_table_of_7)


def add(x, y):
   print(x + y)
   return
def subtract(x, y):
   print(x - y)
   return
def multiply(x, y):
   print(x * y)
   return
def divide(x, y):
   print(x / y)
   return
print("Select your operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operation = input("Enter the operation you would like(1, 2, 3, or 4):")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if operation == '1':
   print(add(x,y))

elif operation == '2':
   print(subtract(x,y))

elif operation == '3':
   print(multiply(x,y))

elif operation == '4':
   print(divide(x,y))
else:
   print("Invalid Input")

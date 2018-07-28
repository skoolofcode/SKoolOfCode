d=input("Would you want to add a phone number to the phonebook or find?")

if d == "Add":
	
	while True:
	

		file = open('phonebook.txt', 'a')
		print("Enter X for stopping(This stops only in the name.)")
		a=input("Name?")
		if a == "X":
			break
		b=input("Phone number?")
		c=input("Additional info?")
		file.write("\nName-  ")
		file.write(a)
		file.write("       Phone Number-  ")
		file.write(b )
		file.write("       Additional info-  ")
		file.write(c)
		
		file.close()
    
if d == "Find":
	file=open('phonebook.txt', 'r')
	e=str(input("Tell me the name of the person."))
	for line in file:
		line.strip().split('/n')
		if e in line:
			print(line)
			
	file.close()

else: 
	print("Wrong value, there!")

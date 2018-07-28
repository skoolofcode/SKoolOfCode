print(" I am going to take your name and age and tell you the exact year you will turn the age you tell me.")

name = input("What is your name?")
age = int(input("What is your age?"))
year = int(input("What age do you want me to find out?"))
now = int(input("What year is it now?"))

sub = now-age
ans = sub + year

print(name, "will be", year, "years old in the year",ans)

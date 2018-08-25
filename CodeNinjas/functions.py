def hello(personname, day):
    dayOfTheYear = 45
    print("Hello " , personname, "Have a happy ",day)
    print("Day of the year is ", dayOfTheYear)
    return dayOfTheYear

dayToday = "Monday"
name = "Suhas"
dayReturned = hello(name,dayToday)
print("Print the returned day", dayReturned)

name= "Sonakshi"
hello(name, "Tuesday")


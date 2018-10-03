def taxcalculator():
    thecost = float(input("Enter the total cost:"))
    taxrate = float(input("Enter the state tax rate:"))
    tax = thecost * taxrate/100
    totalcost = round(thecost + tax,2)
    print("     ")
    print("The total cost is:",totalcost,"dollars.")
taxcalculator()

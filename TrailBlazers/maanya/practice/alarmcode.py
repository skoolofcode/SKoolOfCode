def hourscode():
	thecurrenttime = int(input("Hello. Enter the time in a 24 hour frame. For example, If it is 1:00, enter 13:"))
	thepassinghrs = int(input("Okay, now how many hours would you like to pass before the alarm rings:"))
	hours = round(thepassinghrs/24, 0)
	if thepassinghrs < 24:
		thetimethealarmrings = thecurrenttime + thepassinghrs
		if thetimethealarmrings > 24:
			thetimethealarmrings = thetimethealarmrings - 24
	else:
		thetimethealarmrings = thecurrenttime + hours
	print(" ")
	print("The alarm will ring when it is", thetimethealarmrings," in a 24 hour frame.")
	return
hourscode()

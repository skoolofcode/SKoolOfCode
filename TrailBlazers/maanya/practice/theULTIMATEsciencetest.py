import sys
def thetest():
	print("Hello! Are you rushing to study for a science test or plainly bored? This is THE ULTIMATE SCIENCE QUIZ! ")
	print("                                                    ")
	print("~-~-~-~-THE ULTIMATE SCIENCE TEST-~-~-~-~-")
	print("                                                    ")
	print("Here are the main branches of science:")
	print("1. Earth and Space SCIENCE")
	print("2. Life SCIENCE")
	print("3. Physical SCIENCE")
	scisub = input("What subject in science would you like to learn? Enter 1, 2, or 3:")
	if scisub == '1':
		earthandspace()
	elif scisub == '2':
		life()
	elif scisub == '3':
		physical()
	else: 
		sys.exit("Your input is invalid! Please Try Again.")
		print(thetest())
	return 

def earthandspace():
	score = 0
	print("                                    ")
	print("~~EARTH AND SPACE SCIENCE~~")
	print("                                    ")
	print("1. Fill in the blank: 'Ocean Currents influence temperature by __________.' ")
	print("A. Eroding Shorelines ")
	print("B. Heating or cooling the air")
	print("C. Washing warm, dry sediments out to sea")
	print("D. Distributing Rays of Sunlight")
	q1eass = (input("Enter A,B,C, or D:"))
	if q1eass == 'B' or q1eass == 'b':
		print("That is correct! Good Job!")
		score = 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("2. Fill in the blank: Stars that are alinged in the sky are called __________.")
	print("A. Satellites ")
	print("B. Constellations")
	print("C. Telescopes")
	print("D. Galaxies")
	q2eass = (input("Enter A,B,C, or D:"))
	if q2eass == 'B' or q2eass == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The Correct answer is B.")
		score = score
	print("3. Fill in the Blanks: Days are caused by Earth's ________")
	print("A. Destruction")
	print("B. Climate Change")
	print("C. Revolution")
	print("D. Rotation")
	q3eass = (input("Enter A,B,C, or D:"))
	if q3eass == 'D' or q3eass == 'd':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is D.")
		score = score
	print("4. Fill in The Balnks: Seasons are caused by _______ ")
	print("A. The tilt of the Earth's axis")
	print("B. Earth's distance from the sun")
	print("C. The sun's temperature")
	print("D. The Calendar")
	q4eass = (input("Enter A,B,C, or D:"))
	if q4eass == 'A' or q4eass == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("5. Which of the following forms of radiation can be sheilded by the Earth's Atmosphere?")
	print("A. Visible light")
	print("B. Radio waves")
	print("C. Gamma Rays")
	print("D. All of the above")
	q5eass = (input("Enter A,B,C, or D:"))
	if q5eass == 'C' or q5eass == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("6. What is the most distinctive feature of Jupiter?")
	print("A. The Great Dark Spot")
	print("B. The Great Red Spot")
	print("C. Rings")
	print("D. An Elongated Orbit")
	q6eass = (input("Enter A,B,C, or D:"))
	if q6eass == 'B' or q6eass == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is B.")
		score = score
	print("7. Which planet rotates faster than any other planet in the solar system?")
	print("A. Jupiter")
	print("B. Earth")
	print("C. Mercury")
	print("D. Neptune")
	q7eass = (input("Enter A,B,C, or D:"))
	if q7eass == 'A' or q7eass == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("8. Fill in The Blanks: All the OUTER PLANETS Rotate with their axes perpendicular to their orbital planes except __________. ")
	print("A. Saturn")
	print("B. Jupiter")
	print("C. Uranus")
	print("D. Neptune")
	q8eass = (input("Enter A,B,C, or D:"))
	if q8eass == 'C' or q8eass == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("9. Fill in The Blanks: During each orbit around Earth, the moon spins ons its axis __________. ")
	print("A. 1 time")
	print("B. About 27 times")
	print("C. 365 times")
	print("D. 17 1/2 times")
	q9eass = (input("Enter A,B,C, or D:"))
	if q9eass == 'A' or q9eass == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("10. Fill in The Blanks: At the equator, the sun's rays always strike Earth _________. ")
	print("A. At a low angle ")
	print("B. 18 houres per day")
	print("C. At nearly a 90 degree angle ")
	print("D. Less than 4 hours a day")
	q10eass = (input("Enter A,B,C, or D:"))
	if q10eass == 'C' or q10eass == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("             ")
	print("Congrats! You have completed The Ultimate Earth and Space Science quiz!")
	print("Your score is ",score, "/10.")
	again = (input("Would you like to play again? If 'YES ~ Enter 1' and If 'NO ~ Enter 2':"))
	if again == '1':
		print(thetest())
	elif again == '2':
		print("Okay! Bye :) Have a good day!")
	else:
		print("Sorry... I didn't catch that! Try again.")
		print(again)
	return

def physical():
	score = 0
	print("                                    ")
	print("~~PHYSICAL SCIENCE~~")
	print("                                    ")
	print("1. Which of the following is NOT a branch of Physical Science? ")
	print("A. Physics ")
	print("B. Botany")
	print("C. Chemistry")
	q1ps = (input("Enter A,B, or C:"))
	if q1ps == 'B' or q1ps == 'b':
		print("That is correct! Good Job!")
		score = 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("2.Fill in the Blank: Using superconductors to build computers is an example of __________.")
	print("A. Applied Biology ")
	print("B. Physics and The Elements of The Periodic Table")
	print("C. Technology")
	print("D. An Experiment")
	q2ps = (input("Enter A,B,C, or D:"))
	if q2ps == 'C' or q2ps == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is C.")
		score = score
	print("3.Fill in the Blank: Matter is __________.")
	print("A. Dead weight ")
	print("B. Newtons 1st Law of Motion")
	print("C. Liquids that take up space")
	print("D. Anything that has mass and takes up space")
	q3ps = (input("Enter A,B,C, or D:"))
	if q3ps == 'D' or q3ps == 'd':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is D.")
		score = score
	print("4.Fill in the Blank: Compounds and Elements are __________.")
	print("A. Mixtures  ")
	print("B. Pure Substances")
	print("C. Dense")
	print("D. Always Solid")
	q4ps = (input("Enter A,B,C, or D:"))
	if q4ps == 'B' or q4ps == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("5. Which of the following is a Physical Change?")
	print("A. Burning Paper")
	print("B. Rusting Iron")
	print("C. Burning Gasoline")
	print("D. Melting Ice Cubes")
	q5ps = (input("Enter A,B,C, or D:"))
	if q5ps == 'D' or q5ps == 'd':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is D.")
		score = score
	print("6. Fill in the Blank: Fluid pressure is ALWAYS Directed _________.")
	print("A. Up")
	print("B. In all Directions")
	print("C. Down")
	print("D. Left")
	q6ps = (input("Enter A,B,C, or D:"))
	if q6ps == 'B' or q6ps == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("7. Fill in the Blank: Materials that can flow to fit their containers include _______.")
	print("A. Both Liquids and Gases")
	print("B. Neither Liquids or Gases")
	print("C. Liquids")
	print("D. Gases ")
	q7ps = (input("Enter A,B,C, or D:"))
	if q7ps == 'A' or q7ps == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is A.")
		score = score
	print("8. Fill in the Blank: According to modern day models of the atom, ________.")
	print("A. Atoms never have neutrons, They consist of only Electrons and Protons")
	print("B. Neutrons have an extreme positive charge")
	print("C. Electrons and Neutrons circle Protons")
	print("D. Moving Electrons form an Electron Cloud")
	q8ps = (input("Enter A,B,C, or D:"))
	if q8ps == 'D' or q8ps == 'd':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is D.")
		score = score
	print("9. Which statement about atoms of elements in the same group of the periodic table is true?")
	print("A. They have the same number of Protons")
	print("B. They have similar chemical properties")
	print("C. They have the same Mass Number")
	print("D. They have the same number of electrons")
	q9ps = (input("Enter A,B,C, or D:"))
	if q9ps == 'B' or q9ps == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("10. Which of the following materials is an example of a solid dessolved into another solid?")
	print("A. Bronze ")
	print("B. Smoke")
	print("C. Mayonaise")
	print("D. Ice")
	q10ps = (input("Enter A,B,C, or D:"))
	if q10ps == 'A' or q10ps == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is A.")
		score = score
	print("             ")
	print("Congrats! You have completed The Ultimate Physical Science quiz!")
	print("Your score is ",score, "/10.")
	again = (input("Would you like to play again? If 'YES ~ Enter 1' and If 'NO ~ Enter 2':"))
	if again == '1':
		print(thetest())
	elif again == '2':
		print("Okay! Bye :) Have a good day!")
	else:
		print("Sorry... I didn't catch that! Try again.")
		print(again)
	return

def life():
	score = 0
	print("                                    ")
	print("~~LIFE SCIENCE~~")
	print("                                    ")
	print("1. Who is the FATHER Of Organic chemistry ")
	print("A. Aristole ")
	print("B. Robert Boyle")
	print("C. Isaac Newton")
	print("D. Liam Hemsworth")
	q1ls = (input("Enter A,B,C, or D:"))
	if q1ls == 'B' or q1ls == 'b':
		print("That is correct! Good Job!")
		score = 1
	else:
		print("Sorry, that is incorrect... The correct answer is B.")
		score = score
	print("2. Fill in the blank: The term antibiotic was creted by __________.")
	print("A. Alexander Flemming")
	print("B. Selman Waksman")
	print("C. Elizabeth Blackwell")
	print("D. Oswald Avery")
	q2ls = (input("Enter A,B,C, or D:"))
	if q2ls == 'B' or q2ls == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The Correct answer is B.")
		score = score
	print("3. Fill in the Blanks: Fructose Sugar is also kown as ________")
	print("A. Blood Sugar")
	print("B. Cane Sugar")
	print("C. Grape Sugar")
	print("D. Sweet Sugar")
	q3ls = (input("Enter A,B,C, or D:"))
	if q3ls == 'D' or q3ls == 'd':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect... The correct answer is D.")
		score = score
	print("4. What is the number of the elements in The Periodic Table that are natural? ")
	print("A. 90")
	print("B. 39")
	print("C. 100")
	print("D. 49")
	q4ls = (input("Enter A,B,C, or D:"))
	if q4ls == 'A' or q4ls == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("5. Which of the following is considered non-living?")
	print("A. Grass")
	print("B. Bacteria")
	print("C. Water")
	print("D. All of the above")
	q5ls = (input("Enter A,B,C, or D:"))
	if q5ls == 'C' or q5ls == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("6. Which of the following IS NOT a primary chemical in cells?")
	print("A. Protein")
	print("B. Minerals")
	print("C. Carbohydrates")
	print("D. Nuclecic Acids")
	q6ls = (input("Enter A,B,C, or D:"))
	if q6ls == 'B' or q6ls == 'b':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is B.")
		score = score
	print("7. Which of the following is a AUTOTROPH?")
	print("A. Tree")
	print("B. Butterfly")
	print("C. Toad")
	print("D. Shrimp")
	q7ls = (input("Enter A,B,C, or D:"))
	if q7ls == 'A' or q7ls == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("8. Which of the following is a HETEROTROPH?")
	print("A. Grass")
	print("B. Wheat")
	print("C. Ant")
	print("D. Flower")
	q8ls = (input("Enter A,B,C, or D:"))
	if q8ls == 'C' or q8ls == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("9. Which of these characteristics is a property only in the plant kingdom?  ")
	print("A. They have Leaves")
	print("B. The cells have walls")
	print("C. They can be found in water and land")
	print("D. They come in various colors")
	q9ls = (input("Enter A,B,C, or D:"))
	if q9ls == 'A' or q9ls == 'a':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is A.")
		score = score
	print("10. Which of these are found only in Plant Cells.")
	print("A. Cell Membrane ")
	print("B. DNA")
	print("C. Chloroplasts")
	print("D. Nucleus")
	q10ls = (input("Enter A,B,C, or D:"))
	if q10ls == 'C' or q10ls == 'c':
		print("That is correct! Good Job!")
		score = score + 1
	else:
		print("Sorry, that is incorrect...The correct answer is C.")
		score = score
	print("             ")
	print("Congrats! You have completed The Ultimate Life Science quiz!")
	print("Your score is ",score, "/10.")
	again = (input("Would you like to play again? If 'YES ~ Enter 1' and If 'NO ~ Enter 2':"))
	if again == '1':
		print(thetest())
	elif again == '2':
		print("Okay! Bye :) Have a good day!")
	else:
		print("Sorry... I didn't catch that! Try again.")
		print(again)
	return

thetest()
earthandspace()
physical()
life()

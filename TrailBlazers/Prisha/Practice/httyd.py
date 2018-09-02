twoOne = 10
TwoTwo = 11
TwoThree=12
TwoFour = 13
TwoFive = 14
TwoSix = 15
TwoSeven = 16
TwoOneOne =17
TwoOneTwo = 18
TwoTwoOne = 19
TwoTwoTwo = 20
TwoTwoThree = 21
TwoThreeOne = 22
TwoThreeTwo = 23
TwoThreeThree=24
TwoThreeFour=25
TwoFourOne = 26
TwoFourTwo = 27
TwoFiveOne=28
TwoFiveTwo=29
TwoSixOne=30
TwoSixTwo = 31
TwoSevenOne = 32
TwoSevenTwo = 33
TwoFourThree = 34
print ("Dragon discriptions and all reashearch was done on: howtotrainyourdragon.wikia.com/wiki/")
def intro ():
	print ("------Start----")
	print ("in this quiz i will ask you some questions and in the end i will tell you the httyd that fits you based on your personality")
	name=input (print("what is your name"))
def Questions():
	print ( "-------Question One-------")
	print (" which dragon class do you most prefer???")
	print (" 1.Stoker:Stoker Class dragons are hot-headed fire breathers")
	print (" 2.Strike:Strike Class dragons are characterized by their blazing speed, vice-like jaw strength, and extreme intelligence. ")
	print (" 3.Mystery:Little is known about the Mystery Class dragons due to how stealthy and sneaky they are or how they work.")
	print (" 4.Tracker:Tracker Class dragons have a highly acute sense of smell or taste that enables them to track down and find things.")
	print (" 5.Boulder:Boulder Class dragons are tough and are associated with the earth")
	print (" 6.Sharp:Sharp Class dragons are vain and prideful, and they all possess sharp body parts.")
	print (" 7.Tidal:Tidal Class dragons live in or near the ocean")
	global answerOne
	answerOne = int (input ("enter a number 1-7"))
def QuestionTwo (answerOne):
	global twoOne
	if answerOne == 1:
		print ("------Question Two-----")
		print (" which size dragon do you want, NOTE: small dragons are not rideable thus not in this quiz ")
		print ("1. Medium")
		print ("2. Large")
		twoOne = int (input ("enter a number 1-2"))
	
	if answerOne == 2:
		print ("------Question Two-----")
		print (" whih real life animal attracts you the most")
		print ("1.Scorpion")
		print ("2.Black Panthers")
		print ("3.Electric eels")
		global TwoTwo
		TwoTwo = int (input ("enter a number 1-3"))
	if answerOne == 3:
		print ("------Question Two----")
		print (" what so you want your dragons other special ability to be")
		print ("1. A Magnetic Body")
		print ("2. The ability to mimic fire")
		print ("3. Camaflouge")
		print ("4. a song that lures prey")
		global TwoThree
		TwoThree = int (input("enter a number 1-4"))
	if answerOne == 4:
		print ("------Question Two-----")
		print (" what fire type do you prefer")
		print (" 1.magnesium blast")
		print (" 2.Greenish fire")
		print (" 3.Flaming rock missles")
		global TwoFour
		TwoFour = int (input ("enter a number 1-3"))
	if answerOne == 5 :
		print ("------Question Two-----")
		print ("how commom do you want your dragon to be ")
		print ("1.commom")
		print ("2.very rare")
		global TwoFive
		TwoFive = int (input ("enter a number 1-3"))
	if answerOne == 6:
		print ("------Question Two-----")
		print ("what weakness do you want your dragon to have")
		print ("1.underbelly/belly is vunerable")
		print ("2.No Legs")
		global TwoSix
		TwoSix = int (input ("enter a number 1-2"))
	if answerOne == 7:
		print ("------Question Two-----")
		print ("what should yur dragon eat")
		print ("1.fish/crab")
		print ("2.Smaller tidal class dragons")
		global TwoSeven
		TwoSeven = int (input ("enter a number 1-2"))
def QuestionThreeStoker (twoOne):
	if twoOne== 1:
		print ("------Question Three-----")
		print ("What do you want your dragons special ability to be")
		print ("1.ability to change color depending one his/hers mood")
		print ("2.lighting itself on fire")
		global TwoOneOne
		TwoOneOne = int (input ("enter a number 1-2"))
	if twoOne ==2:
		print ("------Question Three-----")
		print ("what should your dragon eat")
		print ("1. eels")
		print ("2. Ice Tail Pike, a type of fish")
		global TwoOneTwo
		TwoOneTwo = int (input ("enter a number 1-2"))
def QuestionThreeStrike (TwoTwo):
	if TwoTwo == 1:
		print ("------Question Three-----")
		print ("what color do you prefer")
		print ("1.Orange")
		print ("2.Black")
		global TwoTwoOne
		TwoTwoOne = int (input("enter a number 1-2"))
	if TwoTwo == 2:
		print ("------Question Three-----")
		print ("which ability do you want your dragon to have")
		print ("1.Ecolocation")
		print ("2.Electrokenisis")
		global TwoTwoTwo
		TwoTwoTwo = int (input("enter a number 1-2"))
	if TwoTwo ==3:
		print ("------Question Three-----")
		print ("What do you want your dragons weakness to be")
		print ("1.water")
		print ("2.Dragon Root having a longer effect tahn usual")
		global TwoTwoThree
		TwoTwoThree = int (input ("enter a number 1-2"))
def QuestionThreeMystery (TwoThree):
	if TwoThree == 1:
		print ("------Question Three-----")
		print ("what natural dragon habitat do you think is best")
		print ("1.Caves")
		print ("2.Caverns")
		global TwoThreeOne
		TwoThreeOne = int (input("enter a number 1-2"))
	if TwoThree == 2:
		print ("------Question Three-----")
		print ("Do you want your dragon to be a ")
		print ("1.Lone Survivor")
		print ("2. A memmber of a dragon pack ")
		global TwoThreeTwo
		TwoThreeTwo = int (input("enter a number 1-2"))
	if TwoThree == 3:
		print ("------Question Three-----")
		print ("what size")
		print("1.Large")
		print("2.Medium")
		global TwoThreeThree
		TwoThreeThree = int (input("enter a number 1-2"))
	if TwoThree == 4:
		print ("------Question Three-----")
		print ("which real life animal do you prefer")
		print ("1.Butterfly")
		print ("2.Bison")
		global TwoThreeFour
		TwoThreeFour = int (input("enter a number 1-2"))
def QuestionThreeTracker (TwoFour):
	if TwoFour == 1 : 
		print ("------Question Three-----")
		print ("Which animal do you prefer")
		print ("1.Jewel Beetle")
		print ("2.Birds")
		global TwoFourOne
		TwoFourOne = int (input ("enter a number 1-2"))
	if TwoFour == 2:
		print ("-------Question Three-----")
		print ("Do you want your dragon to be a expert at")
		print ("1.Stampeding")
		print ("2.Running (enhanced Speed)")
		global TwoFourTwo
		TwoFourTwo = int (input("enter a number 1-2"))
	if TwoFour ==3:
		print ("-------Question Three-----")
		print("Do you want your dragon to be abe to...")
		print ("1.lift a lot of weight")
		print ("2.be able to lift just one rider")
		global TwoFourThree
		TwoFourThree = int (input("enter a number 1-2"))
def QuestionThreeBoulder (TwoFive):
	if TwoFive == 1:
		print ("-------Question Three-----")
		print("what do you want your dragons natural nature to be")
		print ("1.Reclusive at first but Loyal when they get to know you")
		print ("2.Friendly to anyone, unless they know you are a threat")
		global TwoFiveOne
		TwoFiveOne = int (input("enter a number 1-2"))
	if TwoFive == 2:
		print ("-------Question Three-----")
		print ("what color do you want your dragon to be")
		print ("1.Reddish Brown")
		print ("2.Grey and green")
		global TwoFiveTwo
		TwoFiveTwo = int (input ("enter a number 1-2"))
def QuestionThreeSharp (TwoSix):
	if TwoSix == 1:
		print ("-------Question Three-----")
		print ("do you want your dragons design to be")
		print ("1.Inspired off multiple other dragon species")
		print ("2.or a dinosaur (baryonyx)")
		global TwoSixOne
		TwoSixOne = int(input("enter a number 1-2"))
	if TwoSix == 2:
		print ("-------Question Three-----")
		print ("what color do you want your dragon to be")
		print ("1.Woody brown with a lighter underbelly")
		print ("2.Silver")
		global TwoSixTwo
		TwoSixTwo = int (input ("enter a number 1-2"))
def QuestionThreeTidal (TwoSix):
	if TwoSeven == 1:
		print ("------Question Three-------")
		print ("what color do you want your dragon to be")
		print ("1.Blue")
		print ("2.Purple")
		global TwoSevenOne
		TwoSevenOne = int (input("enter a number 1-2"))
	if TwoSeven ==2 :
		print ("-------Question Three-----")
		print ("what feature do you want your dragon to have")
		print ("1.Expandable Mouth")
		print ("2.Two Pairs of wings")
		global TwoSevenTwo
		TwoSevenTwo = int (input("enter a number 1-2"))
def AnswerStoker (TwoOneOne,TwoOneTwo):
	if TwoOneOne == 1:
		print("------Answer-----")
		print ("YOU GOT A .....HobbleGrunt")
		print ("More sensitive than most other Stoker Class Dragons, it changes color depending on its mood: ")
		print ("Yellown means happy, purple means curious, and red means... RUN!The Hobblegrunt will take on anything its opponent dishes out in combat, and then will dish it right back! ")
	if TwoOneOne == 2:
		print("------Answer-----")
		print ("YOU GOT A.....Monstrous Nightmare")
		print("The Monstrous Nightmare is a Stoker Class dragon, considered to be one of the most aggressive, powerful, and stubborn species of dragons known to Vikings.")
	if TwoOneTwo == 1:
		print("------Answer-----")
		print ("YOU GOT A.....Typhoomerang")
		print ("Famously over-dramatic, this insecure Stoker Class Dragon is known for a spinning Flaming Cyclone maneuver in battle.... ")
		print("and courtship! The Typhoomerang whirls into action and defeats foes by breathing streams of fire. ")
	if TwoOneTwo == 2:
		print("------Answer-----")
		Print ("YOU GOT A.....Singetail")
		print ("Fiercely territorial, Singetails don't just breathe fire—they send it blasting out of their jaws, gills and tails.")
def AnswerStrike (TwoTwoOne,TwoTwoTwo,TwoTwoThree):	
	if TwoTwoOne == 1:
		print("------Answer-----")
		print ("YOU GOT A.... Triple Stryke")
		print ("This giant Strike Class Dragon's three tails can slash through its enemies or snake around its prey. When confronted by one, the best thing to do is turn tail and run!")
	if TwoTwoOne == 2:
		print("------Answer-----")
		print ("YOU GOT A.... Triple Stryke")
		print ("This giant Strike Class Dragon's three tails can slash through its enemies or snake around its prey. When confronted by one, the best thing to do is turn tail and run!")
	if TwoTwoTwo == 1:
		print("------Answer------")
		print ("YOU GOT A..... Night Fury")
		print ("Speed: Unknown. Size: Unknown. The unholy offspring of lightning and death itself. Never engage this Dragon. Your only chance, hide and pray it does not find you.")
	if TwoTwoTwo == 2:
		print ("------Answer-----")
		print ("YOU GOT A.... Skrill")
		print ("This elusive creature is highly secretive, it is known to ride lightning bolts. Found only during electrical storms that can shoot bursts of white fire.")
	if TwoTwoThree == 1:
		print ("------Answer-----")
		print ("YOU GOT A.... Skrill")
		print ("This elusive creature is highly secretive, it is known to ride lightning bolts. Found only during electrical storms that can shoot bursts of white fire.")
	if TwoTwoThree == 2:
		print("------Answer------")
		print ("YOU GOT A..... Night Fury")
		print ("Speed: Unknown. Size: Unknown. The unholy offspring of lightning and death itself. Never engage this Dragon. Your only chance, hide and pray it does not find you.")
def AnswerMystery (TwoThreeOne,TwoThreeTwo,TwoThreeThree,TwoThreeFour):
	if TwoThreeOne == 1:
		print("-----Answer-----")
		print ("YOU GOT A..... ArmorWing")
		print ("With its welding torch-like flames and chain-whip tail the Armor Wing keeps enemies at bay long enough")
		print ("or it to attract new scraps of metal to its magnetic body and fuse them into an ever-expanding coat of armor.")
	if TwoThreeOne == 2:
		print ("------Answer-----")
		print ("YOU GOT A .....Hideous Zippleback")
		print ("Gas + Spark = BOOM! This tricky and evasive 2-headed Mystery Class Dragon is double trouble .")
	if TwoThreeTwo == 1:
		print ("-------Answer-----")
		print ("YOU GOT A.....Boneknapper")
		print ("Even the toughest of dragons need protecting every now and then. ")
	if TwoThreeTwo == 2:
		print ("-------Answer-----")
		print ("YOU GOT A.....Dramillion")
		print ("Although normally withdrawn and wary of humans, Dramillions mimic the fire blast of any dragon they encounter. ")
	if TwoThreeThree == 1:
		print ("------Answer-------")
		print ("YOU GOT A.....Snaptrapper")
		print ("While as beautiful and serene as an exotic flower upon first blush, ")
		print("the four-headed Snaptrapper is actually one of the most insidious and deadly dragons ever discovered.")
	if TwoThreeThree == 2:
		print ("-------Answer-------")
		print ("YOU GOT A...... Changewing")
		print ("This Mystery Class elusive expert in camouflage can shoot hot corrosive acid that can burn through wood and rock (and Vikings!).")
	if TwoThreeFour == 1:
		print ("-------Answer------")
		print ("YOU GOT A.....Death Song")
		print ("The Death Song is a Mystery Class dragon It is regarded as one of the deadliest and most beautiful species of dragon,")
	if TwoThreeFour == 2:
		print ("------Answer------")
		print ("YOU GOT A.....Buffalord")
		print ("Although it's been hunted to near extinction, the benevolent Buffalord holds the only cure to the lethal disease known as The Scourge of Odin.")
def TrackerAnswer (TwoFourOne,TwoFourTwo,TwoFourThree):
	if TwoFourOne == 1:
		print("-----Answer-----")
		print ("YOU GOT A..... Runblehorn")
		print ("A Rumblehorn’s nose knows! From the Tracker Class, it can follow the faintest scent anywhere")
	if TwoFourOne == 2:
		print ("------Answer-----")
		print ("YOU GOT A .....Deadly Nadder")
		print ("The Deadly Nadder is a Tracker Class (formerly Sharp Class) dragon, which is said to be one of the most beautiful dragon ")
		print ("It is well known for its venomous and painful spines")
	if TwoFourTwo == 1:	
		print ("-------Answer-----")
		print ("YOU GOT A.....Thunderclaw")
		print ("Members of this Tracker Class breed form running, rumbling herds very easily. ")
	if TwoFourTwo == 2:
		print ("-------Answer-----")
		print ("YOU GOT A.....Deadly Nadder")
		print ("The Deadly Nadder is a Tracker Class (formerly Sharp Class) dragon, which is said to be one of the most beautiful dragon ")
		print ("It is well known for its venomous and painful spines")
	if TwoFourThree == 1:
		print ("------Answer-------")
		print ("YOU GOT A..... Runblehorn")
		print ("A Rumblehorn’s nose knows! From the Tracker Class, it can follow the faintest scent anywhere")
	if TwoFourThree == 2:
		print ("-------Answer-------")
		print ("YOU GOT A.....Thunderclaw")
		print ("Members of this Tracker Class breed form running, rumbling herds very easily. ")
def BoulderAnswers (TwoFiveOne,TwoFiveTwo):
	if TwoFiveOne == 1:
		print ("-------Answer------")
		print ("YOU GOT A....Catastrophic Quaken")
		print ("The Catastrophic Quaken can smash into the ground and create huge shockwaves that can knock dragons out air.")
	if TwoFiveOne == 2:
		print ("-------Answer------")
		print ("YOU GOT A....Gronckle")
		print ("With its bulbous shape, tiny wings and laid-back demeanor, the wart hoggish Gronckle is proving to be a fan favorite.")
	if TwoFiveTwo == 1:
		print ("------Answer-----")
		print ("YOU GOT A...HotBurple")
		print ("The Hotburple can be a hot mess. Literally! A louder, fussier and lazier Boulder Class cousin to the Gronckle. A nap is never too far away.")
		print ("The slow Hotburple is anything but lazy when it comes to battle. Opponents will have trouble getting out of its way! ")
	if TwoFiveTwo == 2:
		print ("------Answer-----")
		print ("YOU GOT A....Sentinel")
		print ("Although Sightless the Sentinels Keep a close watch over the isle of Vanahiem.Often mistaken for stone statues the sentinels stay still while allowing dragons enter Vanahiem")
		print ("But the second they sense an intruders presence they use their multiple abilites such as sonic screeches and the ability to counter most dragon")
		print ("attacks to save their home")
def SharpAnswer (TwoSixOne,TwoSixTwo):
	if TwoSixOne == 1:
		print ("------Answer-----")
		print ("YOU GOT A....Timberjack ")
		print ("Timberjack. This gigantic creature has razor sharp wings that can slice through full grown trees. Extremely dangerous")
	if TwoSixOne == 2:
		print ("------Answer-----")
		print ("YOU GOT A....Razorwhip")
		print ("Razorwhip. Sharp Class dragon. Long, spiny, barbed tail. Very aggressive. Very dangerous. It can use its tail to wrap around a victim ")
		print ("and literally squeeze the life out of them. Unless it's in a hurry. Then it just slices you in half.")
	if TwoSixTwo == 1:
		print ("------Answer-----")
		print ("YOU GOT A....Timberjack ")
		print ("Timberjack. This gigantic creature has razor sharp wings that can slice through full grown trees. Extremely dangerous")
	if TwoSixTwo == 2:
		print ("------Answer-----")
		print ("YOU GOT A....Razorwhip")
		print ("Razorwhip.Sharp Class dragon. Long, spiny, barbed tail. Very aggressive. Very dangerous. It can use its tail to wrap around a victim ")
		print ("and literally squeeze the life out of them. Unless it's in a hurry. Then it just slices you in half.")
def TidalAnswer (TwoSevenOne,TwoSevenTwo):
	if TwoSevenOne == 1:
		print ("------Answer------")
		print ("YOU GOT A....Thunderdrum")
		print ("When startled, the Thunderdrum will produce a concussive sound wave that can kill a man at close range. Extremely dangerous,")
	if TwoSevenOne == 2:
		print ("------Answer------")
		print ("YOU GOT A....Thunderdrum")
		print ("When startled, the Thunderdrum will produce a concussive sound wave that can kill a man at close range. Extremely dangerous,")	
	if TwoSevenTwo == 1:
		print ("------Answer------")
		print ("YOU GOT A....Thunderdrum")
		print ("When startled, the Thunderdrum will produce a concussive sound wave that can kill a man at close range. Extremely dangerous,")
	if TwoSevenTwo == 2:
		print ("------Answer------")
		print ("YOU GOT A....Thunderdrum")
		print ("When startled, the Thunderdrum will produce a concussive sound wave that can kill a man at close range. Extremely dangerous,")
intro ()
Questions()
QuestionTwo(answerOne)
QuestionThreeStoker(twoOne)
QuestionThreeStrike (TwoTwo)
QuestionThreeMystery (TwoThree)
QuestionThreeTracker (TwoFour)
QuestionThreeBoulder (TwoFive)
QuestionThreeSharp (TwoSix)
QuestionThreeTidal(TwoSeven)
AnswerStoker (TwoOneOne,TwoOneTwo)
AnswerStrike(TwoTwoOne,TwoTwoTwo,TwoTwoThree)
AnswerMystery(TwoThreeOne,TwoThreeTwo,TwoThreeThree,TwoThreeFour)
TrackerAnswer (TwoFourOne,TwoFourTwo,TwoFourThree)
BoulderAnswers (TwoFiveOne,TwoFiveTwo)
SharpAnswer (TwoSixOne,TwoSixTwo)
TidalAnswer (TwoSevenOne,TwoSevenTwo)


	
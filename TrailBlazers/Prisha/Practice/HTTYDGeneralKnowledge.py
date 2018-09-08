choices=10
def intro ():
    name=input (print ("what is your name"))
    print ("in this quiz i will ask you general questions about a specific httyd dragon species")
    choices= int (input ("here are your choices: 1.Deadly Nadder 2.Dramillion 3.Monstrous Nightmare"))
def deadlyNadder (choices):
    DeadlyNadderScore  = 0
    DeadlyNadderScore = int (DeadlyNadderScore)
    print ("------Question One------")
    print ("what fire type does the Deadly Nadder have")
    print ("1.Plasma Blasts")
    print ("2.Flaming Rock Missiles")
    print ("3.Magnesium Blasts")
    print ("4.Icy Blasts")
    OneOne = int (input("enter a number"))
    if OneOne == 3:
        print ("Hooray Magnesium Blast is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Two------")
    print ("in appearance the Deadly Nadder is very beatiful and...")
    print ("1.Crocodile like")
    print("2.Bird Like")
    print ("3.Fish Like")
    print ("4.Scorpion Like")
    OneTwo = int (input("enter a number"))
    if OneTwo == 2:
        print ("Hooray Bird Like is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Three------")
    print ("What is the nadders natural Habitat")
    print ("1.the middle of the ocean")
    print("2.Dark Deep")
    print ("3.Woods")
    print ("4.Temperate Rainforests")
    OneThree = int (input("enter a number"))
    if OneThree == 4:
        print ("Hooray Temperate Rainforests is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Four------")
    print ("After eating what does a deadly nadders Speed increase")
    print ("1.Fish")
    print("2.Chicken")
    print ("3.Eels")
    print ("4.smaller dragons")
    OneFour = int (input("enter a number"))
    if OneFour ==2 :
        print ("Hooray Chicken is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Five------")
    print ("Complete this sentence: Before Fireworms were added to the franchise Deadlt Nadders had the ____ Fire")
    print ("1.Coldest")
    print("2.Hottest")
    print ("3.Prettiest")
    print ("4.Orangey-est")
    OneFive = int (input("enter a number"))
    if OneFive == 2 :
        print ("Hooray Hottest is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Six------")
    print ("What is one thing the Dragon Hunters use a Deadly Nadders spines for")
    print ("1.to make spears")
    print("2.to create Nadder Venom")
    print ("3.to cut vegetables")
    print ("4.They do nothing with the spines")
    Onesix = int (input("enter a number"))
    if Onesix == 1:
        print ("Hooray Dragons hunters do use nadder spines to make spears")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question seven------")
    print ("what is a Nadders favorite activity")
    print ("1.Fetch")
    print("2.catch")
    print ("3.Hopschotch")
    print ("4.Darts")
    OneSeven = int (input("enter a number"))
    if OneSeven == 1:
        print ("Hooray Fetch is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question eight------")
    print ("What changes occor when an adult Deadly Nadder becomes a titan")
    print ("1.Broader Snout")
    print("2.Dark Blue spots on their wings")
    print ("3.More Spikes all around their body")
    print ("4.All of the above")
    OneEight = int (input("enter a number"))
    if OneEight == 4:
        print ("Hooray all of the above is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Nine------")
    print ("when alarmed what does a Deadly Nadder do to intimidate a foe")
    print ("1.use his/her magnesium blast")
    print("2.shoot their spines upwards")
    print ("3.Jump on thier enemy")
    print ("4.all of the above")
    OneNine = int (input("enter a number"))
    if OneNine == 2:
        print ("Hooray shooting their spines upwards is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Ten------")
    print ("What is one possible reason why Deadly Nadder have a Blind Spor")
    print ("1.They cant see directly in front")
    print("2.They have a Huge nasal horn that blocks their view")
    print ("3.Every dragon had a blind spot there")
    print ("4.All of the Above")
    OneTen = int (input("enter a number"))
    if OneTen == 2:
        print ("Hooray 2 is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
    print (" Final score",DeadlyNadderScore,"/10")
def Dramillion (choices):
    DramillionScore  = 0
    DramillionScore = int (DrammilionScore)
    print ("------Question One------")
    print ("what color is the this dragons natural fire")
    print ("1.pink and  orange")
    print ("2.Yellow and Pink")
    print ("3.yellow and purple")
    print ("4.Green and Red")
    TwoOne = int (input("enter a number"))
    if TwoOne == 3:
        print ("Hooray Yellow and Purple is the correct answer!!!")
        DramillionScore = DrammilionScore +1
        print ("Current score:",Dramillionscore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",Dramillionscore,"/10")
    print ("------Question Two------")
    print ("Drammilions are very agressive and territorial if they are...")
    print ("1.Killing something")
    print("2.looking for something")
    print ("3.Protecting something")
    print ("4.All of the above")
    TwoTwo = int (input("enter a number"))
    if TwoTwo == 2:
        print ("Hooray Bird Like is the correct answer!!!")
        Dramillionscore = DrammilionScore +1
        print ("Current score:",DrammilionScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DramillionScore,"/10")
    print ("------Question Three------")
    print ("What is the nadders natural Habitat")
    print ("1.the middle of the ocean")
    print("2.Dark Deep")
    print ("3.Woods")
    print ("4.Temperate Rainforests")
    OneThree = int (input("enter a number"))
    if OneThree == 4:
        print ("Hooray Temperate Rainforests is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Four------")
    print ("After eating what does a deadly nadders Speed increase")
    print ("1.Fish")
    print("2.Chicken")
    print ("3.Eels")
    print ("4.smaller dragons")
    OneFour = int (input("enter a number"))
    if OneFour ==2 :
        print ("Hooray Chicken is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Five------")
    print ("Complete this sentence: Before Fireworms were added to the franchise Deadlt Nadders had the ____ Fire")
    print ("1.Coldest")
    print("2.Hottest")
    print ("3.Prettiest")
    print ("4.Orangey-est")
    OneFive = int (input("enter a number"))
    if OneFive == 2 :
        print ("Hooray Hottest is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Six------")
    print ("What is one thing the Dragon Hunters use a Deadly Nadders spines for")
    print ("1.to make spears")
    print("2.to create Nadder Venom")
    print ("3.to cut vegetables")
    print ("4.They do nothing with the spines")
    Onesix = int (input("enter a number"))
    if Onesix == 1:
        print ("Hooray Dragons hunters do use nadder spines to make spears")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question seven------")
    print ("what is a Nadders favorite activity")
    print ("1.Fetch")
    print("2.catch")
    print ("3.Hopschotch")
    print ("4.Darts")
    OneSeven = int (input("enter a number"))
    if OneSeven == 1:
        print ("Hooray Fetch is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question eight------")
    print ("What changes occor when an adult Deadly Nadder becomes a titan")
    print ("1.Broader Snout")
    print("2.Dark Blue spots on their wings")
    print ("3.More Spikes all around their body")
    print ("4.All of the above")
    OneEight = int (input("enter a number"))
    if OneEight == 4:
        print ("Hooray all of the above is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Nine------")
    print ("when alarmed what does a Deadly Nadder do to intimidate a foe")
    print ("1.use his/her magnesium blast")
    print("2.shoot their spines upwards")
    print ("3.Jump on thier enemy")
    print ("4.all of the above")
    OneNine = int (input("enter a number"))
    if OneNine == 2:
        print ("Hooray shooting their spines upwards is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
        print ("Current score:",DeadlyNadderScore,"/10")
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
        print ("Current score:",DeadlyNadderScore,"/10")
    print ("------Question Ten------")
    print ("What is one possible reason why Deadly Nadder have a Blind Spor")
    print ("1.They cant see directly in front")
    print("2.They have a Huge nasal horn that blocks their view")
    print ("3.Every dragon had a blind spot there")
    print ("4.All of the Above")
    OneTen = int (input("enter a number"))
    if OneTen == 2:
        print ("Hooray 2 is the correct answer!!!")
        DeadlyNadderScore = DeadlyNadderScore +1
    else:
        print ("OH No!!! Thats the wrong answer better luck next time")
    print (" Final score",DeadlyNadderScore,"/10")
intro()
deadlyNadder(choices)
    
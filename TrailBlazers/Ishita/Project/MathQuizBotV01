import random

# This is for people who need help.
def help():
    print(" Okay! That's alright!")
    b = ("What is you best friends name?")
    print("Addition is basically the adding of two quantities together. Like if you have 5 apples and", b , " gave you 2 more, you now have 7 apples.! You can easily draw that by making the number the sticks. ")
    print("Subtraction is the opposite of addition.When ", b, "gave you 2 apples and you had 5 apples, you have 7. Let's say", b, "comes back and asks you for 1 apple. You had 7 but you gave her 1 , you have 6. You can also do that by sticks.")
    print(" Multiplication is repeated addition. 7 * 2 = 7 plus 7 (You are doing 7 + 2 times). You can also do this by sticks. A bundle of 7 sticks. And we have 2 bundles. SO the total sticks we have is 14. ")
    print("For subtraction, when doing like 3 - 4, switch the order = 4-3. The answer is 1 right? No. We must add a negative to the 1 to show that the number is smaller.  ")
    print("You can always scroll up for reference of this. ")
    c = input("Ready?")
    levelone()

# This basically is the number of wrongs there is.


w = 0 
# This function does the checking process. 
def check_results_and_get_them(actualanswer):
    answerinput= int(input(""))
    if answerinput == actualanswer:
        print("Yup!")
        wake = input("Ready to go on?")
    else:
        print("Nope")
        print("The correct answer is :")
        print(actualanswer)
        wake = input("Ready to on?")
        global w
        w = w +1
        

def levelone():
    print("______________________________________Level 1 ________________________________________________________")
    #basic level 1
    
    print("Well, hi! This level is basic - it teaches you your facts till 100.")
   
    print("----------------Addition--------------------")
    # Addition(Tests on it)
  
    for i in range(0,100):
        
        rand= int(random.randint(0,10)) 
        rand_two= int(random.randint(0,10))
        # Two random numbers to answer with. 
        
        actualanswer = rand + rand_two
        print(rand, "+",rand_two, "=?")
        #Prints question.
        
        check_results_and_get_them(actualanswer)
        #This checks if the answer is right or if not, adds 1 to w. 
        
            
    print("On to - Multiplication!")
    print("--------------------Multiplication-----------------------")
        
    print("Remeber- Repeated addition- Go ahead and actually do it like that.")
    for i in range(0,100):
         
        rand = int(random.randint(0,10))
        rand_two = int(random.randint(0,10))
    
        actualanswer  = rand * rand_two
        print( rand, "*", rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
        
        
    print("Whew! Just a bit more - to subtraction.")
    
    print("--------------------Subtraction---------------")
        
    print("Subtraction is the opposite of addition.")
    print("5+3 = 8 and 8- 3 +5 and 8 - 5 =3 ")
    
    for i in range (0,100):
         
        rand= int(random.randint(0,10))
        rand_two= int(random.randint(0,10))
        
        if rand > rand_two:
        
            actualanswer= rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            
            check_results_and_get_them(actualanswer)
            answerinput_one = int(input(" "))
    
        if rand < rand_two:
            
            print("Trick question:")
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
            
            
            
    if w >= 5:
        print("I'm sorry, we must do this level again.")
        print("Because you had ", w , "wrong.")
        levelone()
    
    
    if w < 5:        
        print("Well dear, good job and well done. Let us move on to the second level! Yes!")
        leveltwo()

def leveltwo ():
    print("----------------------------level 2------------------------------------------------------------------------------")
    
    print("This level tests your facts till 100. Here we go! ")
    
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(10,100))
        rand_two= int(random.randint(10,100))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
        


    print("--------------------Multiplication-----------------------")
    for i in range(0,50):
        
         
        rand = int(random.randint(10,100))
        rand_two = int(random.randint(10,100))
    
        actualanswer  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
        
        
        
    print("--------------------Subtraction---------------")        
    for i in range (0,100):
        
         
        rand= int(random.randint(10,100))
        rand_two= int(random.randint(10,100))
        
        if rand > rand_two:
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
            print(w)
    
        if rand < rand_two:
            print("Trick question:")
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
            
    if w >= 5:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        leveltwo()
        
    if w < 5:
        print("Well done! Masters of Mathematics! You are now in level 3!")
        levelthree_four_five()
    
    

def levelthree_four_five():
    print("---------------------------------------------Level 3 ----------------------------------------------------")    
    
    

    # We do 1000 for 3 levels to make next levels easy.
    print("To a 1000! You will have to do this for a couple levels... ")
    
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(100,1000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        
        check_results_and_get_them(actualanswer)


    for i in range(0,10):
        print("--------------------Multiplication-----------------------")
         
        rand = int(random.randint(100,1000))
        rand_two = int(random.randint(100,1000))
    
        actualanswer  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
        
            
    for i in range (0,100):
        print("--------------------Subtraction---------------")
         
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(100,1000))
        
        if rand > rand_two:
        
                answer_two = rand - rand_two
                print(rand, "-", rand_two, "=?")
                 
                check_results_and_get_them(actualanswer)
    
    
                if rand < rand_two:
                    print("Trick question:")
        
                    answer_two = rand - rand_two
                    print(rand, "-", rand_two, "=?")
                    
                    check_results_and_get_them(actualanswer)
                    
    
        print("All right! Arsonist of Arithemetic! You are officialy in level 4 .")
    
    print("--------------------------------------Level 4 -------------------------------------------------")
    
    
    
    print("I know its hard- but that's why we re doing it. Sharpen your pencils! ")
    
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(0,1000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        
        check_results_and_get_them(actualanswer)

    print("--------------------Multiplication-----------------------")
    for i in range(0,10): 
    
         
        rand_five = int(random.randint(100,1000))
        rand_six = int(random.randint(100,1000))
    
        actualanswer  = rand_five * rand_six
    
        print( rand_five, "*", rand_six, "=?")
        
        check_results_and_get_them(actualanswer)
        
        print("--------------------Subtraction---------------")    
    for i in range (0,100):
        
    
         
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(100,1000))
        
        if rand > rand_two:
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
            
    
    print(" Astonishing! Magician of Multipliction, supervisor in subtraction and amazing at addition! Level 5!")
     
    print("-----------------------------------------Level 5 --------------------------------------------------------")
    
   

    print("Last one in a 1000. It was important because it will help you build up. ")

    for i in range(0,100):
        print("----------------Addition--------------------")
        
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(100,1000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)

    for i in range(0,10):
        print("--------------------Multiplication-----------------------")
    
         
        rand_five = int(random.randint(100,1000))
        rand_six = int(random.randint(100,1000))
    
        answer_one  = rand_five * rand_six
    
        print( rand, "*", rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
        
            
    for i in range (0,100):
        print("--------------------Subtraction---------------")
    
         
        rand= int(random.randint(100,1000))
        rand_two= int(random.randint(100,1000))
        
        if rand > rand_two:
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            
            check_results_and_get_them(actualanswer)
            
    if w >=15:
        print("I'm soory, we must do these levels again.")
        print("Because you had ", w , "wrong.")
        levelthree_four_five()
    
    if w < 15:
        print("Yup you are smart enough for rocket science! King of Math! Level 6")
        levelsix()
    
def levelsix():
    print("-----------------------------Level 6 -----------------------------------------------------------")
    
    print("Alright - Let's do this! From now on, you will just get another 0 every time.")
    print("Also if you get too many wrong in buildup, you must do it again. ")
    
    w = 0
    
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        
        rand= int(random.randint(1000,10000))
        rand_two= int(random.randint(1000,10000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)
        
    print("--------------------Multipliction-----------------------")

    for i in range(0,10):
        
    
         
        rand = int(random.randint(1000,10000))
        rand_two = int(random.randint(1000,10000))
    
        actualanswer_one  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        
        check_results_and_get_them(actualanswer)
    print("--------------------Subtraction---------------")
        
            
    for i in range (0,100):
         
        rand= int(random.randint(1000,10000))
        rand_two= int(random.randint(1000,10000))
        
        if rand > rand_two:
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            actualansweranswer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
                
    
    
    if w >=5:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        levelsix()
        
    if w <5:
        print("Wooooo! You got the second badge... Level 7..")
        levelseven()

def levelseven():
    print("===================Level 7 ======================================================================")
    
    
    print("OMG!!!! The second badge - think of this like graduation...")
    
    print("----------------Addition--------------------")
    
    for i in range(0,100):
        
        
        rand= int(random.randint(10000,100000))
        rand_two= int(random.randint(10000,100000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)
    print("--------------------Multiplication-----------------------")

    for i in range(0,10):
        
    
         
        rand = int(random.randint(10000,100000))
        rand_two = int(random.randint(10000,100000))
    
        actualanswer = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        check_results_and_get_them(actualanswer)
        
            
    for i in range (0,50):
    
        print("--------------------Subtraction---------------")
    
         
        rand= int(random.randint(10000,100000))
        rand_two= int(random.randint(10000,100000))
        
        if rand > rand_two:
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
    
    
            if rand < rand_two:
                print("Trick question:")
        
                answer_two = rand - rand_two
                print(rand, "-", rand_two, "=?")
                check_results_and_get_them(actualanswer)
                
    if w >=10:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        levelseven()
        
    if w < 10:
        print("Nice job! You are now an emporer instead of king! Level 8!")
        leveleight()
    
def leveleight():    
    print("===================================Level 8 =================================================")
    
    print("This is going to get harder... Stretch and sit straight! Let's go.")
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(100000,1000000))
        rand_two= int(random.randint(100000,1000000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)

    print("--------------------Multiplication-----------------------")
    for i in range(0,10):
         
        rand = int(random.randint(100000,1000000))
        rand_two = int(random.randint(100000,1000000))
    
        actualanswer  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        check_results_and_get_them(actualanswer)
        
    print("--------------------Subtraction---------------")     
    for i in range (0,50):
         
        rand= int(random.randint(100000,1000000))
        rand_two= int(random.randint(100000,1000000))
        
        if rand > rand_two:
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
            
    if w >= 12:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        leveleight()
        
    if w< 12:
        print("Incredible! Let us move on to ..... Level 9!")
        levelnine()

def levelnine():
    print("=================================Level 9 =======================================================")
    
    print("Almost to the end!!!!")
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(1000000,10000000))
        rand_two= int(random.randint(1000000,10000000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)

    print("--------------------Multiplication-----------------------")
    for i in range(0,10):
         
        rand = int(random.randint(1000000,10000000))
        rand_two = int(random.randint(1000000,10000000))
    
        actualanswer= rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        check_results_and_get_them(actualanswer)
        
    print("---------------Subtraction ------------------------------------")        
    for i in range (0,50):
         
        rand= int(random.randint(1000000,10000000))
        rand_two= int(random.randint(1000000,10000000))
        
        if rand > rand_two:
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            answer_two = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
            
    if w >= 13:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        levelnine()
        
    if w < 13:
        print("OMG! You are in the last and final level. It will test you like no other. Into Billions. Level 10!!")
        levelten()

def levelten ():
    print("===================================Level 10 ===================================================")
    
    print("Take a breath! It will challenge you. ")
    
    print("----------------Addition--------------------")
    for i in range(0,100):
        
        rand= int(random.randint(0,1000000000))
        rand_two= int(random.randint(0,1000000000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        check_results_and_get_them(actualanswer)



    print("--------------------Multiplication-----------------------")
    for i in range(0,10):
         
        rand = int(random.randint(0,1000000000))
        rand_two = int(random.randint(0,1000000000))
    
        actualanswer  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        check_results_and_get_them(actualanswer)
        
        
    print("--------------------Subtraction---------------")        
    for i in range (0,50):
    
         
        rand= int(random.randint(0,1000000000))
        rand_two= int(random.randint(0,1000000000))
        
        if rand > rand_two:
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            check_results_and_get_them(actualanswer)
            
    if w >=15:
        print("I'm soory, we must do this level again.")
        print("Because you had ", w , "wrong.")
        levelten()
        
        
    if w < 15:
        print("You have now reached! The medal of honor. Good job! Best!")
        print("============================The end============================================================")
        z = input("Now that you have reached the end, you can come back later or you can try the hard version: B for exit, Hard for the hard level or you can complete a test to make sure you can do the hard level.TEST is for that. ")
    
        if z == "B":
            print("Visit again soon. Bye")
            exit
            
        if z == "TEST":
            print("Alright!!!")
            print("This is a test from level 1 to level 10. ")
            test()

        
        if z == "Hard":
        
            print("Alright, then! This one never ends so you just exit any time. Good job BTW.")
            hardlevel()



y = 0
def checkprocess(actualanswer):
    if answerinput == actualanswer:
        print("Yup!")
        wake = input("Ready to go on?")
    else:
        print("Nope")
        print("The correct answer is :")
        print(actualanswer)
        wake = input("Ready to on?")
        y = y+1 

def test() :
    
    print("This test doesn't test you into billions. Just a little less. But yoy must do a 100 of each problem. ")
    print("----------------Addition--------------------")
    
    
    
    for i in range(0,100):
        
        rand= int(random.randint(0,100000))
        rand_two= int(random.randint(0,10000))
        
        actualanswer = rand + rand_two
    
        print(rand, "+",rand_two, "=?")
        
        answerinput= int(input(""))
        
        checkprocess(actualanswer)
    


    print("--------------------Multiplication-----------------------")
    for i in range(0,10):
         
        rand = int(random.randint(0,1000))
        rand_two = int(random.randint(0,1000))
        actualanswer  = rand * rand_two
    
        print( rand, "*", rand_two, "=?")
        checkprocess(actualanswer)
        
        
    print("--------------------Subtraction---------------")        
    for i in range (0,50):
    
         
        rand= int(random.randint(0,10000))
        rand_two= int(random.randint(0,100000))
        
        if rand > rand_two:
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            checkprocess(actualanswer)
    
    
        if rand < rand_two:
            print("Trick question:")
        
            actualanswer = rand - rand_two
            print(rand, "-", rand_two, "=?")
            checkprocess(actualanswer)
    
def hardlevel():
        
        y = 1000000000
        while True:
            
            y*10
            
            print("Take a breath! It will challenge you. ")
    
            for i in range(0,5):
                print("----------------Addition--------------------")
                
                rand= int(random.randint(0,y))
                rand_two= int(random.randint(0,y))
        
                actualanswer = rand + rand_two
    
                print(rand, "+",rand_two, "=?")
                check_results_and_get_them(actualanswer)


            for i in range(0,5):
                print("--------------------Multiplication-----------------------")
    
                 
                rand = int(random.randint(0,y))
                rand_two = int(random.randint(0,y))
    
                actualanswer  = rand * rand_two
    
                print( rand, "*", rand_two, "=?")
                check_results_and_get_them(actualanswer)
        
            
            for i in range (0,2):
    
                print("--------------------Subtraction---------------")
    
                 
                rand= int(random.randint(0,y))
                rand_four= int(random.randint(0,y))
        
                if rand > rand_four:
        
                    answer_two = rand - rand_two
                    print(rand, "-", rand_two, "=?")
                    check_results_and_get_them(actualanswer)
    
                if rand < rand_four:
                    print("Trick question:")
        
                    answer_two = rand - rand_four
                    print(rand, "-", rand_two, "=?")
                    check_results_and_get_them(actualanswer)
                    
            if w >= 5 :
                print("Sorry, must repeat this level. ")
                w=0
                
            if w < 5:    
                w = 0
                y = y *10    

print("Hello, I am math. You can practice math (arithmetic) with me.")
print("If you want to try this out, you must know how to work with negtive numbers and know how to add and subtract and multiply, fairly well.")

experiece=input("Have you been here before? Enter no or yes.")

if experiece == "no" :
    
    print("Well, hello there!")
    print("\nThis is a program that helps you to polish your arithmetic(not division).")
    a = input(" Need help? Write' help")
    
    if a == "help":
        print("That's okay! ")
        
        help()
    levelone()
    
if experiece == "yes":
    print("Remember: 1 is one, 2 is two, 3 is three 6 is six, 7 is seven, 8 is eight, 9 is nine, 10 is ten.")
    print("If you did level 4 or 5, we will just start at level three(so write level three)")
    print("Also, if you went to the hard level after 10, just start at 10 for review.")
    print("If you need help, write 'help' ")
    level = input ("Which level have you stopped at? only letters...   ")
    if level == "one":
        levelone()
    if level == "two":
        leveltwo()
    if level == "three":
        levelthree_four_five()
    if level == "six":
        levelsix()
    if level == "seven":
        levelseven()
    if level == "eight":
        leveleight()
    if level == "nine":
        levelnine()
    if level == "ten":
        levelten()
    if level == "help":
        print(" So you need help, that's okay! ")
        help()
    

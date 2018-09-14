import random
import sys
def rps():
    cpoints = 0
    upoints = 0
    operations = ("Rock","Paper","Scissors")
    canswer = random.choice(operations)
    uanswer = (input("Hi, Enter 1 for Rock, 2 for Scissors, and 3 for Paper. Enter 4 to exit:"))
    if canswer == "Rock":
        if uanswer == '1':
            print("I choose",canswer,". Haha! It is a tie I see! Both of us win this time, but your luck is running out! ")
        elif uanswer == '2':
            print("I choose",canswer,". LOSER! I win! HA HA HA HA HA! ")
        elif uanswer == '3':
            print("I choose ",canswer,". Ughhh! So what you win *eye roll* It was probably just a stroke of luck!")
        elif uanswer == '4':
            sys.exit("Bye!")
        else:
            sys.exit("Invalid Input. Try again.")
            print(rps())
    elif canswer == "Paper":
        if uanswer == '1':
            print("I choose",canswer,". LOSER! I win! HA HA HA HA HA!")
        elif uanswer == "2":
            print("I choose ",canswer,". Ughhh! So what you win *eye roll* It was probably just a stroke of luck!")
        elif uanswer == "3":
            print("I choose ",canswer,".  Haha! It is a tie I see! Both of us win this time, but your luck is running out! ")
        elif uanswer == '4':
            sys.exit("Bye!")
        else:
            sys.exit("Invalid Input. Try again.")
            print(rps())
    elif canswer == "Scissors":
        if uanswer == '1':
            print("I choose",canswer,". Ughhh! So what you win *eye roll* It was probably just a stroke of luck!")
        elif uanswer == "2":
            print("I choose ",canswer,". Haha! It is a tie I see! Both of us win this time, but your luck is running out! ")
        elif uanswer == "3":
            print("I choose ",canswer,". LOSER! I win! HA HA HA HA HA! ")
        elif uanswer == '4':
            sys.exit("Bye!")
        else:
            sys.exit("Invalid Input. Try again.")
            print(rps())
    play = (input("Would you like to play again? Enter 1 for yes and 2 for no:"))
    if play == '1':
        print(rps())
    elif play == '2':
        sys.exit("Bye!")
    else:
        sys.exit("Invalid input. Have a nice day!")
rps()

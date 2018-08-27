#Let's start writing the Code Skeleton 
#Objective/Goal here is 
#   1. Following the Design
#   2. Write functions, their input parameters and respetive outputs
#   3. Connect these functions to each other.

#Define this as a global variable.
listOfWords = ['skoolofcode', 'horses','redmond','puppies']

def init():
    #Local variables v/s Global Variables
    print("init:Printing listofWorlds",listOfWords)
    return

def about():
    print("Hey! I am a Simplified Hangman. Guess the sceret word and you will win")
    print("You have 3 tries to guess the word!")
    return

def chooseAWord():
    chWord = "Dummy"
    print("Let's print this list of Words", listOfWords)
    #..
    #..
    return chWord

#Main
init()
about()
chooseAWord()





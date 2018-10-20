#Let's start writing the Code Skeleton 
#Objective/Goal here is 
#   1. Following the Design
#   2. Write functions, their input parameters and respetive outputs
#   3. Connect these functions to each other.
#   4. No need to write all code implementation inside the function.

#Define this as a global variable.
listOfWords = ['skoolofcode', 'horses','redmond','puppies']
NrOfTriesByUser = 0

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

# The createAWordWithDashes outputs a word with only the first n characters 
# and rests hideen by dashes. Parameters to this function are 'word' and 'n' 
# which is number of chars to display
def createAWordWithDashes(word,n):
    wordWithDashes = "Dum**"
    #
    #
    #
    return wordWithDashes

#The function getUserGuess displays the word and takes user try as a input. The it
# returns the user try as a result. It increments the number of tries.
def getUserGuess(w):
    print("The hideen word is ",w)
    ret_value = input("Hey user! Guess this word")
    global NrOfTriesByUser
    NrOfTriesByUser = NrOfTriesByUser + 1
    return ret_value

def YouWin():
    print("You have won! Great!")
    return

def YouLoose():
    print("You loose")
    return
    
#Main
init()
about()
word = chooseAWord()

NrofCharShown = 3

while(NrOfTriesByUser!=3):
    wordToDisplay = createAWordWithDashes(word,NrofCharShown)
    userGuess = getUserGuess(wordToDisplay)

    if(userGuess == word):
        YouWin()
        exit()
    
    NrofCharShown = NrofCharShown + 1

YouLoose()
    


#Use the word to display








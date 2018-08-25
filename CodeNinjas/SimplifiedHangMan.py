#Simplified Hangman

#Present a word with only first 3 characters. Rest everything is masked
#The user would be asked to guess the word. He/She wins if the word is correctly guessed.
#A user get a total of 3 tires. At every try a new character is shown.




#Let's have a global word list.
worldList = ["batman","jumpsuit", "tennis","horses","skoolofcode"]

def initWordList():
    lenghtOfWords = 6 #
    
    print("initiWordList : this function initializes the word list")
    # Write the code to initialize the world list
    #...
    #print("initWordList : The world list is ",worldList) 
    print("initWordList : The world list is initialized with word of lenght", lenghtOfWords)

def selectWord():
    word = "dummyy"
    print("selectWord : Selects a word to play with")
    # ...
    # ...
    return word

def creexateWordToDisplay(word,firstN):
    wordFirstN = "dum***"
    print("This function writes out the given word with N characters hideen with *")
    #..
    #..
    #..

    return wordFirstN

def about():
    print("about: This function tells the users what the program does")
    print("Hey user! Welcome to the Hangman. You are now playing a word guessing game")
    print("Guess the word in 3 tries!")
        

#Main
initWordList()

about()

sWord = selectWord()
print("The selected word for this game is ", sWord)

displayWord = createWordToDisplay(sWord,3)
print("User : Guess the word ", displayWord)



    



#Global variables
global_worldList = ["avi","ranvir", "sonakshi","suhas"] 
global_i = 10000   

def initWordList():
    lenghtOfWords = 6 #
    #Local variable to the initWordList funciton
    worldList = ["batman","jumpsuit", "tennis","horses","skoolofcode"] 
    i = 10 
    
    def printGreen():
        color = "green"
        global global_worldList
        print("printGreen : Hey! i can access global and parent scope",color, worldList, global_worldList,lenghtOfWords,i)
        #Why i can't access worldList. Its global for 
        #print("printGreen : print word list", worldList)
    
    printGreen()

    print("initiWordList : this function initializes the word list", worldList)
    print("initWordList : Printing i ",i)

    print("initiWordList: global wordlist ",global_worldList)
    print("initiWordList : Printing global i ", global_i)
    
    print("initWordList : The world list is initialized with word of lenght", lenghtOfWords)

def about():
    #print("about: Let's print the wordlist",worldList)
    #print("about : Printing i ",i)
    print("about: global wordlist ",global_worldList)
    print("about : Printing global i ", global_i)
    #print("about: This function tells the users what the program does")
    #print("Hey user! Welcome to the Hangman. You are now playing a word guessing game")
    #print("Guess the word in 3 tries!")

initWordList()
about()
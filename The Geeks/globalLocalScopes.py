# This is my main or the global scope of the program.
# Let's check that global variable is accessible by all child functions
# Local variables can only be accessed in local scope


black_var = 20

def about():
    green_var = 30
    print("about: Printing black_var green_var",black_var,green_var)

    def yellowFunc():
        print("yellowFunc: Printing my parent's varaibles",green_var)
    
    yellowFunc()

def initWordList():
    print("initWordList: Printing black_var", black_var)

    def greyFunc():
        brown_var = 400
        print("greyFunc : I can access the global scope",black_var)

    greyFunc()

    #print("initiWordList : See that i cannot access my child's variables",brown_var)

about()
initWordList()
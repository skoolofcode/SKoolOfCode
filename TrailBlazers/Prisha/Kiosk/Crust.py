gglobal namelist
namelist={"Test":'Testflavor'}

def NamePickCrust():
    global name
    global OldNew
    print (" this program will now randomly generate a pizza crust for you to use")
    name=input("what is your name???")
    #for item in namelist :
    if name in namelist:
        #print (namelist, name)
        OldNew = input("welcome back would you like a new flavor your previous flavor 1=new 2=old")
    else :
        OldNew  = '1'

#1- Crust        
    
def FlavorPickCrust():
    print (" ------bases----- ")
    a='BBQ sauce'
    b="Pesto" 
    c="Red sauce"
    d="White sauce"
    e="Garlic Rub"



    #Shiv : Consider being very precise.
    #Shiv : Telling about the program should happen first.
    #Shiv : Telling about the program is not the job of this function.
    #Shiv : This function is just about picking your flavor.
    
    
    import random 
    global choice
    choice= random.choice('abcd')


    if 'a'==choice:
        print("BBQ sauce")
    if 'c'==choice:
        print("red sauce")
    if 'b'==choice:
        print ("pesto")
    if 'd'==choice:
        print ("Garlic Rub")
    
    Savingnamecrust(name,choice)
        
def OldFlavorPickCrust (MyChoice):
    print (" ------crust----- ")
    a='BBQ sauce'
    b="Pesto" 
    c="Red sauce"
    d="White sauce"
    e="Garlic Rub"

    if 'a'==choice:
        print("BBQ sauce")
    if 'c'==choice:
        print("red sauce")
    if 'b'==choice:
        print ("pesto")
    if 'd'==choice:
        print ("Garlic Rub")



    
def Savingnamecrust(name,choice):
    #takes name and choice and writes that to a dictionary
    #global namelist
    namelist[name]= choice
    print ("Saving you in our records",namelist)
    
var=1
while var==1:
    print ("----------------Start Processing--------------------")
    NamePickCrust()
    print(OldNew)
    if OldNew == '2':
        myChoice= (namelist[name])
        OldFlavorPickCrust(myChoice)
    if OldNew == '1':
        FlavorPickCrust()


    


    






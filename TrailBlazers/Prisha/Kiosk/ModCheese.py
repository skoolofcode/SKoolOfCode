global namelist
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
    print (" ------Cheese----- ")
    a='Asiago'
    b="Dairy Free Cheese" 
    c="Feta 
    d='Gorgonzola'
    e="Mozerella"
    f="Parmesan"
    g="Riccotta"

    import random 
    global choice
    choice= random.choice('abcd')


    if 'a'==choice:
        print("Asiago")
    if 'b'==choice:
        print("Dairy Free Cheese")
    if 'c'==choice:
        print ("Feta")
    if 'd'==choice:
        print ("Gorgonzola")
    if 'e'== choice:
        print (" Mozerella")
    if "f" == choice
        print ("Paremesan")
    if 'g'==choice
        print ("Riccotta")
    
    
    Savingnamecrust(name,choice)
        
def OldFlavorPickCrust (MyChoice):
    a='Asiago'
    b="Dairy Free Cheese" 
    c="Feta 
    d='Gorgonzola'
    e="Mozerella"
    f="Parmesan"
    g="Riccotta"

    if 'a'==choice:
        print("Asiago")
    if 'b'==choice:
        print("Dairy Free Cheese")
    if 'c'==choice:
        print ("Feta")
    if 'd'==choice:
        print ("Gorgonzola")
    if 'e'== choice:
        print (" Mozerella")
    if "f" == choice
        print ("Paremesan")
    if 'g'==choice
        print ("Riccotta")



    
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


    


    








#SKC : Logic looks good. 
#SKC : Test and Complete the code.
#SKC : Imports are not done and remember input by default get you a string and not a number.

print("Hi! We all know how difficult it is to set up passwords, especially when we want it to be for a secure account. A password which is secure. No worries! I will give you a password and a key number if you ever lose it. Enjoy!")
print("P.S. DOn't worry, I don't hack into your account.")
name = input("What is your name?")

def maker():
    num = input("How many digits would you like in your password.Type in the 'a' the number of characters you want your password to be")

    for i in num:
        a = string.ascii_lowercase
        A = string.ascii_uppercase
        b =random.choice(a)
        B = random.choice(A)
        c = random.randint(0,9)
        d = random.randint(1,3)
        f = random.randint(0,100000)
    
        if d == 1:
            print(b,sep = '', end = '')
        else:
            if d == 2:
                print(B,sep = '', end = '')
            else:
                if d == 3:
                    print(c,sep = '', end = '')
                  
maker()       

satisfaction = int(input("\nDid you like your password?Enter 1 for yes and 2 for no."))

if satisfaction == 1:
    print("I am glad.")
   
else:    
    if satisfaction == 2:
        print(" Uh oh. Let's do it again then.")
        maker()


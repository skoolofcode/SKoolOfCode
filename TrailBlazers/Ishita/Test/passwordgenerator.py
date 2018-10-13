import string
import random
import getpass

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
                    
def store():
    
    password = input("For practice, write your password here.If you had added a few other characters, write them here too. Write the password you used.")
    site = input("Where did you use this password?")
    other = input("Is there any other security measure you want to put?")
    secret = getpass.getpass("Tell me a word that you will remember. This you will use to retrieve your password. ")
    
    file = open('password.txt', 'a')
    file.write("\n\n\n\nName:")
    file.write(name)
    file.write("\nPlace used:")
    file.write(site)
    file.write("\nPassword:")
    file.write(password)
    file.write("\nOther:")
    file.write(other)
    file.write("\nSecretword:")
    file.write(secret)

    print("Done!")


print("Hi! We all know how difficult it is to set up passwords, especially when we want it to be for a secure account. A password which is secure. No worries! I will give you a password and a key number if you ever lose it. Enjoy!")
print("P.S. DOn't worry, I don't hack into your account.")
name = input("What is your name?")
choice = int(input("DO you want to make a new password(1) or store your passwords(2)?"))

if choice == 1:
    maker()
else:
    if choice == 2:
        store()
   
satisfaction = int(input("\nDid you like your password?Enter 1 for yes and 2 for no."))

if satisfaction == 1:
    print("I am glad.")
    store()
else:    
    if satisfaction == 2:
        print(" Uh oh. Let's do it again then.")
        maker()


    

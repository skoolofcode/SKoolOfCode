print("Welcome student to the Hogwarts School of Wizardy. I am the sorting hat.")

g = 0
h = 0
r = 0
s = 0 

print(" Which one do you honor? enter the letter")
print("a) Courage, Bravery, Nerve")
print("b) Hard work, Patience, Jusctice, Loyalty")
print("c) Intelligence, Creativity, Learning, Wit ")
print("d) Ambition, Cunning, Leadership, Resourcefulness")

a = input("")
if a == "a": 
    g = g+1
else:
    if a == " b":
        h = h+1
    else:
        if a == "c":
            r = r+1
        else:
            if a == "d":
                s = s+1

print("Alright, What if one of your friends is hurt by someone. What will you do?")
print("a) Face the person who hurt your friend in a fight.")
print("b) Stay by your friends's side! ")
print("c) Call a teacher ")
print("d) Run!")

b = input("")

if b == "a": 
    g = g+1
else:
    if b == " b":
        h = h+1
    else:
        if b == "c":
            r = r+1
        else:
            if b == "d":
                s = s+1
                
print("Which skill of yours are you most proud of?")
print("a) Bravery")
print("b) Ability to make a lot of friends!")
print("c) Abilty to absorb new information and retention.")
print("d) My ability to get a goal, stick to it and get it.")

d = input("")

if d == "a": 
    g = g+1
else:
    if d == " b":
        h = h+1
    else:
        if d == "c":
            r = r+1
        else:
            if d == "d":
                s = s+1

print("Well, DO you know about the book diveergent and the factions? (If not, skip this by typing n.")
print("Which faction would you choose or did you get in a quiz( I recomend this option.)")
print("a) Dauntless/ Abnigation")
print("b)Amity")
print("c)Erudite")
print("d) A mix of everything really.")

f = input("")

if f == "a": 
    g = g+1
else:
    if f == " b":
        h = h+1
    else:
        if f == "c":
            r = r+1
        else:
            if f == "d":
                s = s+1
        
                    


print("Well, The Sorting Hat takes into consideration what you want to be. So?")
print("a) Griffindor - Bravery")
print("b) Hufflepuff - Niceness")
print("c) Ravenclaw - INtelegence")
print("d) Slythterin - Ambition")

c = input("")

if c == "a": 
    g = g+1
else:
    if c == " b":
        h = h+1
    else:
        if c == "c":
            r = r+1
        else:
            if c == "d":
                s = s+1
                

if g > 3:
    print("Congrats! You got Griffindor")
else:
    if h > 3:
        print("COngrats Hufflepuff!")
    else:
        if r> 3:
            print("Congrats. You got Ravenclaw!")
        else:
            if s > 3:
                print("Yay! Slytherin( DOn't worry it doesn't mean you are evil)")
            else:
                if g > 2:
                    print("Congrats! You got Griffindor")
                else:
                    if h > 2:
                        print("COngrats Hufflepuff!")
                    else:
                        if r> 2:
                            print("Congrats. You got Ravenclaw!")
                        else:
                            if s > 2:
                                print("Yay! Slytherin( DOn't worry it doesn't mean you are evil)")
                    

def randomPassword ():
    import random
    charectars= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars2= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars3= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars4= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars5= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars6= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars7= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars8= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars9= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charectars10= random.choice ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    Passwordlenght= input("how long do you want your password to be (1-10)")
    catchyPhrase = input("what is a catchy phrase that you would remmember?")
    if Passwordlenght == '1' :
        for i in range (0, 1):
            print(catchyPhrase, charectars)
    if Passwordlenght == '2' :
        for i in range (0,1):
            print(charectars,catchyPhrase,charectars2)
    if Passwordlenght == '3' :
        for i in range (0, 1):
            print(charectars, catchyPhrase,charectars2, charectars3)
    if Passwordlenght == '4' :
        for i in range (0, 1):
            print(charectars,charectars2, catchyPhrase,charectars3,charectars4)
    if Passwordlenght == '5' :
        for i in range (0, 1):
            print(charectars,charectars2, catchyPhrase,charectars3,charectars4,charectars5)
    if Passwordlenght == '6' :
        for i in range (0, 1):
            print(charectars,charectars2, charectars3,catchyPhrase,charectars4,charectars5,charectars6)
    if Passwordlenght == '7' :
        for i in range (0, 1):
            print(charectars,charectars2, charectars3,charectars4,catchyPhrase,charectars5,charectars6,charectars7)
    if Passwordlenght == '8' :
        for i in range (0, 1):
            print(charectars,charectars2, charectars3,charectars4,charectars5,catchyPhrasecharectars6,charectars7,charectars8)
    if Passwordlenght == '9' :
        for i in range (0, 1):
            print(charectars,charectars2, charectars3,charectars4,charectars5,charectars6,charectars7,catchyPhrase,charectars8,charectars9)   
    if Passwordlenght == '10' :
        for i in range (0, 1):
            print(charectars,charectars2, charectars3,charectars4,charectars5,charectars6,catchyPhrase,charectars7,charectars8,charectars9,charectars10)   
    
            
while (0<9)  :
    randomPassword()
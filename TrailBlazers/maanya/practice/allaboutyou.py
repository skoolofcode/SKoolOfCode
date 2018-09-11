import sys
def you():
    print("Answer these questions and I will tell you some interesting facts about you!")
    print(" ")
    name = (input("Enter your name (First, Middle, Last):"))
    YEAR_INPUT = (input("What year were you born in:"))
    bday = (input("What month you born in (Ex: x or 6 ~~Meaning you were born in June, The 6th Month):"))
    print("  ")
    print("A. Loyal and Patient")
    print("B. Intelligent and Witty")
    print("C. Bravery and Nerve")
    print("D. Ambitious and Cunning")
    hh = (input("Which of the above are you (A, B, C, or D):"))
    print("   ")
    print("A. Selfless")
    print("B. Peaceful")
    print("C. Honest")
    print("D. Brave")
    print("E. Smart")
    df = (input("You think of yourself as which of the above (A,B,C,D,E ):"))
    print(" ")
    print("1.Physics")
    print("2.Biology ")
    print("3.Chemical Engineering ")
    print("4.Aerospace and Aeronautical Engineering ")
    print("5.Nursing")
    print("6.Economics")
    print("7.Computer Science")
    print("8.Finance")
    print("9.Software Engineering")
    print("10.Political Science")
    mjr = (input("What would you like to major in ~out of options above ~ (1-10) :"))
    print("   ")
    print("   ")
    print("   ")
    print("   ")
    print("      ",name,"       ")
    RAT_LIST = ['1924','1936','1948','1960','1972','1984','1996','2008']
    for item in RAT_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The RAT! My lucky colors are Blue, Gold, and Green and I am Quick-Witted and Resouceful.")
    OX_LIST = ['1925','1937','1949','1961','1973','1985','1997','2009']
    for item in OX_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The OX! My lucky colors are Blue, Yellow, and Green and I am Diligent and Strong.")
    TIGER_LIST = ['1926','1938','1950','1962','1974','1986','1998','2010']
    for item in TIGER_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The TIGER! My lucky colors are Blue, Grey, White and Orange and I am Brave and Respected.")
    RABBIT_LIST = ['1927','1939','1951','1963','1975','1987','1999','2011']
    for item in RABBIT_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The RABBIT! My lucky colors are Red, Pink, Purple, and Blue and I am Gentle and Compassionate.")
    DRAGON_LIST = ['1928','1940','1952','1964','1976','1988','2000','2012']
    for item in DRAGON_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The DRAGON! My lucky colors are Gold, Silver, and A Grayish White and I am Intellectual and Energetic.")
    SNAKE_LIST = ['1929','1941','1953','1965','1977','1989','2001','2013']
    for item in SNAKE_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The SNAKE! My lucky colors are Red, Pale Yellow, and Black and I am Wise and have Financial Habits.")
    HORSE_LIST = ['1930','1942','1954','1966','1978','1990','2002','2014']
    for item in HORSE_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The HORSE! My lucky colors are Green, Red, and Purple and I am Active and Social.")
    GOAT_LIST = ['1931','1943','1955','1967','1979','1991','2003','2015']
    for item in GOAT_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The GOAT! My lucky colors are Brown, Red, and Purple and I am Clever and Polite.")
    MONKEY_LIST = ['1920','1932','1944','1956','1968','1980','1992','2004','2016']
    for item in MONKEY_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The MONKEY! My lucky colors are White, Gold, and Blue and I am Witty and Intelligent.")
    ROOSTER_LIST = ['1921','1933','1945','1957','1969','1981','1993','2005','2017']
    for item in ROOSTER_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The ROOSTER! My lucky colors are Gold, Brown, and Yellow and I am Hard-Working and Talented.")
    DOG_LIST = ['1922','1934','1946','1958','1970','1982','1994','2006','2018']
    for item in DOG_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The DOG! My lucky colors are Green, Red, and Purple and I am Kind and Loyal.")
    PIG_LIST = ['1923','1935','1947','1959','1971','1983','1995','2007','2019']
    for item in PIG_LIST:
        if YEAR_INPUT == item:
            print("My Chinese Zodiac is The year of The PIG! My lucky colors are Yellow, Gray, Brown, and Gold and I am Diligent and Driven.")
    if YEAR_INPUT < '1920' or YEAR_INPUT > '2019':
        sys.exit("Sorry, your input is invalid!")
        print(you())
    print("   ")
    if bday == '1':
        print("My Birthstone is a Garnet! The two Horoscopes associated with January are Capricorn(Jan.1-21) and Aquarius(Jan.22-31)")
    elif bday == '2':
        print("My Birthstone is an Amethyst! The two Horoscopes associated with February are Aquarius(Feb.1-21) and Pisces(Feb.22-31)")
    elif bday == '3':
        print("My Birthstone is an Aquamarine! The two Horoscopes associated with March are Pisces(March 1-21) and Aries(March 22-31)")
    elif bday == '4':
        print("My Birthstone is a Diamond! The two Horoscopes associated with April are Aries(April 1-21) and Pisces(April 22-30)")
    elif bday == '5':
        print("My Birthstione is an Emerald! The two Horoscopes associated with May are Taurus(May 1-21) and Gemini(May 22-31)")
    elif bday == '6':
        print("My Birthstione is a Pearl! The two Horoscopes associated with June are Gemini(June 1-21) and Cancer(June 22-30)")
    elif bday == '7':
        print("My Birthstione is a Ruby! The two Horoscopes associated with July are Cancer(July 1-21) and Leo(July 22-31)")
    elif bday == '8':
        print("My Birthstione is a Peridot! The two Horoscopes associated with August are Leo(Aug. 1-21) and Virgo(Aug. 22-31)")
    elif bday == '9':
        print("My Birthstione is a Sapphire! The two Horoscopes associated with September are Virgo(Sept. 1-21) and Libra(Sept. 22-30)")
    elif bday == '10':
        print("My Birthstione is an Opal! The two Horoscopes associated with October are Libra(Oct. 1-21) and Scorpio(Oct. 22-31)")
    elif bday == '11':
        print("My Birthstione is Topaz! The two Horoscopes associated with November are Scorpio(Nov. 1-21) and Sagittarius(Nov. 22-30)")
    elif bday == '12':
        print("My Birthstione is Turquoise! The two Horoscopes associated with December are Sagittarius(Dec. 1-21) and Capricorn(Dec. 22-31)")
    else:
        sys.exit("Your input is invalid.")
        print(you())
    if hh == 'A' or hh == 'a':
        print("   ")
        print("My Hogwarts house is HUFFLEPUFF! Hufflepuff is one of the four Houses of Hogwarts School of Witchcraft and Wizardry. Its founder was the medieval witch Helga Hufflepuff. Hufflepuff is the most inclusive among the four houses; valuing hard work, dedication, patience, loyalty, and fair play rather than a particular aptitude in its members.")
    elif hh == 'B' or hh == 'b':
        print("  ")
        print("My Hogwarts house is RAVENCLAW! Ravenclaw is one of the four Houses of Hogwarts School of Witchcraft and Wizardry. Its founder was a medieval witch Rowena Ravenclaw. Members of this house are characterised by their wit, learning, and wisdom. The emblematic animal is symbol is an eagle, and blue and bronze are its colours.")
    elif hh == 'C' or hh == 'c':
        print("  ")
        print("My Hogwarts house is GRYFFINDOR! Gryffindor is one of the four Houses of Hogwarts School of Witchcraft and Wizardry, founded by Godric Gryffindor. Godric instructed the Sorting Hat to choose a few particular characteristics he most values. Such character traits of students Sorted into Gryffindor are courage, chivalry, and determination.")
    elif hh == 'D' or hh == 'd':
        print("  ")
        print("My Hogwarts house is SLYTHERIN! Slytherins tend to be ambitious, shrewd, cunning, strong leaders, and achievement-oriented. They also have highly developed senses of self-preservation. This means that Slytherins tend to hesitate before acting, so as to weigh all possible outcomes before deciding exactly what should be done.")
    else:
        sys.exit("Your input is Invalid")
        print(you())
    if df == 'A' or df == 'a':
        print("  ")
        print("In Divergent, I would be Abnegation, The faction of Selflessness")
    elif df == 'B' or df == 'b':
        print("  ")
        print("In Divergent, I would be Amity, The Faction of Peace")
    elif df == 'C' or df == 'c':
        print("  ")
        print("In Divergent, I would be Candor, The Faction of Honesty ")
    elif df == 'D' or df == 'd':
        print("  ")
        print("In Divergent, I would be Dauntless, The Faction of Bravery")
    elif df == 'E' or df == 'e':
        print("  ")
        print("In Divergent, I would be Erudite, The Faction of the Intelligent ")
    else:
        print("  ")
        ("I AM DIVERGENT!")
    if mjr == '1':
        print("I would love to major in Physics. The top college for my chosen career is Massachusetts Institute of Technology")
    elif mjr == '2':
        print("I would love to major in Biology. The top college for my career is Harvard University.")
    elif mjr == '3':
        print("I would love to major in Chemical Engineering. The top college for my career is Massachusetts Institute of Technology.")
    elif mjr == '4':
        print("I would love to major in Aerospace and Aeronautical Engineering. The top college for my career is Georgia Institute of Technology.")  
    elif mjr == '5':
        print("I would love to major in Nursing. The top college for my career is University of Pennsylvania.") 
    elif mjr == '6':
        print("I would love to major in Economics. The top college for my career is Harvard University.") 
    elif mjr == '7':
        print("I would love to major in Computer Science. The top college for my career is Massachusetts Institute of Technology.")
    elif mjr == '8':
        print("I would love to major in Finance. The top college for my career is University of Pennsylvania.")
    elif mjr == '9':
        print("I would love to major in Software Engineering. The top college for my career is Carnegie Mellon University.")
    elif mjr == '10':
        print("I would love to major in Political Science. The top college for my career is Harvard University.")
    else:
        sys.exit("Your input is Invalid.")   
    print("Au Revoir ~",name)

    return
you()

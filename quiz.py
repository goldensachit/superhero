import splash_screen

while 1:
    x = input("Who is your favourite superhero?")
    y = x;
    x = x.replace(" ", "")
    x = x.lower();

    if x == "ironman" or x == "captainamerica":
        print("Atharva is " + y)
    elif x=="spiderman" or x == "doctorstrange" or x == "antman":
        print("Sachit is "+ y)
    elif x=="wonderwomen":
        print("Aavya is "+y)
    elif x=="wonderwoman" :
        print("Aavya is "+y)
    elif x=="captainmarvel":
        print("Aana is "+y)
    elif x=="blackpanther":
        print("Aarav is "+y)
    elif x=="deadpool":
        print("Hriday is "+y)
    elif x == "exit":
        print("Good bye")
        break
    else:
        print("Silly, '" + y + "' is not a superhero")
    print("--------------------")



total = 0
orderliszt = []

chicken = "Chicken, $5.25"
beef = "Beef, $6.25"
tofu = "Tofu, 5.75"

runda = 0

sandwhichselected = False
frenchffriesselected = False
bavardageselected = False

funymessage = 0

def totalprice(total):
    if sandwhichselected == True and frenchffriesselected == True and bavardageselected == True:
        print("Yoo brotha you ordered a healthy meal so u get a 1 dolla discount")
        total = total - 1
        print(" ")
    else:
        print("Next time, try to get something healthy..")
        print("")
    print("Heres yer total price buko: $" + str(total))
    quit()

def ketchup():
    global total
    print("You would like ketchup packets?")
    a = input("")
    if a.lower() == "y" or a.lower() == "yes":
        print("how many?")
        a = input("")
        if a.isnumeric() == False:
            print(" !! ")
            print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
            print(" !! ")
        else:
            ketchup()
            total = total + int(a) * .25
            orderliszt.append("Ketchup packets x" + int(a))
            totalprice(total)
    else:
        print(" ")
        print("Okayge Buisness Heres your total price and stuff you ordered.")
        print(" -- ")
        print(" Ordered items: ")
        print(orderliszt)
        print(" -- ")
        print(" Total: ")
        totalprice(total)
        quit()

def frenchffries():
    global total,funymessage,frenchffriesselected
    def ouiouimorefriesslvousplait():
        global total, runda
        moreorder = True
        while moreorder:
            print("Would you like to order anything else?")
            print("(Y)es or (N)o")
            b = input("")
            if b.lower() == "n" or b.lower() == "no":
                moreorder = False
                ketchup()

            elif b.lower() == "y" or b.lower() == "yes":
                print("OUI OUI! vous un fries enjoyer?")
                print("what fries more you want?")
                print("small, ok, or bakers dozen")

                a = input(" ")
                if a.lower() in ["small", "ok", "bakers dozen"]:
                    orderliszt.append(a)
                    runda = len(orderliszt)

                    if orderliszt[runda - 1] == "sall":
                        total = total + 1
                    elif orderliszt[runda - 1] == "ok":
                        total = total + 1.5
                    elif orderliszt[runda - 1] == "bakers dozen":
                        total = total + 2
                else:
                    print("")
                    print("Loll you spelled something wrong please try again")

            else:
                print("")
                print("Loll you spelled something wrong please try again")

    print(" ---- ")
    print("Dom's Alley Food")
    print("Current total cost: $" + str(total))
    print(" ---- ")
    print("Would you care for a french fry Monsieur?")
    
    a = input("")

    if a.lower() == "y" or a == "yes":
        print("What size of french fries would you like?")
        print("Small, Ok, or Collosal")
        a = input("")
        if a.lower() == "small":
            funnymessage = funnymessage + 1
            if funnymessage > 0:
                print("Would you like to mega size your french fries cuz obivously your french fries are too small at the current moment and need mega-sizing in order to get the best for your buck...")
                print("(Y)ae or (N)ae?")
            else:
                print("would u like to mega size yah order?")
                print("(Y)ae or (N)ae?")
            
            a = input("")

            if a.lower() == "y" or a.lower() == "yae" or a.lower() == "yes":
                print("Fry Order: Mega Sized")
                print("Order mega-sized.. you know that was just the price of the large fries...") # LOLL YOU GOT TROLLED :>
                frenchffriesselected = True
                total = total + 2
                ouiouimorefriesslvousplait()
            else:
                print("sum spelling error idk, your just gonna get the smal fries cuz u are like that.")
                total = total + 1
                ouiouimorefriesslvousplait()

        elif a.lower() == "ok":
            total = total + 1.5
            frenchffriesselected = True
            ouiouimorefriesslvousplait()
        elif a.lower() == "collosal":
            total = total + 2
            frenchffriesselected = True
            ouiouimorefriesslvousplait()
        else:
            print(" !! ")
            print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
            print(" !! ")
            frenchffries()
    elif a.lower() == "n" or a == "no":
        ketchup()
    else:
        print(" !! ")
        print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
        print(" !! ")
        frenchffries()

def Beverage():
    global total,bavardageselected,runda
    print(" ---- ")
    print("Dom's Alley Food")
    print("Current total cost: $" + str(total))
    print(" ---- ")
    print("Would you care for a drink Monsieur?")

    a = input("")

    if a.lower() == "exit":
        print("instaquitfunciton")
        quit()

    if a.lower() == "y" or a.lower() == "yes":
        print("What beverage size would you like?")
        print("Your current choices are: Teaspoon, Small, Massive, Collosal")
        a = input("")
        if a.lower() == "teaspoon":
            bavardageselected = False
            total = total + .25
            yumm1000000morecalories()
        if a.lower() == "small":
            bavardageselected = False
            total = total + 1
            yumm1000000morecalories()
        elif a.lower() == "massive":
            bavardageselected = False
            total = total + 1.75
            yumm1000000morecalories()
        elif a.lower() == "collosal":
            bavardageselected = False
            total = total + 2.25
            yumm1000000morecalories()
        else:
            print("Syntax or spel error Bozo")
            Beverage()

    elif a.lower() == "n" or a.lower() == "no":
        frenchffries()

    else: 
        print(" !! ")
        print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
        print(" !! ")
        Beverage()

def yumm1000000morecalories():
    global total, runda
    moreorder = True
    while moreorder:
        print("Would you like to order anything else?")
        print("(Y)es or (N)o")
        b = input("")
        if b.lower() == "n" or b.lower() == "no":
            moreorder = False
            frenchffries()

        elif b.lower() == "y" or b.lower() == "yes":
            print("What size Beverage would you like?")
            print("teaspoon, small, massive, collosal")

            a = input(" ")
            if a.lower() in ["teaspoon", "small", "massive", "collosal"]:
                orderliszt.append(a)
                runda = len(orderliszt)

                if orderliszt[runda - 1] == "teaspoon":
                    print("You'd like how many teaspoons????????")
                    a = input("")
                    teaspoons = int(a) * .25
                    total = total + teaspoons
                elif orderliszt[runda - 1] == "small":
                    total = total + 1
                elif orderliszt[runda - 1] == "massive":
                    total = total + 1.75
                elif orderliszt[runda - 1] == "collosal":
                    total = total + 2.25
            else:
                print("")
                print("Loll you spelled something wrong please try again")

        else:
            print("")
            print("Loll you spelled something wrong please try again")

def start(chicken,beef,tofu):
    global total, sandwhichselected,orderliszt
    def sandwichmoreorder():
        global runda,total
        moreorder = True
        while moreorder:
            print("Would you like to order anything else?")
            print("(Y)es or (N)o")
            b = input("")
            if b.lower() == "n" or b.lower() == "no":
                moreorder = False
                Beverage()
            elif b.lower() == "y" or b.lower() == "yes":
                print("What kind of sandwich would you like?")
                print("chicken $5.25, beef $6.25, tofu $5.75")
                a = input(" ")
                if a.lower() == "chicken" or a.lower() == "beef" or a.lower() == "tofu":
                    orderliszt.append(a)
                    if orderliszt[runda] == "chicken":
                        total = total + 5.25
                        runda = runda + 1
                    elif orderliszt[runda] == "beef":
                        total = total + 6.25
                        runda = runda + 1
                    elif orderliszt[runda] == "tofu":
                        total = total + 5.75
                        runda = runda + 1
                else:
                    print("")
                    print("Loll you spelled somethin wrong pls try again")
                    sandwichmoreorder()
            else:
                print("")
                print("Loll you spelled somethin wrong pls try again")
                sandwichmoreorder()

    print("Dom's Alley Food")
    print(" ---- ")
    print("What kind of sandwich would you like?")
    print("chicken $5.25, beef $6.25, tofu $5.75")
    
    a = input(" ")

    orderliszt.append(a)

    if orderliszt[0] == "chicken":
        total = total + 5.25
        sandwichmoreorder()
    elif orderliszt[0] == "beef":
        total = total + 6.25
        sandwichmoreorder()
    elif orderliszt[0] == "tofu":
        total = total + 5.75
        sandwichmoreorder()

    if a.lower() == "exit":
        print("instaquitfuncitonlmaogettrolledthatsepicyoufoundthesecretcommandfrfr!!!!")
        quit()

    if a.lower() == "chicken":
        sandwhichselected = True
        print("You currently ordered " + chicken + "... would you like to choose something else?")
        print("Type (Y)es or (N)o")
        a = input("")
        if a.lower() == "y" or a.lower() == "yes":
            start(chicken,beef,tofu)
        elif a.lower() == "n" or a.lower() == "no":
            total = total + 5.75
            Beverage()
        else: 
            print(" !! ")
            print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
            print(" !! ")
            start(chicken,beef,tofu)

    if a.lower() == "beef":
        sandwhichselected = True
        print("You currently ordered " + beef + "... would you like to choose something else?")
        print("Type (Y)es or (N)o")
        a = input("")
        if a.lower() == "y" or a.lower() == "yes":
            start(chicken,beef,tofu)
        elif a.lower() == "n" or a.lower() == "no":
            total = total+ 6.25
            Beverage()
        else: 
            print(" !! ")
            print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
            print(" !! ")
            start(chicken,beef,tofu)

    if a.lower() == "tofu":
        sandwhichselected = True
        print("You currently ordered " + tofu + "... would you like to choose something else?")
        print("Type (Y)es or (N)o")
        a = input("")
        if a.lower() == "y" or a.lower() == "yes":
            start(chicken,beef,tofu)
        if a.lower() == "y" or a.lower() == "no":
            total = total + 5.25
            Beverage()
        else: 
            print(" !! ")
            print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
            print(" !! ")
            start(chicken,beef,tofu)

    else:
        print("this guy THOUGHT he could say: '" + str(a) + "' , What a loser!!!")
        start(chicken,beef,tofu)

start(chicken,beef,tofu)
import random
import time
import math

#///////////////CONSTANT VARIABLES AND FUNCTIONS//////////////////
dirtarmourbuff = 1
silverarmourbuff = 1
goldarmourbuff = 1
dragonarmourbuff = 1
morbiusarmourbuff = 1

fishingrodowned = False

commonfish = 0
uncommonfish = 0
rarefish = 0
legendaryfish = 0
morbiusfish = 0
TOTALfish = commonfish + uncommonfish + rarefish + legendaryfish + morbiusfish

bopbought = 0
boplevel = 0
boplevel2 = 0
boplevel3 = 0
boplevel4 = 0
boss1defeated = False
boss2defeated = False
roundhp = 100
buff = 1
armour = 1
gold = 50
shopvisitcount = 0
skillopt = random.randint(15, 30 * buff)
attkopt = random.randint(1, 15 * buff)
attkdmg = attkopt * buff
skilldmg = skillopt * buff
plrhp = 100

def sleepge(seconds):
    print(end='', flush=True)
    for _ in range(seconds):
        time.sleep(1)
        print('.', end='', flush=True)
sleepge(5)
print(" ")

a = random.randint(1,5)
name = input("What is your name? ")
if a == 5:
    randending = ", Tears of my coding"
if a == 4:
    randending = ", Breath of the random.randint"
if a == 3:
    randending = ", Ocarina of time.sleep(2175984000)"
if a == 2:
    randending = ", The boolean waker"
if a == 1:
    randending = " " + str(name) + "'s Awakening"

print("________________________________")
print("Welcome to the game, the Legend of " + str(name) + str(randending))

# ///////////////PRE-GAME BUFFS AND ABILITIES, add fishing//////////////////
def fishshop(gold):
    global commonfish,uncommonfish,rarefish,legendaryfish,morbiusfish,fishingrodowned
    print(" ")
    print("________________________________")
    print("Hello and welcome to Sam's fishing department!")
    print(" ")
    print("I sell rods and currency, at the expense of fish!")
    print(" ")
    print("type in 'help' to show all the fish names")
    print(" ")
    print("Would you like to buy rods or sell fish?")
    a1 = input("type exit to go to the main screen ")
    if a1.lower() == "help":
        print("The fish names are...")
        print("commonfish,uncommonfish,rarefish,legendaryfish,morbiusfish")
        print(" ")
        fishshop(gold)
    if a1.lower() == "rods" or a1.lower() == "buy rods":
        print("________________________________")
        print("currently you can buy a fishing rod, would you like to buy one?")
        b1 = input("it costs 50 gold.. ")
        if b1.lower() == "y" or "yes" and gold > 50:
            print("________________________________")
            print("Purchase sucessfull..")
            fishingrodowned = True
            gold = gold - 50
            b = input("Would you like to go and fish with your new rod? ")
            if b == "yes" or b == "y":
                print("Travelling to the docs...")
                fish()
            else:
                print(" ")
                print("Returning to fish shoppe.")
                print(" ")
                fishshop(gold)
        else:
            print("________________________________")
            print("Insufficent currency or typo.")
            fishshop(gold)
    elif a1.lower() == "exit":
        print("________________________________")
        print("Returning back to main..")
        main()
    elif a1.lower() == "fish" or a1.lower() == "sell fish":
        def sellfish():
            if TOTALfish > 0:
                print("________________________________")
                print("Hello and welcome to the fish kiosk..")
                print("________________________________")
                print("You currently have.. " + str(commonfish) + "common fish, worth 25 gold")
                print(str(uncommonfish) + "uncommon fish, worth 50 gold")
                print(str(rarefish) + "rare fish, worth 150 gold")
                if legendaryfish > 0:
                    print("________________________________")
                    print(str(legendaryfish) + "LEGENDARY fish, worth 300 gold")
                if morbiusfish > 0:
                    print("________________________________")
                    print(str(morbiusfish) + "MORBIUS fish, worth 1200 gold")
                fish = input("what fish do you wnat to sell?, type exit to exit.")
                print("________________________________")
                if fish.lower() == "exit":
                    print("________________________________")
                    print("Exiting sell kiosk..")
                    fishshop(gold)
                if fish.lower() == "uncommon fish" or fish.lower() == "uncommon" or fish.lower() =="uncommonfish" and uncommonfish > 0:
                    uncommonfishtxt = input("how many uncommon fish would you like to sell?")
                    if uncommonfishtxt.isnumeric() == False:
                        print("________________________________")
                        print("only text is alloweed.")
                        sellfish()
                    if uncommonfishtxt <= uncommonfish:
                        gold = gold + (uncommonfishtxt * 25)
                        uncommonfish = uncommonfish - uncommonfishtxt
                        print("________________________________")
                        print("Sold sucessfully.")
                        sellfish()
                    else:
                        print("________________________________")
                        print("!!        uncommonfishtxt is larger than uncommon fish obtained.")
                        sellfish()
                else:
                    print("!!         fish not avaliable or typo.")
                    sellfish()
                if fish.lower() == "common fish" or fish.lower() == "common" or fish.lower() == "commonfish" and commonfish > 0:
                    commonfishtxt = input("how many uncommon fish would you like to sell?")
                    if commonfishtxt.isnumeric() == False:
                        print("________________________________")
                        print("only text allowed")
                        sellfish()
                    if commonfishtxt <= commonfish:
                        gold = gold + (commonfishtxt * 50)
                        commonfish = commonfish - commonfishtxt
                        print("Sold sucessfully.")
                        sellfish()
                    else:
                        print("________________________________")
                        print("!!        commonfishtxt is larger than common fish obtained.")
                        sellfish()
                else:
                    print("!!         fish not avaliable or typo.")
                    sellfish()
                if fish.lower() == "rare fish" or fish.lower() == "rare" or fish.lower() == "rarefish" and rarefish > 0:
                    rarefishtxt = input("how many rare fish would you like to sell?")
                    if rarefishtxt.isnumeric() == False:
                        print("________________________________")
                        print("only text allowed")
                        sellfish()
                    if rarefishtxt <= rarefish:
                        gold = gold + (rarefishtxt *  150)
                        rarefish = rarefish - rarefishtxt
                        print("Sold sucessfully.")
                        sellfish()
                    else:
                        print("________________________________")
                        print("!!        rarefishtxt is larger than rare fish obtained.")
                        sellfish()
                else:
                    print("!!         fish not avaliable or typo.")
                if fish.lower() == "legendary fish" or fish.lower() == "legendary" or fish.lower() == "legendaryfish" and legendaryfish > 0:
                    legendaryfishtxt = input("how many legendary fish would you like to sell?")
                    if legendaryfishtxt.isnumeric() == False:
                        print("________________________________")
                        print("only text allowed")
                        sellfish()
                    if legendaryfishtxt <= legendaryfish:
                        gold = gold + (legendaryfishtxt *  300)
                        legendaryfish = legendaryfish - legendaryfishtxt
                        print("Sold sucessfully.")
                        sellfish()
                    else:
                        print("________________________________")
                        print("!!        legendaryfish text is larger than legendary fish obtained.")
                        sellfish()
                else:
                    print("!!         fish not avaliable or typo.")
                if fish.lower() == "morbius fish" or "morbius" or "morbiusfish" and morbiusfish > 0:
                    morbiusfishtxt = input("how many morbius fish would you like to sell?")
                    if morbiusfishtxt.isnumeric() == False:
                        print("________________________________")
                        print("only text allowed")
                        sellfish()
                    if morbiusfishtxt <= morbiusfish:
                        gold = gold + (morbiusfishtxt *  300)
                        morbiusfish = morbiusfish - morbiusfishtxt
                        print("Sold sucessfully.")
                        sellfish()
                    else:
                        print("________________________________")
                        print("!!        morbius text is larger than morbius fish obtained.")
                        sellfish()
                else:
                    print("!!         fish not avaliable or typo.")
            else:
                print("Go get a fishing rod from the shop and start fishing!!")
                fishshop(gold)

    else:
        print("Typo occured!")
        fishshop(gold)

def fishaction():
    global commonfish,uncommonfish,rarefish,legendaryfish,morbiusfish,fishingrodowned
    randomfish = random.randint(1,400)
    if randomfish in range(1,110):
        print(" - - - " + str(name) + "'s Fishing rewards - - -")
        print("Reeling in...")
        sleepge(1)
        print("Done!")
        sleepge(1)
        randomamount = random.randint(1,15)
        print("You gained " + str(randomamount) + " uncommon fish!")
        uncommonfish = uncommonfish + randomamount
        xyz = input("Would you like to continue fishing? ")
        if xyz.lower() == "n" or xyz.lower() == "no" or xyz.lower() == "nae":
            print("Returning to the main menu")
            main()
        else:
            fishaction()
    elif randomfish in range (111,282):
        print(" - - - " + str(name) + "'s Fishing rewards - - -")
        print("Reeling in...")
        sleepge(1)
        print("Done!")
        sleepge(1)
        randomamount = random.randint(1,10)
        print("You gained " + str(randomamount) + " common fish!")
        commonfish = commonfish + randomamount
        xyz = input("Would you like to continue fishing? ")
        if xyz.lower() == "n" or xyz.lower() == "no" or xyz.lower() == "nae":
            print("Returning to the main menu")
            main()
        else:
            fishaction()
    elif randomfish in range (283,373):
        print(" - - - " + str(name) + "'s Fishing rewards - - -")
        print("Reeling in...")
        sleepge(1)
        print("Done!")
        sleepge(1)
        randomamount = random.randint(1,5)
        rarefish = rarefish + randomamount
        print("You gained " + str(randomamount) + " rare fish!")
        xyz = input("Would you like to continue fishing? ")
        if xyz.lower() == "n" or xyz.lower() == "no" or xyz.lower() == "nae":
            print("Returning to the main menu")
            main()
        else:
            fishaction()
    elif randomfish in range (374,399):
        print(" - - - " + str(name) + "'s Fishing rewards - - -")
        print("Reeling in...")
        sleepge(1)
        print("Done!")
        sleepge(1)
        randomamount = random.randint(1,5)
        legendaryfish = legendaryfish + randomamount
        print("You gained " + str(randomamount) + " legendary fish!")
        xyz = input("Would you like to continue fishing? ")
        if xyz.lower() == "n" or xyz.lower() == "no" or xyz.lower() == "nae":
            print("Returning to the main menu")
            main()
        else:
            fishaction()
    elif randomfish in range (399,400):
        print(" - - - " + str(name) + "'s Fishing rewards - - -")
        print("Reeling in...")
        sleepge(1)
        print("Done!")
        sleepge(1)
        randomamount = random.randint(1,3)
        morbiusfish = morbiusfish + randomamount
        print("You gained " + str(randomamount) + " morbius fish!")
        xyz = input("Would you like to continue fishing? ")
        if xyz.lower() == "n" or xyz.lower() == "no" or xyz.lower() == "nae":
            print("Returning to the main menu")
            main()
        else:
            fishaction()
    if TOTALfish > 25:
        b = random.randint(1,10000100101010)
        if b % 2 > 0:
            print("Your fishing rod BROKE!")
            fishingrodowned = False
        else:
            fishaction()


def fish():
    global commonfish,uncommonfish,rarefish,legendaryfish,morbiusfish,fishingrodowned
    if fishingrodowned == True:
        print("________________________________")
        print("You arrive at the docks and start fishing..")
        fishaction()
    else:
        print(" ")
        print("You DONT own a fishing rod, go to the fish shop to buy one!")
        print(" ")
        a = input("Would you like to be re-directed to the fish shop? ")
        print(" ")
        if a.lower() == "y" or a.lower() == "yes" or a.lower() == "yae":
            print("Transporting to fish shop")
            sleepge(1)
            fishshop(gold)
        else:
            print("Returning back to main...")
            main()


def gamble(gold):
    mingold = int(gold)/2
    sleepge(3)
    print("You currently have " + str(gold) + " złote (gold) in your pocket")
    if gold < 0:
        print("You broke. You cant gamble no more.")
        main()
    print("___________________________")
    print("Hello and welcome to Roberts gambilling corner")
    print("___________________________")
    print("input using numbers 1,2, or 3 ")
    print(" !!     type in exit to return back to the main screen, or type continue to continue gambilling!")
    print("___________________________")
    a = input(" ")
    if a.lower() == "exit":
        print("Returning to main screen")
        main()
    if a.lower() == "1":
        print("So, you've chosen the 1st game eh?")
        a2 = input("How much money would you like to gamble? ")
        if a2.isnumeric == False:
            print("Ight bro, for clearly not understanding the concept of numbers, ill have to take away some cash")
            gold = gold - 2
            print("You currently have " + str(gold) + " gold.")
        elif int(a2) > gold:
            print("Just by looking at your pockets, i can determine that YOU DONT HAVE THAT MONEY!!!!")
            gamble(gold)
        if int(a2) < float(mingold):
            print("You see, after taking a look at your pockets, id advise you to gamble some more...")
            gamble(gold)
        b = random.randint(1,1000000000000000)
        if b % 2 > 0:
            print("HAHA, ALL MINE.")
            gold = gold - int(a2)
            print("You've lost " + str(int(gold - int(a2))))
            gamble(gold)
        else:
            print("Ahh, you seem quite lucky! you've won it all!")
            print("You now have " + str(gold) + " gold.")
            print("___________________________")
            gold = + (int(a2) * 2)
            print("Doubble or nothing?, (Y)ae or (N)ae?")
            print("___________________________")
            doub = input(" ")
            print("___________________________")
            if doub.upper() == "Y":
                print("Allrighty! lets go again..")
                print("___________________________")
                print("How much money would you like to gamble?")
                a1 = input(" ")
                print("___________________________")
                if a1.isnumeric == False:
                    print("Ight bro, for clearly not understanding the concept of numbers, ill have to take away some cash")
                    gold = gold - 4
                    print("You currently have " + str(gold) + " gold.")
                    main()
                elif int(a1) > gold:
                    print("Just by looking at your pockets, i can determine that YOU DONT HAVE THAT MONEY!!!!")
                    gamble(gold)
                if int(a1) < float(mingold):
                    print("You see, after taking a look at your pockets, id advise you to gamble some more...")
                    gamble(gold)
                b1 = random.randint(1,1000000000000000)
                if b1 % 2 > 0:
                    print("HAHA, ALL MINE.")
                    gold = gold - int(a2)
                    print("You've lost " + str(int(gold - int(a2))))
                    main()
                else:
                    print("Ahh, you seem quite lucky! you've won it all!")
                    print("You now have " + str(gold) + " gold.")
                    gold = str(a1) * 4
                    gamble(gold)
            else:
                print("Alright, you missed a golden opportunity though....")
                main()

def shop(buff,armour):
    plrhp = 100
    global shopvisitcount,gold,bopbought,boplevel,boplevel2,boplevel3,boplevel4,dirtarmourbuff,silverarmourbuff,goldarmourbuff,dragonarmourbuff,morbiusarmourbuff
    print("________________________________")
    print("You've been at the shop " + str(shopvisitcount) + " Time(s)")
    print("You currently have " + str(gold) + " gold!")
    shopvisitcount += 1
    print("________________________________")
    print("Hello and welcome to the Shop!")
    print("Currently you can buy buffs, armour, or go to the fish shop")
    a = input(" ")
    print("________________________________")
    if a == "buffs":
        print("use the term 'buy' to buy products")
        b = input("Currently, you can buy 1 buff, called Blessing of Protection ")
        print("type 'info' for the item's description.")
        if b == "buy" and gold > 100:
            if bopbought == 0:
                bopbought = bopbought + 1
                boplevel = boplevel + 5
                print("Applied Level I Buff")
                gold = gold - 100
            elif bopbought == 1:
                bopbought = bopbought + 1
                boplevel2 = boplevel2 + 5
                print("Applied Level II Buff")
                gold = gold - 150
            elif bopbought == 2:
                bopbought = bopbought + 1
                boplevel3 = boplevel3 + 5
                print("Applied Level III Buff")
                gold = gold - 300
            elif bopbought == 3:
                bopbought = bopbought + 1
                boplevel4 = boplevel4 + 5
                print("Applied Level III Buff")
                gold = gold - 450
            elif bopbought == 4:
                print("Maximum Level III Buff has allready been applied")
                shop(buff,armour)
            buff = boplevel + boplevel2 + boplevel3 + boplevel4
            print("________________________________")
        else:
            print("________________________________")
            print("Insufficent gold or spelling error...")
            shop(buff,armour)
        if b == "info":
            print("Blessing of Protection; Level " + str(bopbought))
            print("This protection buff allows you to multiply your damage by 5,10,15, and 20 times as respective to the blessings level.")
            sleepge(3)
            shop(buff,armour)
    if a == "armour" or a == "armor":
        print("________________________________")
        print("There are currently 4 armour sets..")
        print("Dirt, Gold, and Silver")
        e = input(" ")
        if e.lower() == "dirt":
            print("this armour costs 150 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 150:
                print("Purchase complete!")
                dirtarmourbuff = 1.5
                gold = gold - 150
                shop(buff,armour)
            else:
                print("!!     Insufficent currency or typo.")
                shop(buff,armour)
        if e.lower() == "silver":
            print("this armour costs 300 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 300:
                print("Purchase complete!")
                dirtarmourbuff = 1
                silverarmourbuff = 2
                gold = gold - 300
                shop(buff,armour)
            else:
                print("!!     Insufficent currency or typo.")
                shop(buff,armour)
        if e.lower() == "gold":
            print("this armour costs 600 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 600:
                print("Purchase complete!")
                dirtarmourbuff = 1
                silverarmourbuff = 1
                goldarmourbuff = 3
                gold = gold - 300
                shop(buff,armour)
            else:
                print("!!     Insufficent currency or typo.")
                shop(buff,armour)
        else:
            print("________________________________")
            print("insufficient gold")
            shop(buff,armour)
        if a == "fish shop" or a == "fish" or a == "fishshop":
            fishshop(gold)
    else:
        c = input("do you want to exit the shop?")
        if c.lower() == "yes" or c.lower() == "y" or c.lower() == "exit":
            print("ok returning to the game")
            main()
        else:
            shop(buff,armour)

def main():
    print("Welcome to the main screen")
    i1 = input("Would you like to take on a boss, or go to the shop?")
    if i1.lower() == "boss":
        bosses()
    elif i1.lower() == "shop":
        shop(buff,armour)

# ///////////////BOSSES//////////////////
def bosses():
    global boss1defeated, gold
    print("________________________________")
    print("Hello and welcome to the boss area")
    print(" ")
    print("There are currently 10 bosses, the harder they are, the closer to 10 they're going to be.")
    print("It is recommended that you start with the (1)st boss.")
    a1 = input(" ")
    if a1 == "1" or a1.lower() == "first":
        print("________________________________")
        boss1(roundhp)
    elif a1 == "2" or a1.lower() == "second":
        if boss1defeated:
            boss2()
        else:
            print("You have to defeat the 1st boss to take on the second!")
            main()
    else:
        print("Returning back to main")
        main()
# ///////////////BOSS 1//////////////////
skilluse = 0
def boss1(roundhp):
    def boss1defeatrule():
        if roundhp < 0 and plrhp > 0:
            print("You've Won! 1000 gold has been added to your account")
            gold += gold + 1000
            main()
        elif roundhp > 0 or plrhp < 0:
            print("You've lost all of you hp and or you've run out of turns!")
        else:
            sleepge(3)

    global attkdmg, skilldmg, armour, boss1defeated, gold
    plrhp = 100 * dirtarmourbuff * silverarmourbuff * dragonarmourbuff * morbiusarmourbuff
    print("\n---" + name + "'s Turn ---")
    round1 = input("do an Attack or Skill ")

    if round1 == "attack":
        roundhp = roundhp - attkdmg
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg) + " damage!")
    elif round1 == "skill":
        roundhp = roundhp - skilldmg
        skilluse + 1
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg) + " damage!")

    
    print("\n--- Opponents's Turn ---")

    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp - (opponentdmg / armour)

    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))

    # ROUND 2 TURN
    print("\n---" + name + "'s Turn ---")
    print("")
    round2 = input("ROUND II! Would you like to attack, skill, or FLEE?")
    if round2 == "attack":
        roundhp = roundhp - attkdmg
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg) + " damage!")
    elif round2 == "skill":
        if skilluse > 1:
            print("Sorry, but your SKILL is on ICD (internal cooldown)")
            a = input("Would you like to sacrifice a turn to get your skill back? (Y)es,(N)o")
            if a.upper() == "Y":
                print("Alright, skipping turn...")
                opponentdmg = random.randint(1, 100)
                plrhp = plrhp - (opponentdmg / armour)
                print("You currently have " + str(plrhp) + " HP left")
                if plrhp > 0:
                    print("Activating Skill...")
                    roundhp = roundhp - skilldmg
                    print("The current boss health is... " + str(roundhp))
                    print("You dealt " + str(skilldmg) + " damage!")
                else:
                    print("You've died from the bosse's passive attack... Returning to main menu")
                    main()
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()
    
    boss1defeatrule()

    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp - (opponentdmg / armour)

    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))
    
    boss1defeatrule()

    # ROUND 3 TURN

    print("\n---" + name + "'s Turn ---")
    round2 = input("ROUND III! Would you like to attack, skill, or FLEE?")
    print("___________________________")
    print("!!           At this stage in the game, one turn should defeat the boss!")
    print("___________________________")
    if round2 == "attack":
        roundhp = roundhp - attkdmg
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg) + " damage!")
    elif round2 == "skill":
        roundhp = roundhp - skilldmg
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg) + " damage!")
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()
    boss1defeatrule()

    # OPPONENT'S TURN

    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp - (opponentdmg / armour)

    boss1defeatrule()
    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))

    if plrhp > 0 and roundhp <= 0:
        print("You've successfully defeated the boss!")
        boss1defeated = True
        gold += 10000
        print("You now have " + str(gold) + " gold")
        main()
    else:
        print("You havent sucessfully defeated the boss...")
        print("You've run out of turns! Returning to the home menu...")
        main()


# ///////////////BOSS 2, get dragon armour from this boss//////////////////
def boss2():
    print("___________________________")
    print("second boss hasnt been added yet.")
    main()

# ///////////////MAIN SCREEN//////////////////

def main():
    global gold
    if name.lower() == "dominik":
        print("Hej developer dom, you gained a grap ton of currency rn.")
        gold = gold + 1000000000000
    roundhp = 100
    print("___________________________")
    print("Welcome to the main screen")
    print("________________________________")
    print("P.S. for advanced options, type in 'help'")
    print("___________________________")
    i1 = input("Would you like to take on a boss, fish, or go to the shop? ")
    if i1.lower() == "boss":
        bosses()
    elif i1.lower() == "shop":
        shop(buff,armour)
    elif i1.lower() == "fish":
        fish()
    elif i1.lower() == "help":
        print("___________________________")
        print("Other commands include: gamble,statistics")
        print("___________________________")
        main()
    elif i1.lower() == "exit":
        print("___________________________")
        print("exiting game")
        sleepge(3)
        print("___________________________")
        quit()
    elif i1.lower() == "exit2":
        print("___________________________")
        print("developerinstaquit")
        quit()
    elif i1.lower() == "statistics":
        print("___________________________")
        print("You have " + str(gold) + "gold")
        print(str(plrhp) + "health")
        print("Boss 1 has beend defeated? "+ str(boss1defeated))
        print("Boss 2 has been defeated? " + str(boss2defeated))
        print("current buff: " + str(buff) + " this value is multiplicative")
        print("current armour: " + str(armour) + " this value is the dividend of the enemies attacks")
        print("___________________________")
        main()
    elif i1.lower() == "gamble":
        gamble(gold)
    else:
        print(" ")
        print("!!        Thats not in the selection!")
        print(" ")
        main()
main()
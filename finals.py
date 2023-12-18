import random
import time

#///////////////CONSTANT VARIABLES AND FUNCTIONS//////////////////
secretachievements = 0

armourliszt = ["gold", "iron","silver", "platinum", "dragon","morbius"]

fishingrodowned = False
bopbought = 0

commonfish = 0
uncommonfish = 0
rarefish = 0
legendaryfish = 0
morbiusfish = 0

fishliszt = ["commonfish","uncommonfish","rarefish","legendaryfish","morbiusfish"]

gold = 50

boss1defeated = False
boss2defeated = False
boss3defeated = False

roundhp = 100
buff = 1
armour = 1
plrhp = 100 * armour
shopvisitcount = 0

skillopt = random.randint(15, 30)
attkopt = random.randint(1, 15)

attkdmg = attkopt * buff
skilldmg = skillopt * buff

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
def bossdefeatrule(gold,plrhp):
        if roundhp <= 0 and plrhp >= 0:
            global boss1defeated
            print("    ")
            print(" !!! ")
            print("You've Won! 1000 gold has been added to your account")
            print(" !!! ")
            gold += gold + 1000
            plrhp = 100 * armour
            boss1defeated = True
            main()
        elif roundhp >= 0 and plrhp <= 0:
            print("    ")
            print(" !!! ")
            print("You've lost all of you hp and or you've run out of turns!")
            print("YOU LOOSE.....")
            print(" !!! ")
            print(" ")
            main()
        elif plrhp <= 0:
            print("    ")
            print(" !!! ")
            print("You've lost all of you hp and or you've run out of turns!")
            print("YOU LOOSE.....")
            print(" !!! ")
            print(" ")
            main()
        else:
            sleepge(3)


def sellfish():
    global gold,rarefish,commonfish,uncommonfish,legendaryfish,morbiusfish
    if commonfish + uncommonfish + legendaryfish + morbiusfish + rarefish > 0:
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
            if int(uncommonfishtxt) <= uncommonfish:
                gold = gold + int(uncommonfishtxt) * 25
                uncommonfish = uncommonfish - int(uncommonfishtxt)
                print("________________________________")
                print("Sold sucessfully.")
                sellfish()
            else:
                print("________________________________")
                print("!!        uncommonfishtxt is larger than uncommon fish obtained.")
                sellfish()
        if fish.lower() == "common fish" or fish.lower() == "common" or fish.lower() == "commonfish" and commonfish > 0:
            commonfishtxt = input("how many uncommon fish would you like to sell?")
            if commonfishtxt.isnumeric() == False:
                print("________________________________")
                print("only text allowed")
                sellfish()
            if int(commonfishtxt) <= commonfish:
                gold = gold + int(commonfishtxt) * 50
                commonfish = commonfish - int(commonfishtxt)
                print("Sold sucessfully.")
                sellfish()
            else:
                print("________________________________")
                print("!!        commonfishtxt is larger than common fish obtained.")
                sellfish()
        if fish.lower() == "rare fish" or fish.lower() == "rare" or fish.lower() == "rarefish" and rarefish > 0:
            rarefishtxt = input("how many rare fish would you like to sell?")
            if rarefishtxt.isnumeric() == False:
                print("________________________________")
                print("only text allowed")
                sellfish()
            if int(rarefishtxt) <= rarefish:
                gold = gold + int(rarefishtxt) *  150
                rarefish = rarefish - rarefishtxt
                print("Sold sucessfully.")
                sellfish()
            else:
                print("________________________________")
                print("!!        rarefishtxt is larger than rare fish obtained.")
                sellfish()
        if fish.lower() == "legendary fish" or fish.lower() == "legendary" or fish.lower() == "legendaryfish" and legendaryfish > 0:
            legendaryfishtxt = input("how many legendary fish would you like to sell?")
            if legendaryfishtxt.isnumeric() == False:
                print("________________________________")
                print("only text allowed")
                sellfish()
            if int(legendaryfishtxt) <= legendaryfish:
                gold = gold + int(legendaryfishtxt) *  300
                legendaryfish = legendaryfish - int(legendaryfishtxt)
                print("Sold sucessfully.")
                sellfish()
            else:
                print("________________________________")
                print("!!        legendaryfish text is larger than legendary fish obtained.")
                sellfish()
        if fish.lower() == "morbius fish" or "morbius" or "morbiusfish" and morbiusfish > 0:
            morbiusfishtxt = input("how many morbius fish would you like to sell?")
            if morbiusfishtxt.isnumeric() == False:
                print("________________________________")
                print("only text allowed")
                sellfish()
            if int(morbiusfishtxt) <= morbiusfish:
                gold = gold + int(morbiusfishtxt) *  300
                morbiusfish = morbiusfish - int(morbiusfishtxt)
                print("Sold sucessfully.")
                sellfish()
            else:
                print("________________________________")
                print("!!        morbius text is larger than morbius fish obtained.")
                sellfish()
        else:
            print("!!         fish not avaliable or typo.")
            sellfish()
    else:
        print("!!!       Go get a fishing rod from the shop and start fishing!!")
        fishshop(gold)

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
    print("  ")
    if a1.lower() == "rods" or a1.lower() == "buy rods" or a1.lower() == "rod":
        print("________________________________")
        print("currently you can buy a fishing rod, would you like to buy one?")
        b1 = input("it costs 50 gold.. ")
        if b1.lower() == "y" or "yes" and gold >= 50:
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
    if a1.lower() == "fish" or a1.lower() == "sell fish" or a1.lower() == "sell":
        sellfish()
    else:
        c = input("do you want to exit the fish shop?")
        if c.lower() == "yes" or c.lower() == "y" or c.lower() == "exit":
            print("ok returning to the game")
            main()
        else:
            fishshop(gold)

def fishaction():
    global commonfish,uncommonfish,rarefish,legendaryfish,morbiusfish,fishingrodowned
    xyz = input("Would you like to continue fishing? ")
    if xyz.lower() == "y" or xyz.lower() == "yes":
        randomfish = random.randint(1,400)
        if randomfish in range (111,282):
            print(" - - - " + str(name) + "'s Fishing rewards - - -")
            print("Reeling in...")
            sleepge(1)
            print("Done!")
            sleepge(1)
            randomamount = random.randint(1,3)
            print("You gained " + str(randomamount) + " common fish!")
            commonfish = commonfish + randomamount
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
            fishaction()
        elif randomfish in range (374,399):
            print(" - - - " + str(name) + "'s Fishing rewards - - -")
            print("Reeling in...")
            sleepge(1)
            print("Done!")
            sleepge(1)
            randomamount = random.randint(1,2)
            legendaryfish = legendaryfish + randomamount
            print("You gained " + str(randomamount) + " legendary fish!")
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
            fishaction()
        if commonfish + uncommonfish + legendaryfish + morbiusfish + rarefish > 25:
            b = random.randint(1,10000100101010)
            if b % 2 > 0:
                print("Your fishing rod BROKE!")
                fishingrodowned = False
            else:
                fishaction()
    else:
        def exitlog():
            a = input("Would you like to be re-directed to the fish shop, continue fishing or return to the main menu? ")
            print(" ")
            if a.lower() == "fishshop" or a.lower() == "fish" or a.lower() == "shop":
                print("Transporting to fish shop")
                sleepge(1)
                fishshop(gold)
            elif a.lower() == "main" or a.lower() == "menu" or a.lower() == "main menu" or a.lower() == "exit":
                print("Transporting to main screen")
                sleepge(1)
                main()
            elif a.lower() == "continue" or a.lower() == "fish" or a.lower() == "continue fishing" or a.lower() == "fishing":
                fishaction()
            else:
                print("Accepted arguments are fishshop,fish,shop and main,menu,mainmenu,continue fishing,fish,fishing,exit")
                exitlog()
                print("  ")
        exitlog()

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

def shop(shopvisitcount,plrhp):
    global gold,buff,bopbought,armour
    print("________________________________")
    print("You've been at the shop " + str(shopvisitcount) + " Time(s)")
    print("You currently have " + str(gold) + " gold!")
    shopvisitcount += 1
    print("________________________________")
    print("Hello and welcome to the Shop!")
    print("Currently you can buy buffs, armour, or go to the fish shop")
    a = input(" ")
    print("________________________________")
    if a == "fish shop" or a == "fish" or a == "fishshop":
        fishshop(gold)
    if a == "buffs":
        print("use the term 'buy' to buy products")
        b = input("Currently, you can buy 1 buff, called Blessing of Protection ")
        print("type 'info' for the item's description.")
        if b == "buy" and gold > 1000:
            if bopbought == 0:
                if gold < 1000:
                    print(" ")
                    print("!!        Insuficcent currency")
                    print(" ")
                    shop(shopvisitcount,plrhp)
                else:
                    bopbought = bopbought + 1
                    print("Applied Level I Buff")
                    buff = 2
                    gold = gold - 1000
                    shop(2,plrhp)
            if bopbought == 1:
                if gold < 3000:
                    print(" ")
                    print("!!        Insuficcent currency")
                    print(" ")
                    shop(shopvisitcount,plrhp)
                else:
                    bopbought = bopbought + 1
                    print("Applied Level II Buff")
                    buff = 3
                    gold = gold - 3000
                    shop(3,plrhp)
            if bopbought == 2:
                if gold < 6000:
                    print(" ")
                    print("!!        Insuficcent currency")
                    print(" ")
                    shop(shopvisitcount,plrhp)
                else:
                    bopbought = bopbought + 1
                    buff = 4
                    print("Applied Level III Buff")
                    gold = gold - 6000
                    shop(4,plrhp)
            if bopbought == 3:
                if gold < 12000:
                    print(" ")
                    print("!!        Insuficcent currency")
                    print(" ")
                    shop(shopvisitcount,plrhp)
                else:
                    bopbought = bopbought + 1
                    print("Applied Level IV Buff")
                    buff = 5
                    gold = gold - 12000
                    shop(5,plrhp)
            if bopbought == 4:
                print("Maximum Level IV Buff has allready been applied")
                shop(5,plrhp)
            print("________________________________")
        else:
            print("________________________________")
            print("Insufficent gold or spelling error...")
            shop(shopvisitcount,plrhp)
        if b == "info":
            print("Blessing of Protection; Level " + str(bopbought))
            print("This protection buff allows you to multiply your damage by 2,3,4, and 5 times as respective to the blessings level.")
            sleepge(3)
            shop(shopvisitcount,plrhp)
    if a == "armour" or a == "armor":
        print("________________________________")
        print("There are currently 4 armour sets..")
        print("Iron, Gold, and Platinum")
        e = input(" ")
        if e.lower() == "iron":
            print("this armour costs 1500 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 1500:
                print("Purchase complete!")
                armour = armour + 2
                gold = gold - 1500
                shop(shopvisitcount,plrhp)
            else:
                print("!!     Insufficent currency or typo.")
                shop(shopvisitcount,plrhp)
        if e.lower() == "gold":
            print("this armour costs 3000 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 3000:
                print("Purchase complete!")
                armour = armour + 4
                gold = gold - 3000
                shop(shopvisitcount,plrhp)
            else:
                print("!!     Insufficent currency or typo.")
                shop(shopvisitcount,plrhp)
        if e.lower() == "platinum":
            print("this armour costs 6000 gold, would you like to buy it?")
            a1 = input("(Y)ae or (N)ae? ")
            if a1.lower() == "y" and gold > 6000:
                print("Purchase complete!")
                armour = armour + 8
                gold = gold - 6000
                shop(shopvisitcount,plrhp)
            else:
                print("!!     Insufficent currency or typo.")
                shop(shopvisitcount,plrhp)
        else:
            print("________________________________")
            print("insufficient gold")
            shop(shopvisitcount,plrhp)
    else:
        c = input("do you want to exit the shop?")
        if c.lower() == "yes" or c.lower() == "y" or c.lower() == "exit":
            print("ok returning to the game")
            main()
        else:
            shop(shopvisitcount,plrhp)

def main():
    print("Welcome to the main screen")
    i1 = input("Would you like to take on a boss, or go to the shop?")
    if i1.lower() == "boss":
        bosses()
    elif i1.lower() == "shop":
        shop(shopvisitcount,plrhp)

# ///////////////BOSSES//////////////////
def bosses():
    global buff,plrhp
    print(armour)
    print("________________________________")
    print("Hello and welcome to the boss area")
    print(armour)
    print(" ")
    print("There are currently 10 bosses, the harder they are, the closer to 10 they're going to be.")
    print("It is recommended that you start with the (1)st boss.")
    a1 = input(" ")
    if a1 == "1" or a1.lower() == "first":
        print("________________________________")
        boss1()
    elif a1 == "2" or a1.lower() == "second":
        if boss1defeated:
            boss2()
        else:
            print("You have to defeat the 1st boss to take on the second!")
            main()
    else:
        print("Returning back to main")
        main()
# ///////////////BOSS 1, REWORK COMBAT SYSTEM OVER WEEKEND.. PREHAPS USE FOR LOOPS//////////////////
skilluse = 0
def boss1():
    global buff,roundhp,attkopt,skillopt,armour,attkdmg,skilldmg,plrhp,gold,boss1defeated
    roundhp = 100
    print(armour)
    print("\n---" + name + "'s Turn ---")
    round1 = input("do an Attack or Skill ")

    if round1 == "attack":
        roundhp = roundhp - (attkdmg * buff)
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round1 == "skill":
        roundhp = roundhp - (skilldmg * buff)
        skilluse + 1
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg * buff) + " damage!")

    bossdefeatrule(gold,plrhp)
    
    print("\n--- Opponents's Turn ---")

    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp * armour - (opponentdmg)

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
        roundhp = roundhp - attkdmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round2 == "skill":
        if skilluse > 1:
            print("Sorry, but your SKILL is on ICD (internal cooldown)")
            a = input("Would you like to sacrifice a turn to get your skill back? (Y)es,(N)o")
            if a.upper() == "Y":
                print("Alright, skipping turn...")
                opponentdmg = random.randint(1, 100)
                plrhp = plrhp * buff - (opponentdmg)
                print("You currently have " + str(plrhp) + " HP left")
                if plrhp > 0:
                    print("Activating Skill...")
                    roundhp = roundhp - skilldmg
                    print("The current boss health is... " + str(roundhp))
                    print("You dealt " + str(skilldmg) + " damage!")
                else:
                    print("You've died from the bosse's passive attack... Returning to main menu")
                    main()
        else:
            roundhp = roundhp - skilldmg * buff
            print("The current boss health is... " + str(roundhp))
            print("You dealt " + str(skilldmg * buff) + " damage!")
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()

    bossdefeatrule(gold,plrhp)

    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp * buff - (opponentdmg)

    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))
    
    bossdefeatrule(gold,plrhp)

    # ROUND 3 TURN

    print("\n---" + name + "'s Turn ---")
    round2 = input("ROUND III! Would you like to attack, skill, or FLEE?")
    print("___________________________")
    print("!!           At this stage in the game, one turn should defeat the boss!")
    print("___________________________")
    if round2.lower() == "attack":
        roundhp = roundhp - attkdmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round2.lower() == "skill":
        roundhp = roundhp - skilldmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg * buff) + " damage!")
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()
    bossdefeatrule(gold,plrhp)

    # OPPONENT'S TURN

    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp * buff - (opponentdmg)

    bossdefeatrule(gold,plrhp)
    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))

    if plrhp > 0 and roundhp <= 0:
        print(" !!! ")
        print("You've successfully defeated the boss!")
        print(" !!! ")
        boss1defeated = True
        gold += 10000
        print("You now have " + str(gold) + " gold")
        main()
    else:
        print(" ")
        print(" !!! ")
        print("You havent sucessfully defeated the boss...")
        print("You've run out of turns! Returning to the home menu...")
        print(" !!! ")
        main()

# ///////////////BOSS 2, get dragon armour from this boss//////////////////
def boss2():
    global buff,attkopt,skillopt,armour,attkdmg,skilldmg,plrhp,gold,boss2defeated
    roundhp = 500
    print(armour)
    def boss2defeatrule(gold,plrhp):
        if roundhp <= 0 and plrhp >= 0:
            global boss2defeated
            print("    ")
            print(" !!! ")
            print("You've Won! 10000 gold has been added to your account,along with the dragon armour suit!")
            print(" !!! ")
            armour = armour + 4
            gold += gold + 10000
            plrhp = 100 * armour
            boss2defeated = True
            main()
        elif roundhp >= 0 and plrhp <= 0:
            print("    ")
            print(" !!! ")
            print("You've lost all of you hp and or you've run out of turns!")
            print("YOU LOOSE.....")
            print(" !!! ")
            print(" ")
            main()
        else:
            sleepge(3)

    print("\n---" + name + "'s Turn ---")
    round1 = input("do an Attack or Skill ")

    if round1 == "attack":
        roundhp = roundhp - (attkdmg * buff)
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round1 == "skill":
        roundhp = roundhp - (skilldmg * buff)
        skilluse + 1
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg * buff) + " damage!")

    boss2defeatrule(gold,plrhp)
    
    print("\n--- Opponents's Turn ---")
    print("Your oppoent invokes the power of lightning...")
    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp - (opponentdmg * 2 )

    if opponentdmg > 50:
        print("that was quite the hit...")
        print("your hp is... " + str(float(plrhp)))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(float(plrhp)))

    # ROUND 2 TURN
    print("\n---" + name + "'s Turn ---")
    print("")
    round2 = input("ROUND II! Would you like to attack, skill, or FLEE?")
    print(" ")
    if round2 == "attack":
        roundhp = roundhp - attkdmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round2 == "skill":
        if skilluse > 1:
            print("Sorry, but your SKILL is on ICD (internal cooldown)")
            a = input("Would you like to sacrifice a turn to get your skill back? (Y)es,(N)o")
            if a.upper() == "Y":
                print("Alright, skipping turn...")
                print("Your opponent dashes with the power of lightning...")
                opponentdmg = random.randint(1, 100)
                plrhp = plrhp - (opponentdmg * 10 )
                print("You currently have " + str(float(plrhp) + " HP left"))
                if plrhp > 0:
                    print("Activating Skill...")
                    roundhp = roundhp - skilldmg
                    print("The current boss health is... " + str(roundhp))
                    print("You dealt " + str(skilldmg) + " damage!")
                else:
                    lightningswhim = 0
                    if lightningswhim == 0:
                        print(" !!! ")
                        print("Secret Achievement unlocked: Lightning's whim..")
                        print("get struck down by the lightning prisim while on skill ICD")
                        lightningswhim = lightningswhim + 1
                        secretachievements = secretachievements + 1
                        gold = gold + 250
                    print(" !!! ")
                    print("You've died from the bosse's passive attack... Returning to main menu")
                    main()
        else:
            roundhp = roundhp - skilldmg * buff
            print("The current boss health is... " + str(roundhp))
            print("You dealt " + str(skilldmg * buff) + " damage!")
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()

    boss2defeatrule(gold,plrhp)

    # OPPONENT'S TURN
    print("Its now your opponent's turn")
    print("Your opponent conserves their elemental energy, prepairing for a blast...")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    plrhp = plrhp - (opponentdmg * 2 )

    if opponentdmg > 500:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))
    
    boss2defeatrule(gold,plrhp)

    # ROUND 3 TURN

    print("\n---" + name + "'s Turn ---")
    round2 = input("ROUND III! Would you like to attack, skill, or FLEE?")
    print("___________________________")
    print("!!           At this stage in the game, one turn should defeat the boss!")
    print("___________________________")
    if round2.lower() == "attack":
        roundhp = roundhp - attkdmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(attkdmg * buff) + " damage!")
    elif round2.lower() == "skill":
        roundhp = roundhp - skilldmg * buff
        print("The current boss health is... " + str(roundhp))
        print("You dealt " + str(skilldmg * buff) + " damage!")
    elif round2.lower() == "flee":
        print("L Bozo, You Just Fled the battle!")
        main()
    boss2defeatrule(gold,plrhp)

    # OPPONENT'S TURN

    print("Its now your opponent's turn")
    print("You opponent now harnesses their powers and puts them forth with a blast!")
    sleepge(3)

    opponentdmg = random.randint(1, 100)
    def dogechance(plrhp):
        y = random.randint(1,2)
        if y == 1:
            plrhp = plrhp - (opponentdmg * 10 )
        if y == 2:
            print("You sucessfully doged the blast!")
    dogechance()

    boss2defeatrule(gold,plrhp)
    if opponentdmg > 500:
        print("that was quite the hit...")
        print("your hp is... " + str(plrhp))
    else:
        opom = 0
        if opom == 0:
            print(" !!! ")
            print("Secret Achievement unlocked: Survival of 'Electrical Omniprescence'")
            print("Survive the maximum electrical current the lightning prisim offers")
            print(" !!! ")
            gold = gold + 250
            opom = opom + 1
            secretachievements = secretachievements + 1
        print("your opponent's turn has ended~ your current hp is..." + str(plrhp))

    if plrhp > 0 and roundhp <= 0:
        print(" !!! ")
        print("You've successfully defeated the boss!")
        print(" !!! ")
        print("You've gained the dragon armour!")
        armour = armour + 4
        boss2defeated = True
        gold += 10000
        print("You now have " + str(gold) + " gold")
        main()
    else:
        print(" ")
        print(" !!! ")
        print("You havent sucessfully defeated the boss...")
        print("You've run out of turns! Returning to the home menu...")
        print(" !!! ")
        main()


# ///////////////MAIN SCREEN//////////////////

def main():
    global gold,buff,plrhp
    print(plrhp)
    print(armour)
    if name.lower() == "dominik":
        print("Hej developer dom, you gained a grap ton of currency rn.")
        gold = gold + 1000000000000
    print("___________________________")
    print("Welcome to the main screen")
    print("________________________________")
    print("P.S. for advanced options, type in 'help'")
    print("___________________________")
    i1 = input("Would you like to take on a boss, fish, or go to the shop? ")
    print("additional options include gamble and statistics!")
    if i1.lower() == "boss":
        bosses()
    elif i1.lower() == "shop":
        shop(shopvisitcount,plrhp)
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
        print("current armour: " + str(armour) + " this value is multiplied by your hp")
        print("Secret achievements unlocked: " + str(secretachievements) + "/5")
        print("current armours in game: " + str(armourliszt))
        print("current fish in game: " + str(fishliszt))
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
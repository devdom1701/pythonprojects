import pygame
import random
from sys import exit

pygame.init()
pygame.display.set_caption("Phart")
screen = pygame.display.set_mode((800, 500))
        
# ____BIOME ASSETS____
sakuraalpha = 0
snowalpha = 0
scorealpha = 0

snoworigin = pygame.image.load('graphics/snowbg.png').convert_alpha()
snoworigin2 = pygame.image.load('graphics/snowbg2.png').convert_alpha()
snowsky = pygame.transform.scale(snoworigin, (800, 500)).convert_alpha()
snowsky2 = pygame.transform.scale(snoworigin2, (800, 500)).convert_alpha()
snowimage = pygame.image.load("graphics/snowfall.png").convert_alpha()
snowrect = snowimage.get_rect(midleft =(0,0))

sakuraorigin = pygame.image.load('graphics/sakurasky.png').convert_alpha()
sakuraorigin2 = pygame.image.load('graphics/sakurasky2.png').convert_alpha()
sakurasky = pygame.transform.scale(sakuraorigin, (800, 500)).convert_alpha()
sakurasky2 = pygame.transform.scale(sakuraorigin2, (800, 500)).convert_alpha()
sakura_image = pygame.image.load("graphics/sakuraleaves.png").convert_alpha()
sakura_rect = sakura_image.get_rect(midleft = (0,0))

currentbiome = ""

biomelist = []
#_____FISHES____
inventorylist = []
fishoutput = ""
# ____TEXTS_____
itemgotimage = pygame.image.load("graphics/itemobtain.png").convert_alpha()
itemgotimagerect = itemgotimage.get_rect()
itemgotfont = pygame.font.Font("font/Pixeltype.ttf", 34)
itemgotfont2 = pygame.font.Font("font/Pixeltype.ttf", 14)
itemgottext = itemgotfont.render(f"Obtained", True, "White")
itemgottextrect = itemgottext.get_rect(center = (55, 245))
itemgottextrect2 = itemgottext.get_rect(center = (60, 270))
itemgottag = True

itemgotalpha = 0
itemgottextalpha = 0
itemgottextalpha2 = 0

def display_score():
    global currency
    current_time = max(0, int((pygame.time.get_ticks() - start_time) / 1000))
    score = text_font.render(f'{currency}', False, "Gold")
    score_rect = score.get_rect(topleft=(0, 0))
    screen.blit(score, score_rect)

text_font = pygame.font.Font("font/Pixeltype.ttf", 40)

# ___PLAYER____

player1 = pygame.image.load('player/still.png').convert_alpha()
player_shadow1 = pygame.image.load('player/shadow.png').convert_alpha()

player = pygame.transform.scale2x(player1)
player_shadow = pygame.transform.scale2x(player_shadow1)
plrshadowrect = player_shadow.get_rect()

plr_gravity = 0
player_rect = player.get_rect(midbottom=(0, 500))

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

#____FISHING___
infishingzone = False
fishing = False
fishingfini = False
fishcheckflag = True
fishchecking = False
screen2tag = False

shopmusic = False
shopmusic_playing = False
snowmusic_playing = False
sakuramusicplaying = False

notenoughcurrencyerror = False
purchasesucesss = False
soldfishies = False

rarerodbought = False
masterrodbought = False
goldrodbought = False
kafaldaugerodbought = False
diffrenttab2 = False

errortextalpha = 255
purchasalpha = 255
fishingtimermultiplier = 0
rodgravitydecrease = 1
fishmultiplier = [1]
fishmultiplierint = 1
fishingpoints = 0
timertime = 0
fishingtimer = 0
scorealpha = 200
fishingrodgravity = 0
currency = 0

commonfishcount = 0
uncommonfishcount = 0
rarefishcount = 0
legendaryfishcount = 0
morbiusfishcount = 0
inventoryvalue = (commonfishcount * 1) + (uncommonfishcount * 2) + (rarefishcount * 5) + (legendaryfishcount * 10) + (morbiusfishcount * 20)

fishingrod = pygame.image.load('graphics/fishingrod.png').convert_alpha()
fishingbg = pygame.image.load('graphics/fishingbg.png').convert_alpha()

blur = pygame.image.load('graphics/blur.png').convert_alpha()
blurrect = blur.get_rect()

fishingrodrect = fishingrod.get_rect(center = (400,250))
fishingbgrect = fishingbg.get_rect()

            
# ____USER INPUT____
key_e = pygame.image.load('graphics/key_e.png').convert_alpha()
key_e_width = key_e.get_width() // 4
key_e_height = key_e.get_height() // 4
keye = pygame.transform.scale(key_e, (key_e_width, key_e_height))
keyerect = keye.get_rect(midleft=(327,369))

# ___Shop____
jumpscar = pygame.image.load('graphics/america.webp').convert_alpha()
shoppingshopgui = pygame.image.load('graphics/shoppinggui.png').convert_alpha()
shopactif = False
#_____Musique___
from pygame import mixer

pygame.mixer.init()
pygame.mixer.music.load("audio/sakura-main.wav")
pygame.mixer.music.play(loops=-99999)

sakuramusic = "audio/sakura-main.wav"
snowmusic = "audio/snow-main.wav"

sakuramusiclen = pygame.mixer.Sound(sakuramusic).get_length()
snowmusic_length = pygame.mixer.Sound(snowmusic).get_length()

def fade_out_music():
    volume = pygame.mixer.music.get_volume()
    volume -= 0.01
    if volume <= 0:
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.set_volume(volume)
# _________________________
def purchasesucess(message):
    global purchasalpha, purchasesucesss
    if purchasalpha > 0 and purchasesucesss:
        silly2 = pygame.font.Font("font/Pixeltype.ttf", 30)
        purchasetext = silly2.render(f"{message}!", True, "Green")
        purchasetextrect = purchasetext.get_rect(center = (400,460))
        purchasetext.set_alpha(purchasalpha)
        purchasalpha -= 2
        screen.blit(purchasetext, purchasetextrect)
    else:
        purchasesucesss = False
class Shop():
    def __init__(self,screen,itemimage,price,xpos,ypos,bg):
        self.screen = screen
        self.itemimage = itemimage
        self.price = price
        self.xpos = xpos
        self.ypos = ypos
        self.bg = bg
    def genshop(screen,bg):
        global shopactif, fishing, timertime, fishingpoints, uncommonfishcount, commonfishcount, rarefishcount, legendaryfishcount, morbiusfishcount, mousepos, morbiusfishcount, inventoryvalue, currency, rodgravitydecrease, fishingtimermultiplier, notenoughcurrencyerror,errortextalpha, purchasalpha, purchasesucesss,rarerodbought,masterrodbought,goldrodbought,kafaldaugerodbought,diffrenttab2,soldfishies
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            if not fishing and not fishchecking:
                shopactif = True
        if shopactif:
            if keys[pygame.K_2]:
                diffrenttab2 = True
                aaa = pygame.Rect((148, 395), (400, 500))
                silly2 = pygame.font.Font("font/Pixeltype.ttf", 30)
                inventoryvalue = (commonfishcount * 15) + (uncommonfishcount * 25) + (rarefishcount * 100) + (legendaryfishcount * 250) + (morbiusfishcount * 1000)
                invvaluetext = silly2.render(f"{inventoryvalue}", True, "Gold")
                
                bg = pygame.image.load('graphics/sellfishingui.png').convert_alpha()
                # (101,422);(187,421)||(282,423);(370,418)||(460,421);(545,422)||
                invvaluetextrect = invvaluetext.get_rect(midleft = (530,440))
                inventorytext = silly2.render(f"uncommon: {uncommonfishcount} common: {commonfishcount} rare: {rarefishcount}", True, "Black")
                inventorytext2 = silly2.render(f"legendary: {legendaryfishcount} morbin: {morbiusfishcount}", True, "Black")
                inventorytext2rect = inventorytext2.get_rect(center=(260, 280))
                inventorytextrect = inventorytext.get_rect(center=(260, 300))
                if event.type == pygame.MOUSEBUTTONDOWN and aaa.collidepoint(mousepos) and soldfishies == False:
                    soldfishies = True
                    if uncommonfishcount > 1:
                        uncommonfishcount = 0
                    if commonfishcount > 1:
                        commonfishcount = 0
                    if rarefishcount > 1:
                        rarefishcount = 0
                    if legendaryfishcount > 1:
                        legendaryfishcount = 0
                    if morbiusfishcount > 1:
                        morbiusfishcount = 0
                    currency += inventoryvalue
                else:
                    purchasesucess("Already sold fishies bro!!")
                if soldfishies == True:
                    inventoryvalue = 0
            else:
                diffrenttab2 = False
            
            jaa = pygame.Rect((82, 422),(100, 500))
            if event.type == pygame.MOUSEBUTTONDOWN and jaa.collidepoint(mousepos) and not diffrenttab2:
                if currency >= 1500:
                    fishingtimermultiplier = 2
                    rodgravitydecrease = 10
                    purchasalpha = 255
                    currency -= 15000
                    purchasesucesss = True
                    rarerodbought = True
                else:
                    notenoughcurrencyerror = True
                    errortextalpha = 255

            screen.blit(bg,(0,0))
            if keys[pygame.K_2]:
                screen.blit(inventorytext,inventorytextrect)
                screen.blit(inventorytext2,inventorytext2rect)
                screen.blit(invvaluetext,invvaluetextrect)
            if notenoughcurrencyerror and errortextalpha > 0:
                silly2 = pygame.font.Font("font/Pixeltype.ttf", 30)
                errortext = silly2.render(f"In order to purchase this item, you need {-(currency - 15000)} coins!", True, "Red")
                errorrect = errortext.get_rect(center = (400,460))
                errortext.set_alpha(errortextalpha)
                errortextalpha -= 5
                screen.blit(errortext, errorrect)
            
            purchasesucess("Purchase Sucessfull!")
            fishing = False
            timertime = 0
            fishingpoints = 0
        if keys[pygame.K_x]:
            shopactif = False
            soldfishies = False
    def createitem(screen,itemimage,xpos,ypos,price,pricex,pricey): #(76,76) first item, (117,201) price
        if shopactif:
            silly2 = pygame.font.Font("font/Pixeltype.ttf", 24)
            text = silly2.render(f"{price}" , True, 'Gold')
            textrect = text.get_rect(topleft = (pricex,pricey))

            screen.blit(itemimage,(xpos,ypos))
            screen.blit(text,textrect)

#____TESTING____
a = 0
#____BIOMES____
class Biome():
    def __init__(self,base,base2,shadowpresent):
        self.base = base
        self.base2 = base2 # BASE2 IS ONLY GROUND AND TRANSPARERENIZED WATER
        self.shadowpresent = shadowpresent
    
    def biomegen(base,base2,shadowpresent):
        global plr_gravity, player_shadow, plrshadowrect
        screen.blit(base, (0, 0))
        if shadowpresent == True:
            screen.blit(player_shadow, (player_rect.x - 0, player_rect.y + 65))
        if base2 is not None:
            screen.blit(base2, (0, 0))
        if base == sakurasky:
            biomelist.append("Sakura")
        elif base == snowsky:
            biomelist.append("Snow")

goup2 = False
def snowbiome():
    global infishingzone, currentbiome,snoworigin2, player_rect,snoworigin,snowsky,snowsky2,snowimage,snowrect,goup2,snowalpha
    currentbiome = "snow"
    snowimage.set_alpha(snowalpha)

    if not goup2:
        snowrect.y += 1
        snowalpha += 1
    else:
        snowalpha -= 10
        goup2 = False
        if snowalpha <= 0:
            snowrect.top = -snowrect.height

    if snowrect.bottom >= 450:
        goup2 = True
    
    if snowrect.top > 800:
        snowrect.top =- snowrect.height

    Biome.biomegen(snowsky, snowsky2, True)
    screen.blit(snowimage, snowrect)

    # borderzone = pygame.Rect(425, 387, 1, 1) # 425, 387 (snow)
    if player_rect.x >= 300: # 300 (snow)
        screen.blit(keye,keyerect)
        infishingzone = True
    else:
        infishingzone = False
    # if player_rect.colliderect(borderzone):
    #     player_rect = player.get_rect(midbottom=(355, 387))
    
goup = False

def sakurabiome():
    global infishingzone, player_rect, currentbiome, sakuraalpha, sakura_rect, sakura_image, goup
    currentbiome = "sakura"
    sakura_image.set_alpha(sakuraalpha)

    if not goup:
        sakura_rect.y += 1
        sakuraalpha += 1
    else:
        sakuraalpha -= 10
        goup = False
        if sakuraalpha <= 0:
            sakura_rect.top = -sakura_rect.height

    if sakura_rect.bottom >= 450:
        goup = True
    
    if sakura_rect.top > 800:
        sakura_rect.top =- sakura_rect.height

    Biome.biomegen(sakurasky, sakurasky2, True)
    screen.blit(sakura_image, sakura_rect)

    keyerect = keye.get_rect(midleft=(350, 369))

    if player_rect.x >= 240 and player_rect.x <= 500:
        screen.blit(keye, keyerect)
        infishingzone = True
    else:
        infishingzone = False

def plainsbiome():
    None
    # Biome.biomegen(plainssky,planssky2,True,boundry1,boundry2,fishingspot)
def mountianbiome():
    None
    # Biome.biomegen(mountiansky,mountiansky2,True,boundry1,boundry2,fishingspot)


def gradedisplay():
    global fishingpoints, fishoutput, fishmultiplier, fishcheckflag, fishing, scorealpha, inventorylist, commonfishcount, uncommonfishcount, rarefishcount, legendaryfishcount, morbiusfishcount, fishmultiplierint

    if fishingpoints <= 30:
        fishoutput = "NOTHING!"
    elif fishingpoints <= 35:
        fishoutput = "Common Fish"
    elif fishingpoints <= 45:
        fishoutput = "Common Fish"
    elif fishingpoints <= 50:
        fishoutput = "Uncommon Fish"
    elif fishingpoints <= 60:
        fishoutput = "Uncommon Fish"
    elif fishingpoints <= 75:
        fishoutput = "Rare Fish "
    elif fishingpoints <= 85:
        fishoutput = "Legendary Fish"
    elif fishingpoints <= 100:
        fishoutput = "Legendary Fish"
    elif fishingpoints <= 150:
        fishoutput = "MORBIUS Fish"
    elif fishingpoints <= 160:
        fishoutput = "MORBIUS Fish"
    

def fishcheck():
    global fishingpoints, fishoutput, fishmultiplier, fishcheckflag, fishing, scorealpha, inventorylist, commonfishcount, uncommonfishcount, rarefishcount, legendaryfishcount, morbiusfishcount, fishmultiplierint, fishchecking

    if fishingpoints <= 30:
        fishoutput = "NOTHING!"
    elif fishingpoints <= 35:
        if fishcheckflag:
            if "Common Fish" not in inventorylist:
                inventorylist.append("Common Fish")
                commonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Common Fish" in inventorylist:
                inventorylist.append("Common Fish")
                commonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 45:
        if fishcheckflag:
            if "Common Fish" not in inventorylist:
                inventorylist.append("Common Fish ")
                commonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Common Fish" in inventorylist:
                inventorylist.append("Common Fish")
                commonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 50:
        if fishcheckflag:
            if "Uncommon Fish" not in inventorylist:
                inventorylist.append("Uncommon Fish ")
                uncommonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Uncommon Fish" in inventorylist:
                inventorylist.append("Common Fish")
                uncommonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 60:
        if fishcheckflag:
            if "Uncommon Fish" not in inventorylist:
                inventorylist.append("Uncommon Fish ")
                uncommonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Uncommon Fish" in inventorylist:
                inventorylist.append("Common Fish")
                uncommonfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 75:
        if fishcheckflag:
            if "Rare Fish" not in inventorylist:
                inventorylist.append("Rare Fish")
                rarefishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Rare Fish" in inventorylist:
                inventorylist.append("Common Fish")
                rarefishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 85:
        if fishcheckflag:
            if "Legendary Fish" not in inventorylist:
                inventorylist.append("Legendary Fish")
                legendaryfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Legendary Fish" in inventorylist:
                inventorylist.append("Common Fish")
                legendaryfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 100:
        if fishcheckflag:
            if "Legendary Fish" not in inventorylist:
                inventorylist.append("Legendary Fish")
                legendaryfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Legendary Fish" in inventorylist:
                inventorylist.append("Legendary Fish")
                legendaryfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 150:
        if fishcheckflag:
            if "Morbius Fish" not in inventorylist:
                inventorylist.append("Morbius Fish")
                morbiusfishcount += 1 * fishmultiplierint
                fishcheckflag = False
            elif "Morbius Fish" in inventorylist:
                inventorylist.append("Morbius Fish")
                morbiusfishcount += 1 * fishmultiplierint
                fishcheckflag = False
    elif fishingpoints <= 151:
        if fishcheckflag:
            morbiusfishcount += 10
            fishcheckflag = False
    print()
    print(inventorylist,fishmultiplier)
    print(f"uncommon: {uncommonfishcount}", f"common: {commonfishcount}", f"rare: {rarefishcount}",f"legendary: {legendaryfishcount}",f"morbin: {morbiusfishcount}")
    print()

def fishingscore():
    global score, score_rect, fishingpoints, gradeaplha, scoreaplha, timertime
    silly2 = pygame.font.Font("font/Pixeltype.ttf", 50)
    score = silly2.render(f"Fishing Score: {fishingpoints}" , True, (64, 64, 64))
    grade = silly2.render(f" Grade: [F]", True, "Black")
    if fishingpoints <= 30:
            grade = silly2.render(f" Grade: [D]", True, "Red")
    elif fishingpoints <= 35:
        grade = silly2.render(f" Grade: [D+]", True, "Red")
    elif fishingpoints <= 45:
        grade = silly2.render(f" [C]", True, "Orange")
    elif fishingpoints <= 50:
        grade = silly2.render(f" [C+]", True, "Orange")
    elif fishingpoints <= 60:
        grade = silly2.render(f" [B-]", True, "Green")
    elif fishingpoints <= 75:
        grade = silly2.render(f" [B]", True, "Green")
    elif fishingpoints <= 80:
        grade = silly2.render(f" [B+]", True, "Green")
    elif fishingpoints <= 85:
        grade = silly2.render(f" [A-]", True, "Green")
    elif fishingpoints <= 95:
        grade = silly2.render(f" [A]", True, "Green")
    elif fishingpoints <= 100:
        grade = silly2.render(f" [A+]", True, "Green")
    elif fishingpoints <= 120 or fishingpoints >= 120:
        grade = silly2.render(f" [A++]", True, "Gold")

    grade_rect = grade.get_rect(midtop = (400, 0))
    score_rect = score.get_rect(center=(400, 45))
    screen.blit(score, score_rect)
    screen.blit(grade, grade_rect)

def fishingbanner():
    global scorealpha, fishingpoints, fishing, fishingfini, infishingzone, itemgotimage, itemgotimagerect,itemgotfont,itemgottag,itemgotalpha,itemgottextalpha,itemgottext,itemgottextrect,itemgottextalpha2, fishoutput, fishmultiplier, inventorylist, fishcheckflag, fishchecking
    fishchecking = True                                
    if fishingfini and not fishing:
        fishcheckflag = True

        silly2 = pygame.font.Font("font/Pixeltype.ttf", 45)
        score = silly2.render(f"Score: {fishingpoints} [F]", True, "Black")
        
        if fishingpoints <= 30:
            score = silly2.render(f"Score: {fishingpoints} [D]", True, "Red")
        elif fishingpoints <= 35:
            score = silly2.render(f"Score: {fishingpoints} [D+]", True, "Red")
        elif fishingpoints <= 45:
            score = silly2.render(f"Score: {fishingpoints} [C]", True, "Orange")
        elif fishingpoints <= 50:
            score = silly2.render(f"Score: {fishingpoints} [C+]", True, "Orange")
        elif fishingpoints <= 60:
            score = silly2.render(f"Score: {fishingpoints} [B-]", True, "Green")
        elif fishingpoints <= 75:
            score = silly2.render(f"Score: {fishingpoints} [B]", True, "Green")
        elif fishingpoints <= 80:
            score = silly2.render(f"Score: {fishingpoints} [B+]", True, "Green")
        elif fishingpoints <= 85:
            score = silly2.render(f"Score: {fishingpoints} [A-]", True, "Green")
        elif fishingpoints <= 95:
            score = silly2.render(f"Score: {fishingpoints} [A]", True, "Green")
        elif fishingpoints <= 100:
            score = silly2.render(f"Score: {fishingpoints} [A+]", True, "Green")
        elif fishingpoints <= 120 or fishingpoints >= 120:
            score = silly2.render(f"Score: {fishingpoints} [A++]", True, "Gold")
            

        score_rect = score.get_rect(center=(400, 45))
        itemgottext2 = itemgotfont2.render(f"{fishoutput}", True, "White")

        score.set_alpha(scorealpha)
        itemgotimage.set_alpha(itemgotalpha)
        itemgottext.set_alpha(itemgottextalpha)
        itemgottext2.set_alpha(itemgottextalpha2)
        

        if scorealpha != 0:
            scorealpha -= 1.5
            itemgotalpha -= 1.5
            itemgottextalpha -= 1.5
            itemgottextalpha2 -= 1.5
            infishingzone = False
            gradedisplay()

        if scorealpha == 0:
            infishingzone = True
            fishcheck()
            fishingpoints = 0
            fishoutput = "Aint Got Nun"
            fishchecking = False

        screen.blit(itemgotimage, itemgotimagerect)
        screen.blit(itemgottext, itemgottextrect)
        screen.blit(itemgottext2, itemgottextrect2)
        screen.blit(score, score_rect)
    
def timerdisplay():
    global timertime, score, score_rect, sessionalpha
    silly = pygame.font.Font("font/Pixeltype.ttf", 25)
    score = silly.render(f"{timertime}/{10 + fishingtimermultiplier}", False, "Red")
    score_rect = score.get_rect(center=(25, 480))
    screen.blit(score, score_rect)


while True:  # GAME START
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            a += 1
            if a % 2 > 0:
                plr_gravity = -10
        #____FISHING INTERFACE____
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and infishingzone:
            fishing = True

    if currentbiome == "":
        sakurabiome()
        print(biomelist)
    elif currentbiome == "sakura":
        sakurabiome()
    elif currentbiome == "snow":
        snowbiome()

    # ______CONTROLS______
    plr_gravity += 1
    player_rect.y += plr_gravity

    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000
    if keys[pygame.K_a]:
        player_rect.x -= 300 * dt
    if keys[pygame.K_d]:
        player_rect.x += 300 * dt

    # ___biome___
    if currentbiome == "snow":
        if player_rect.bottom >= 450:
            player_rect.bottom = 450
        if not snowmusic_playing:
            pygame.mixer.music.load(snowmusic)
            pygame.mixer.music.play(loops=-1)
            snowmusic_playing = True
            if sakuramusicplaying:
                sakuramusicplaying = False
        else:
            time_remaining = snowmusic_length - (pygame.mixer.music.get_pos() / 1000)
            if time_remaining < 10 and not fading_out:
                fade_out_music() 
                fading_out = True
            elif time_remaining >= 10:
                fading_out = False

    if currentbiome == "sakura":
        if player_rect.bottom >= 460:
            player_rect.bottom = 460
        if not sakuramusicplaying:
            pygame.mixer.music.load(sakuramusic)
            pygame.mixer.music.play(loops=-1)
            sakuramusicplaying = True
            if snowmusic_playing:
                snowmusic_playing = False
        else:
            sakuratimeremaining = sakuramusiclen - (pygame.mixer.music.get_pos() / 1000)
            if sakuratimeremaining < 10 and not fading_out:
                fade_out_music() 
                fading_out = True
            elif sakuratimeremaining >= 10:
                fading_out = False
        

    #____SCREEN BORDER_____
    if player_rect.left < 0:
        player_rect.x = 0
    elif player_rect.right > 800: # use this for terrain gen later
        player_rect.x = 800 - player_rect.width
        player_rect.x = 0
        currentbiome = random.choice(["sakura","snow"])
        print(currentbiome)

    if fishing:
        player_rect.x = 300
        fishingrodgravity += 1
        fishingrodrect.y += fishingrodgravity

        fishingtimer += 1
        if fishingtimer == 60:
            timertime += 1
            fishingtimer = 0
            if timertime == 10 + fishingtimermultiplier:
                fishing = False
                fishingfini = True
                scorealpha = 255
                itemgotalpha = 255
                itemgottextalpha = 255
                itemgottextalpha2 = 255
                timertime = 0
    
        if keys[pygame.K_w]:
            if fishingpoints >= 50:
                fishingrodgravity = -20 + rodgravitydecrease
            elif fishingpoints >= 70:
                fishingrodgravity = -80 + rodgravitydecrease
            elif fishingpoints >= 90:
                fishingrodgravity = -160 + rodgravitydecrease
            else:
                fishingrodgravity = -5

        if fishingrodrect.y <= 200 and fishingrodrect.y >= 172:
            fishingpoints += 1

        if fishingrodrect.bottom >= 450:
            fishingrodrect.bottom = 450

        if fishingrodrect.y <= 25:
            fishingrodrect.y = 25
        
        screen.blit(blur,(0,0))
        screen.blit(fishingbg,(0,0))
        fishingbg.set_alpha(220)
        if rarerodbought == True:
            fishingrod = pygame.image.load('graphics/rarerod.png').convert_alpha()
            screen.blit(fishingrod,fishingrodrect)
        screen.blit(fishingrod,fishingrodrect)
        fishingscore()
        timerdisplay()
    
    fishingbanner()
    screen.blit(player, player_rect)
    mousepos = pygame.mouse.get_pos()
    print(mousepos)
    print(shopactif)
    Shop.genshop(screen,shoppingshopgui)

    display_score()
    pygame.display.flip()
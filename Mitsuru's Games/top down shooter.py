from pygame.locals import *
import pygame
import sys
from random import randint
from time import sleep

FPS = 30

WINDOWWIDTH = 480
WINDOWHEIGHT = 640

BUTTONHEIGHT = 50
BUTTONWIDTH = 250
BUTTONLEFT = 115

BUTTON1TOP = 525
BUTTON2TOP = 425
BUTTON3TOP = 325
BUTTON4TOP = 225

BUTTON1 = pygame.Rect(BUTTONLEFT, BUTTON1TOP, BUTTONWIDTH, BUTTONHEIGHT)
BUTTON2 = pygame.Rect(BUTTONLEFT, BUTTON2TOP, BUTTONWIDTH, BUTTONHEIGHT)
BUTTON3 = pygame.Rect(BUTTONLEFT, BUTTON3TOP, BUTTONWIDTH, BUTTONHEIGHT)
BUTTON4 = pygame.Rect(BUTTONLEFT, BUTTON4TOP, BUTTONWIDTH, BUTTONHEIGHT)

BUTTONLIST = [BUTTON1TOP,BUTTON2TOP,BUTTON3TOP,BUTTON4TOP]

TITLEBOXHEIGHT = 130
TITLEBOXTOP = 50
TITLEBOXWIDTH = 400
TITLEBOXLEFT = 40

BACKBUTTONHEIGHT = 50
BACKBUTTONWIDTH = 125
BACKBUTTONLEFT = 50
BACKBUTTONTOP = 540
BACKBUTTON = pygame.Rect(BACKBUTTONLEFT, BACKBUTTONTOP, BACKBUTTONWIDTH, BACKBUTTONHEIGHT)

INSTRUCTIONSWIDTH = 350
INSTRUCTIONSHEIGHT = 475
INSTRUCTIONSLEFT = 65
INSTRUCTIONSTOP = 30
INSTRUCTIONSBUTTON = pygame.Rect(INSTRUCTIONSLEFT, INSTRUCTIONSTOP, INSTRUCTIONSWIDTH, INSTRUCTIONSHEIGHT)

HIGHLIGHTLIST = ["PLAY","OPTIONS","INSTRUCTIONS","QUIT"]
highlight = "PLAY"

play = False
instruction = False

SHIPBOXWIDTH = 48
SHIPBOXHEIGHT = 20
SHIPTRIANGLEHEIGHT = 30

ENEMYWIDTH = 15
ENEMYHEIGHT = 15

BOSSBOXWIDTH = 192
BOSSBOXHEIGHT = 30
BOSSTRIANGLEHEIGHT = 20
BOSSSHOOTERWIDTH = 5
BOSSSHOOTERHEIGHT = 10

PLAYERSHOOTINGRATE = 0
ENEMYSHOOTINGRATE = 0.01
BOSSSHOOTINGRATE = 0.75

#ENEMYLOCATION = (48, 96, 144, 192, 240, 288, 336, 384, 432)

"""
First level enemies - multiples of 2 on backmost row (dont forget 0)
Second level enemies - all odds on front row
Third level enemies - all on backrow, all odds on front row
Fourth level enemies - all on both backrow and front row
Fifth level - BOSS
"""
#movement restricted to +- 20

BACKROWY = 50
FRONTROWY = 75

ENEMYSHIP = pygame.image.load("ENEMYSHIP.PNG")
PLAYERSHIP = pygame.image.load("PLAYERSHIP.PNG")
PLAYERSHIP2 = pygame.image.load("PLAYERSHIP2.PNG")
HEART = pygame.image.load("HEART.PNG")

"""
player width is 48
player height is 37

blitz will spawn item at top left coordinate
"""

PLAYERMOVEBOX = 390

def main():
    global BLACK
    global WHITE
    global BLUE
    global GREY
    global YELLOW
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE = (0,0,225)
    GREY = (128,128,128)
    YELLOW = (255,255,0)
    global FPSCLOCK
    global DISPLAY
    global highlight
    global instruction
    global play
    enemy1 = None
    enemy2 = None
    enemy3 = None
    enemy4 = None
    enemy5 = None
    enemy6 = None
    enemy7 = None
    enemy8 = None
    enemy9 = None
    enemy10 = None
    enemy11 = None
    enemy12 = None
    enemy13 = None
    enemy14 = None
    enemy15 = None
    enemy16 = None
    enemy17 = None
    enemy18 = None
    enemylist = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11,enemy12,enemy13,enemy14,enemy15,enemy16,enemy17,enemy18]
    boss = False
    enemynumber = 0
    PLAYERX = 216
    PLAYERY = 550
    start = True
    gameover = False
    levelon = 1
    life = 10
    instruction = False
    menu = True
    fire = False
    god = False
    pygame.init()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Top Down Shooter")
    DISPLAY.fill(BLUE)
    displaymenuonce = True
    FPSCLOCK = pygame.time.Clock()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_w or event.key == K_UP) and HIGHLIGHTLIST.index(highlight) > 0:
                    if instruction == False:
                        displaymenuonce = True
                        highlight = HIGHLIGHTLIST[HIGHLIGHTLIST.index(highlight)-1]
                elif (event.key == K_s or event.key == K_DOWN) and HIGHLIGHTLIST.index(highlight) < 3:
                    if instruction == False:
                        displaymenuonce = True
                        highlight = HIGHLIGHTLIST[HIGHLIGHTLIST.index(highlight)+1]
                elif event.key == K_RETURN:
                    if instruction == True:
                        displaymenuonce = True
                        highlight = "INSTRUCTIONS"
                        instruction = False
                    elif highlight == "PLAY":
                        DISPLAY.fill(GREY)
                        play = True
                        leveltext = pygame.font.Font("freesansbold.ttf",32)
                        if levelon == 1:
                            levelsurface = leveltext.render("Level 1",True, WHITE, BLACK)
                        elif levelon == 2:
                            levelsurface = leveltext.render("Level 2", True, WHITE, BLACK)
                        elif levelon == 3:
                            levelsurface = leveltext.render("Level 3", True, WHITE, BLACK)
                        elif levelon == 4:
                            levelsurface = leveltext.render("Level 4", True, WHITE, BLACK)
                        elif levelon == 5:
                            levelsurface = leveltext.render("Level 5", True, WHITE, BLACK)
                        levelrect = levelsurface.get_rect()
                        levelrect.center = (240, 320)
                        DISPLAY.blit(levelsurface, levelrect)
                        pygame.display.update()
                        sleep(1.5)
                        DISPLAY.fill(BLACK)
                        alternate = "LEFT"
                    elif highlight == "OPTIONS":
                        print "options"
                    elif highlight == "INSTRUCTIONS":
                        instruction = True
                        INSTRUCTIONS()
                    elif highlight == "QUIT":
                        pygame.quit()
                        sys.exit()
        if menu:
            if displaymenuonce:
                DISPLAY.fill(BLUE)
                displaymenuonce = False
                menudisplay()
                DISPLAY.blit(button1surface, button1rect)
                DISPLAY.blit(button2surface, button2rect)
                DISPLAY.blit(button3surface, button3rect)
                DISPLAY.blit(button4surface, button4rect)
        while play:
            DISPLAY.fill(BLACK)
            if start:
                enemy1 = True
                enemy2 = True
                enemy3 = True
                enemy4 = True
                enemy5 = True
                enemy6 = True
                enemy7 = True
                enemy8 = True
                enemy9 = True
                enemy10 = True
                enemy11 = True
                enemy12 = True
                enemy13 = True
                enemy14 = True
                enemy15 = True
                enemy16 = True
                enemy17 = True
                enemy18 = True
                enemy1life = True
                enemy2life = True
                enemy3life = True
                enemy4life = True
                enemy5life = True
                enemy6life = True
                enemy7life = True
                enemy8life = True
                enemy9life = True
                enemy10life = True
                enemy11life = True
                enemy12life = True
                enemy13life = True
                enemy14life = True
                enemy15life = True
                enemy16life = True
                enemy17life = True
                enemy18life = True
                enemy1counter = 0
                enemy2counter = 0
                enemy3counter = 0
                enemy4counter = 0
                enemy5counter = 0
                enemy6counter = 0
                enemy7counter = 0
                enemy8counter = 0
                enemy9counter = 0
                enemy10counter = 0
                enemy11counter = 0
                enemy12counter = 0
                enemy13counter = 0
                enemy14counter = 0
                enemy15counter = 0
                enemy16counter = 0
                enemy17counter = 0
                enemy18counter = 0
                movingup = False
                movingleft = False
                movingright = False
                movingdown = False
                shooting = False
                PLAYERX = 216
                PLAYERY = 550
                invinciblecounter = 0
                playershootcounter = 0
                playerhit = False
                playershoot = True
                BULLETX = []
                BULLETY = []
                PLAYERBULLETX = []
                PLAYERBULLETY = []
                playercanshoot = True
                enemynumber += 1
                start = False
                SPAWNBACK = []
                SPAWNFRONT = []
                #24.5 is center
                center = 24
                if levelon == 1:
                    SPAWNBACK = {48, 144, 240, 336, 432}
            
                    enemynumber = 5
        
                    enemy1left = 48 - center
                    enemy1top = BACKROWY #50
                
                    enemy2left = 144 - center
                    enemy2top = BACKROWY
        
                    enemy3left = 240 - center
                    enemy3top = BACKROWY

                    enemy4left = 336 - center
                    enemy4top = BACKROWY

                    enemy5left = 432 - center
                    enemy5top = BACKROWY
                elif levelon == 2:

                    enemynumber = 9
        
                    SPAWNBACK = {48, 144, 240, 336, 432}
                    SPAWNFRONT = {96, 192, 288, 384}

                    enemy1left = 48 - center
                    enemy1top = BACKROWY #50
        
                    enemy2left = 144 - center
                    enemy2top = BACKROWY
        
                    enemy3left = 240 - center
                    enemy3top = BACKROWY

                    enemy4left = 336 - center
                    enemy4top = BACKROWY

                    enemy5left = 432 - center
                    enemy5top = BACKROWY

                    enemy6left = 96 - center
                    enemy6top = FRONTROWY

                    enemy7left = 192 - center
                    enemy7top = FRONTROWY

                    enemy8left = 288 - center
                    enemy8top = FRONTROWY

                    enemy9left = 384 - center
                    enemy9top = FRONTROWY
                elif levelon == 3:

                    enemynumber = 13
        
                    SPAWNBACK = {48, 96, 144, 192, 240, 288, 336, 384, 432}
                    SPAWNFRONT = {96, 192, 288, 384}

                    enemy1left = 48 - center
                    enemy1top = BACKROWY
        
                    enemy2left = 96 - center
                    enemy2top = BACKROWY

                    enemy3left = 144 - center
                    enemy3top = BACKROWY

                    enemy4left = 192 - center
                    enemy4top = BACKROWY

                    enemy5left = 240 - center
                    enemy5top = BACKROWY

                    enemy6left = 288 - center
                    enemy6top = BACKROWY

                    enemy7left = 336 - center
                    enemy7top = BACKROWY

                    enemy8left = 384 - center
                    enemy8top = BACKROWY
            
                    enemy9left = 432 - center
                    enemy9top = BACKROWY

                    enemy10left = 96 - center
                    enemy10top = FRONTROWY

                    enemy11left = 192 - center
                    enemy11top = FRONTROWY

                    enemy12left = 288 - center
                    enemy12top = FRONTROWY

                    enemy13left = 384 - center
                    enemy13top = FRONTROWY
        
                elif levelon == 4:

                    enemynumber = 18
        
                    SPAWNBACK = {48, 96, 144, 192, 240, 288, 336, 384, 432}
                    SPAWNFRONT = {48, 96, 144, 192, 240, 288, 336, 384, 432}

                    enemy1left = 48 - center
                    enemy1top = BACKROWY
                
                    enemy2left = 96 - center
                    enemy2top = BACKROWY

                    enemy3left = 144 - center
                    enemy3top = BACKROWY

                    enemy4left = 192 - center
                    enemy4top = BACKROWY

                    enemy5left = 240 - center
                    enemy5top = BACKROWY

                    enemy6left = 288 - center
                    enemy6top = BACKROWY

                    enemy7left = 336 - center
                    enemy7top = BACKROWY

                    enemy8left = 384 - center
                    enemy8top = BACKROWY

                    enemy9left = 432 - center
                    enemy9top = BACKROWY

                    enemy10left = 48 - center
                    enemy10top = FRONTROWY
        
                    enemy11left = 96 - center
                    enemy11top = FRONTROWY

                    enemy12left = 144 - center
                    enemy12top = FRONTROWY

                    enemy13left = 192 - center
                    enemy13top = FRONTROWY

                    enemy14left = 240 - center
                    enemy14top = FRONTROWY

                    enemy15left = 288 - center
                    enemy15top = FRONTROWY

                    enemy16left = 336 - center
                    enemy16top = FRONTROWY

                    enemy17left = 384 - center
                    enemy17top = FRONTROWY

                    enemy18left = 432 - center
                    enemy18top = FRONTROWY

                elif levelon == 5:
                    print "level is 5"
                enemy1timer = randint(3,5)*15
                enemy2timer = randint(3,5)*15
                enemy3timer = randint(3,5)*15
                enemy4timer = randint(3,5)*15
                enemy5timer = randint(3,5)*15
                enemy6timer = randint(3,5)*15
                enemy7timer = randint(3,5)*15
                enemy8timer = randint(3,5)*15
                enemy9timer = randint(3,5)*15
                enemy10timer = randint(3,5)*15
                enemy11timer = randint(3,5)*15
                enemy12timer = randint(3,5)*15
                enemy13timer = randint(3,5)*15
                enemy14timer = randint(3,5)*15
                enemy15timer = randint(3,5)*15
                enemy16timer = randint(3,5)*15
                enemy17timer = randint(3,5)*15
                enemy18timer = randint(3,5)*15
#{48, 96, 144, 192, 240, 288, 336, 384, 432}
#center = 24
            if enemynumber >= 5:
                if enemy1life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy1left, enemy1top))
                if enemy2life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy2left, enemy2top))
                if enemy3life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy3left, enemy3top))
                if enemy4life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy4left, enemy4top))
                if enemy5life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy5left, enemy5top))
                if alternate == "LEFT":
                    enemy1left -= 3
                    enemy2left -= 3
                    enemy3left -= 3
                    enemy4left -= 3
                    enemy5left -= 3
                    if enemy1left < 4:
                        alternate = "RIGHT"
                elif alternate == "RIGHT":
                    enemy1left += 3
                    enemy2left += 3
                    enemy3left += 3
                    enemy4left += 3
                    enemy5left += 3
                    if enemy1left > 44:
                        alternate = "LEFT"
            if enemynumber >= 9:
                if enemy6life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy6left, enemy6top))
                if enemy7life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy7left, enemy7top))
                if enemy8life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy8left, enemy8top))
                if enemy9life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy9left, enemy9top))
                if alternate == "LEFT":
                    enemy6left -= 3
                    enemy7left -= 3
                    enemy8left -= 3
                    enemy9left -= 3
                elif alternate == "RIGHT":
                    enemy6left += 3
                    enemy7left += 3
                    enemy8left += 3
                    enemy9left += 3
            if enemynumber >= 13:
                if enemy10life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy10left, enemy10top))
                if enemy11life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy11left, enemy11top))
                if enemy12life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy12left, enemy12top))
                if enemy13life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy13left, enemy13top))
                if alternate == "LEFT":
                    enemy10left -= 5
                    enemy11left -= 5
                    enemy12left -= 5
                    enemy13left -= 5
                elif alternate == "RIGHT":
                    enemy10left += 5
                    enemy11left += 5
                    enemy12left += 5
                    enemy13left += 5
            if enemynumber >= 18:
                if enemy14life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy14left, enemy14top))
                if enemy15life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy15left, enemy15top))
                if enemy16life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy16left, enemy16top))
                if enemy17life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy17left, enemy17top))
                if enemy18life != False:
                    DISPLAY.blit(ENEMYSHIP, (enemy18left, enemy18top))
                if alternate == "LEFT":
                    enemy14left -= 5
                    enemy15left -= 5
                    enemy16left -= 5
                    enemy17left -= 5
                    enemy18left -= 5
                elif alternate == "RIGHT":
                    enemy14left += 5
                    enemy15left += 5
                    enemy16left += 5
                    enemy17left += 5
                    enemy18left += 5
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.key == K_UP and event.type == KEYDOWN and PLAYERY >= PLAYERMOVEBOX:
                    movingup = True
                    movingdown = False
                    movingleft = False
                    movingright = False
                if event.key == K_DOWN and event.type == KEYDOWN and PLAYERY <= 545:
                    movingdown = True
                    movingup= False
                    movingleft = False
                    movingright = False
                if event.key == K_LEFT and event.type == KEYDOWN and PLAYERX >= 0:
                    movingleft = True
                    movingup = False
                    movingdown = False
                    movingright = False
                if event.key == K_RIGHT and event.type == KEYDOWN and PLAYERX <= 432:
                    movingright = True
                    movingup = False
                    movingleft = False
                    movingdown = False
                if event.key == K_SPACE and event.type == KEYDOWN:
                    shooting = True
                if event.key == K_UP and event.type == KEYUP:
                    movingup = False
                if event.key == K_DOWN and event.type == KEYUP:
                    movingdown = False
                if event.key == K_LEFT and event.type == KEYUP:
                    movingleft = False
                if event.key == K_RIGHT and event.type == KEYUP:
                    movingright = False
                if event.key == K_SPACE and event.type == KEYUP:
                    shooting = False
                if event.key == K_1:
                    god = True
                if event.key == K_2:
                    god = False
                if event.key == K_3:
                    fire = True
                if event.key == K_4:
                    fire = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
#19.5(center),27(top)
#-24
            if movingup == True and PLAYERY >= PLAYERMOVEBOX:
                PLAYERY -= 5
            if PLAYERY < PLAYERMOVEBOX:
                movingup = False
            if movingdown == True and PLAYERY <= 545:
                PLAYERY += 5
            if PLAYERY > 545:
                movingdown = False
            if movingleft == True and PLAYERX >= 0:
                PLAYERX -= 5
            if PLAYERX < 0:
                movingleft = False
            if movingright == True and PLAYERX <= 432:
                PLAYERX += 5
            if PLAYERX > 432:
                movingright = False
            if shooting and playershoot:
                playershoot = False
                PLAYERBULLETX.append(PLAYERX + 19)
                PLAYERBULLETY.append(PLAYERY)
            if not playershoot:
                shooting = False
            if enemynumber >= 5:
                if enemy1life != False:
                    if enemy1 == True:
                        enemy1 = False
                        BULLETX.append(enemy1left+10)
                        BULLETY.append(enemy1top+27)
                if enemy2life != False:
                    if enemy2 == True:
                        enemy2 = False
                        BULLETX.append(enemy2left+10)
                        BULLETY.append(enemy2top+27)
                if enemy3life != False:
                    if enemy3 == True:
                        enemy3 = False
                        BULLETX.append(enemy3left+10)
                        BULLETY.append(enemy3top+27)
                if enemy4life != False:
                    if enemy4 == True:
                        enemy4 = False
                        BULLETX.append(enemy4left+10)
                        BULLETY.append(enemy4top+27)
                if enemy5life != False:
                    if enemy5 == True:
                        enemy5 = False
                        BULLETX.append(enemy5left+10)
                        BULLETY.append(enemy5top+27)
            if enemynumber >= 9:
                if enemy6life != False:
                    if enemy6 == True:
                        enemy6 = False
                        BULLETX.append(enemy6left+10)
                        BULLETY.append(enemy6top+27)
                if enemy7life != False:
                    if enemy7 == True:
                        enemy7 = False
                        BULLETX.append(enemy7left+10)
                        BULLETY.append(enemy7top+27)
                if enemy8life != False:
                    if enemy8 == True:
                        enemy8 = False
                        BULLETX.append(enemy8left+10)
                        BULLETY.append(enemy8top+27)
                if enemy9life != False:
                    if enemy9 == True:
                        enemy9 = False
                        BULLETX.append(enemy9left+10)
                        BULLETY.append(enemy9top+27)
            if enemynumber >= 13:
                if enemy10life != False:
                    if enemy10 == True:
                        enemy10 = False
                        BULLETX.append(enemy10left+10)
                        BULLETY.append(enemy10top+27)
                if enemy11life != False:
                    if enemy11 == True:
                        enemy11 = False
                        BULLETX.append(enemy11left+10)
                        BULLETY.append(enemy11top+27)
                if enemy12life != False:
                    if enemy12 == True:
                        enemy12 = False
                        BULLETX.append(enemy12left+10)
                        BULLETY.append(enemy12top+27)
                if enemy13life != False:
                    if enemy13 == True:
                        enemy13 = False
                        BULLETX.append(enemy13left+10)
                        BULLETY.append(enemy13top+27)
            if enemynumber >= 18:
                if enemy14life != False:
                    if enemy14 == True:
                        enemy14 = False
                        BULLETX.append(enemy14left+10)
                        BULLETY.append(enemy14top+27)
                if enemy15life != False:
                    if enemy15 == True:
                        enemy15 = False
                        BULLETX.append(enemy15left+10)
                        BULLETY.append(enemy15top+27)
                if enemy16life != False:
                    if enemy16 == True:
                        enemy16 = False
                        BULLETX.append(enemy16left+10)
                        BULLETY.append(enemy16top+27)
                if enemy17life != False:
                    if enemy17 == True:
                        enemy17 = False
                        BULLETX.append(enemy17left+10)
                        BULLETY.append(enemy17top+27)
                if enemy18life != False:
                    if enemy18 == True:
                        enemy18 = False
                        BULLETX.append(enemy18left+10)
                        BULLETY.append(enemy18top+27)
            if playershoot == False:
                playershootcounter += 1
                if fire:
                    playershootcounter += 50
                if playershootcounter >= 50:
                    playershootcounter = 0
                    playershoot = True
            DISPLAY.blit(PLAYERSHIP, (PLAYERX, PLAYERY))
            if playerhit == True:
                DISPLAY.blit(PLAYERSHIP2, (PLAYERX, PLAYERY))
            if enemy1 == False:
                enemy1counter += 1
                if enemy1counter >= enemy1timer:
                    enemy1counter = 0
                    enemy1 = True
                    enemy1timer = randint(0,3)*15
            if enemy2 == False:
                enemy2counter +=1
                if enemy2counter >= enemy2timer:
                    enemy2counter = 0
                    enemy2 = True
                    enemy2timer = randint(0,3)*15
            if enemy3 == False:
                enemy3counter += 1
                if enemy3counter >= enemy3timer:
                    enemy3counter = 0
                    enemy3 = True
                    enemy3timer = randint(0,3)*15
            if enemy4 == False:
                enemy4counter += 1
                if enemy4counter >= enemy4timer:
                    enemy4counter = 0
                    enemy4 = True
                    enemy4timer = randint(0,3)*15
            if enemy5 == False:
                enemy5counter += 1
                if enemy5counter >= enemy5timer:
                    enemy5counter = 0
                    enemy5 = True
                    enemy5timer = randint(0,3)*15
            if enemy6 == False:
                enemy6counter += 1
                if enemy6counter >= enemy6timer:
                    enemy6counter = 0
                    enemy6 = True
                    enemy6timer = randint(0,3)*15
            if enemy7 == False:
                enemy7counter += 1
                if enemy7counter >= enemy7timer:
                    enemy7counter = 0
                    enemy7 = True
                    enemy7timer = randint(0,3)*15
            if enemy8 == False:
                enemy8counter += 1
                if enemy8counter >= enemy8timer:
                    enemy8counter = 0
                    enemy8 = True
                    enemy8timer = randint(0,3)*15
            if enemy9 == False:
                enemy9counter += 1
                if enemy9counter >= enemy9timer:
                    enemy9counter = 0
                    enemy9 = True
                    enemy9timer = randint(0,3)*15
            if enemy10 == False:
                enemy10counter += 1
                if enemy10counter >= enemy10timer:
                    enemy10counter = 0
                    enemy10 = True
                    enemy10timer = randint(0,3)*15
            if enemy11 == False:
                enemy11counter += 1
                if enemy11counter >= enemy11timer:
                    enemy11counter = 0
                    enemy11 = True
                    enemy11timer = randint(0,3)*15
            if enemy12 == False:
                enemy12counter += 1
                if enemy12counter >= enemy12timer:
                    enemy12counter = 0
                    enemy12= True
                    enemy12timer = randint(0,3)*15
            if enemy13 == False:
                enemy13counter += 1
                if enemy13counter >= enemy13timer:
                    enemy13counter = 0
                    enemy13 = True
                    enemy13timer = randint(0,3)*15
            if enemy14 == False:
                enemy14counter += 1
                if enemy14counter >= enemy14timer:
                    enemy14counter = 0
                    enemy14 = True
                    enemy14timer = randint(0,3)*15
            if enemy15 == False:
                enemy15counter += 1
                if enemy15counter >= enemy15timer:
                    enemy15counter = 0
                    enemy15 = True
                    enemy15timer = randint(0,3)*15
            if enemy16 == False:
                enemy16counter += 1
                if enemy16counter >= enemy16timer:
                    enemy16counter = 0
                    enemy16 = True
                    enemy16timer = randint(0,3)*15
            if enemy17 == False:
                enemy17counter += 1
                if enemy17counter >= enemy17timer:
                    enemy17counter = 0
                    enemy17 = True
                    enemy17timer = randint(0,3)*15
            if enemy18 == False:
                enemy18counter += 1
                if enemy18counter >= enemy18timer:
                    enemy18counter = 0
                    enemy18 = True
                    enemy18timer = randint(0,3)*15
            i = 0
            c = 0
            while c < len(BULLETX)-1:
                c+=1
                pygame.draw.line(DISPLAY,WHITE,(BULLETX[i],BULLETY[i]),(BULLETX[i],BULLETY[i]+5))
                if not god:
                    if invinciblecounter >= 75:
                        playerhit = False
                if not god:
                    if BULLETX[i] >= PLAYERX and BULLETX[i] <= PLAYERX + 27*1.75 and BULLETY[i] >= PLAYERY and BULLETY[i] <= PLAYERY + 38 and playerhit == False:
                        life -= 1
                        invinciblecounter = 0
                        playerhit = True
                        if life<=0:
                            play = False
                            gameover = True
                BULLETY[i] += 3
                if BULLETY[i] >= 640:
                    del BULLETX[i]
                    del BULLETY[i]
                i+=1
            i = 0
            c = -1
            while c < len(PLAYERBULLETX)-1:
                c+= 1
                pygame.draw.line(DISPLAY,WHITE,(PLAYERBULLETX[i]+5,PLAYERBULLETY[i]),(PLAYERBULLETX[i]+5,PLAYERBULLETY[i]-10))
                PLAYERBULLETY[i] -= 3
                if PLAYERBULLETY[i] <= 0:
                    del PLAYERBULLETX[i]
                    del PLAYERBULLETY[i]
                i+=1
            i = 0
            c = -1
            while c <len(PLAYERBULLETX)-1:
                if enemynumber >= 5:
                    if enemy1life:
                        if (PLAYERBULLETX[i] >= enemy1left) and PLAYERBULLETX[i] <= (enemy1left + 40) and PLAYERBULLETY[i] >= enemy1top and PLAYERBULLETY[i] <= enemy1top+27:
                            enemy1life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy2life:
                        if (PLAYERBULLETX[i] >= enemy2left) and PLAYERBULLETX[i] <= (enemy2left + 40) and PLAYERBULLETY[i] >= enemy2top and PLAYERBULLETY[i] <= enemy2top+27:
                            enemy2life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy3life:
                        if (PLAYERBULLETX[i] >= enemy3left) and PLAYERBULLETX[i] <= (enemy3left + 40) and PLAYERBULLETY[i] >= enemy3top and PLAYERBULLETY[i] <= enemy3top+27:
                            enemy3life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy4life:
                        if (PLAYERBULLETX[i] >= enemy4left) and PLAYERBULLETX[i] <= (enemy4left + 40) and PLAYERBULLETY[i] >= enemy4top and PLAYERBULLETY[i] <= (enemy4top+27):
                            enemy4life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy5life:
                        if (PLAYERBULLETX[i] >= enemy5left) and PLAYERBULLETX[i] <= (enemy5left + 40) and PLAYERBULLETY[i] >= enemy5top and PLAYERBULLETY[i] <= enemy5top+27:
                            enemy5life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemynumber == 5 and enemy1life == False and enemy2life == False and enemy3life == False and enemy4life == False and enemy5life == False:
                        start = True
                        levelon = 2
                        DISPLAY.fill(GREY)
                        leveltext = pygame.font.Font("freesansbold.ttf",32)
                        levelsurface = leveltext.render("Level 2", True, WHITE, BLACK)
                        levelrect = levelsurface.get_rect()
                        levelrect.center = (240, 320)
                        DISPLAY.blit(levelsurface, levelrect)
                        pygame.display.update()
                        sleep(1.5)
                        DISPLAY.fill(WHITE)
                        alternate = "LEFT"
                        PLAYERBULLETX = []
                        PLAYERBULLETY = []
                        BULLETX = []
                        BULLETY = []
                if enemynumber >= 9:
                    if enemy6life:
                        if PLAYERBULLETX[i] >= (enemy6left) and PLAYERBULLETX[i] <= (enemy6left + 40) and PLAYERBULLETY[i] >= enemy6top and PLAYERBULLETY[i] <= enemy6top+27:
                            enemy6life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy7life:
                        if PLAYERBULLETX[i] >= (enemy7left) and PLAYERBULLETX[i] <= (enemy7left + 40) and PLAYERBULLETY[i] >= enemy7top and PLAYERBULLETY[i] <= enemy7top+27:
                            enemy7life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy8life:
                        if PLAYERBULLETX[i] >= (enemy8left) and PLAYERBULLETX[i] <= (enemy8left + 40) and PLAYERBULLETY[i] >= enemy8top and PLAYERBULLETY[i] <= enemy8top+27:
                            enemy8life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy9life:
                        if PLAYERBULLETX[i] >= (enemy9left) and PLAYERBULLETX[i] <= (enemy9left + 40) and PLAYERBULLETY[i] >= enemy9top and PLAYERBULLETY[i] <= enemy9top+27:
                            enemy9life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemynumber == 9 and enemy1life == False and enemy2life == False and enemy3life == False and enemy4life == False and enemy5life == False and enemy6life == False and enemy7life == False and enemy8life == False and enemy9life == False:
                        start = True
                        levelon = 3
                        DISPLAY.fill(GREY)
                        leveltext = pygame.font.Font("freesansbold.ttf",32)
                        levelsurface = leveltext.render("Level 3", True, WHITE, BLACK)
                        levelrect = levelsurface.get_rect()
                        levelrect.center = (240, 320)
                        DISPLAY.blit(levelsurface, levelrect)
                        pygame.display.update()
                        sleep(1.5)
                        DISPLAY.fill(WHITE)
                        alternate = "LEFT"
                        PLAYERBULLETX = []
                        PLAYERBULLETY = []
                        BULLETX = []
                        BULLETY = []
                if enemynumber >= 13:
                    if enemy10life:
                        if PLAYERBULLETX[i] >= (enemy10left) and PLAYERBULLETX[i] <= (enemy10left + 40) and PLAYERBULLETY[i] >= enemy10top and PLAYERBULLETY[i] <= enemy10top+27:
                            enemy10life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy11life:
                        if PLAYERBULLETX[i] >= (enemy11left) and PLAYERBULLETX[i] <= (enemy11left + 40) and PLAYERBULLETY[i] >= enemy11top and PLAYERBULLETY[i] <= enemy11top+27:
                            enemy11life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy12life:
                        if PLAYERBULLETX[i] >= (enemy12left) and PLAYERBULLETX[i] <= (enemy12left + 40) and PLAYERBULLETY[i] >= enemy12top and PLAYERBULLETY[i] <= enemy12top+27:
                            enemy12life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemy13life:
                        if PLAYERBULLETX[i] >= (enemy13left) and PLAYERBULLETX[i] <= (enemy13left + 40) and PLAYERBULLETY[i] >= enemy13top and PLAYERBULLETY[i] <= enemy13top+27:
                            enemy13life = False
                            del PLAYERBULLETX[i]
                            del PLAYERBULLETY[i]
                    if enemynumber == 13 and enemy1life == False and enemy2life == False and enemy3life == False and enemy4life == False and enemy5life == False and enemy6life == False and enemy7life == False and enemy8life == False and enemy9life == False and enemy10life == False and enemy11life == False and enemy12life == False and enemy13life == False:
                        start = True
                        levelon = 4
                        DISPLAY.fill(GREY)
                        leveltext = pygame.font.Font("freesansbold.ttf",32)
                        levelsurface = leveltext.render("Level 4", True, WHITE, BLACK)
                        levelrect = levelsurface.get_rect()
                        levelrect.center = (240, 320)
                        DISPLAY.blit(levelsurface, levelrect)
                        pygame.display.update()
                        sleep(1.5)
                        DISPLAY.fill(WHITE)
                        alternate = "LEFT"
                        PLAYERBULLETX = []
                        PLAYERBULLETY = []
                        BULLETX = []
                        BULLETY = []
                if enemynumber >= 18:
                    if PLAYERBULLETX[i] >= (enemy14left) and PLAYERBULLETX[i] <= (enemy14left + 40) and PLAYERBULLETY[i] >= enemy14top and PLAYERBULLETY[i] <= enemy14top+27:
                        enemy14life = False
                        del PLAYERBULLETX[i]
                        del PLAYERBULLETY[i]
                    if PLAYERBULLETX[i] >= (enemy15left) and PLAYERBULLETX[i] <= (enemy15left + 40) and PLAYERBULLETY[i] >= enemy15top and PLAYERBULLETY[i] <= enemy15top+27:
                        enemy15life = False
                        del PLAYERBULLETX[i]
                        del PLAYERBULLETY[i]
                    if PLAYERBULLETX[i] >= (enemy16left) and PLAYERBULLETX[i] <= (enemy16left + 40) and PLAYERBULLETY[i] >= enemy16top and PLAYERBULLETY[i] <= enemy16top+27:
                        enemy16life = False
                        del PLAYERBULLETX[i]
                        del PLAYERBULLETY[i]
                    if PLAYERBULLETX[i] >= (enemy17left) and PLAYERBULLETX[i] <= (enemy17left + 40) and PLAYERBULLETY[i] >= enemy17top and PLAYERBULLETY[i] <= enemy17top+27:
                        enemy17life = False
                        del PLAYERBULLETX[i]
                        del PLAYERBULLETY[i]
                    if PLAYERBULLETX[i] >= (enemy18left) and PLAYERBULLETX[i] <= (enemy18left + 40) and PLAYERBULLETY[i] >= enemy18top and PLAYERBULLETY[i] <= enemy18top+27:
                        enemy18life = False
                        del PLAYERBULLETX[i]
                        del PLAYERBULLETY[i]
                    if enemynumber == 18 and enemy1life == False and enemy2life == False and enemy3life == False and enemy4life == False and enemy5life == False and enemy6life == False and enemy7life == False and enemy8life == False and enemy9life == False and enemy10life == False and enemy11life == False and enemy12life == False and enemy13life == False and enemy14== False and enemy15life == False and enemy16life == False and enemy17life == False and enemy18life == False:
                        start = True
                        levelon = 5
                        DISPLAY.fill(GREY)
                        leveltext = pygame.font.Font("freesansbold.ttf",32)
                        levelsurface = leveltext.render("Level 5", True, WHITE, BLACK)
                        levelrect = levelsurface.get_rect()
                        levelrect.center = (240, 320)
                        DISPLAY.blit(levelsurface, levelrect)
                        pygame.display.update()
                        sleep(1.5)
                        DISPLAY.fill(WHITE)
                        alternate = "LEFT"
                        PLAYERBULLETX = []
                        PLAYERBULLETY = []
                        BULLETX = []
                        BULLETY = []
                c += 1
                i += 1
            if life >= 1:
                DISPLAY.blit(HEART,(480-30-16,590))
            if life >= 2:
                DISPLAY.blit(HEART,(480-60-16*2,590))
            if life >= 3:
                DISPLAY.blit(HEART,(480-90-16*3,590))
            if life >= 4:
                DISPLAY.blit(HEART,(480-120-16*4,590))
            if life >= 5:
                DISPLAY.blit(HEART,(480-150-16*5,590))
            if life >= 6:
                DISPLAY.blit(HEART,(480-180-16*6,590))
            if life >= 7:
                DISPLAY.blit(HEART,(480-210-16*7,590))
            if life >= 8:
                DISPLAY.blit(HEART,(480-240-16*8,590))
            if life >= 9:
                DISPLAY.blit(HEART,(480-270-16*9,590))
            if life >= 10:
                DISPLAY.blit(HEART,(480-300-16*10,590))
            invinciblecounter += 1
            pygame.display.update()
            FPSCLOCK.tick(FPS-5)
        if gameover == True:
            DISPLAY.fill(GREY)
            leveltext = pygame.font.Font("freesansbold.ttf",32)
            levelsurface = leveltext.render("GAME OVER", True, WHITE, BLACK)
            levelrect = levelsurface.get_rect()
            levelrect.center = (240, 320)
            DISPLAY.blit(levelsurface, levelrect)
            pygame.display.update()
            sleep(3)
            pygame.quit()
            sys.exit()
            
def menudisplay():
    global button1surface
    global button2surface
    global button3surface
    global button4surface

    global button1rect
    global button2rect
    global button3rect
    global button4rect

    highlightbutton()
    
    pygame.draw.rect(DISPLAY, BLACK,(BUTTON1))
    pygame.draw.rect(DISPLAY, BLACK,(BUTTON2))
    pygame.draw.rect(DISPLAY, BLACK,(BUTTON3))
    pygame.draw.rect(DISPLAY, BLACK,(BUTTON4))

    buttontext = pygame.font.Font("freesansbold.ttf",32)
    
    button1surface = buttontext.render("Quit",True, WHITE, BLACK)
    button2surface = buttontext.render("Instructions",True, WHITE, BLACK)
    button3surface = buttontext.render("Options",True, WHITE, BLACK)
    button4surface = buttontext.render("Play",True, WHITE, BLACK)
    
    button1rect = button1surface.get_rect()
    button2rect = button2surface.get_rect()
    button3rect = button3surface.get_rect()
    button4rect = button4surface.get_rect()
    
    button1rect.center = (BUTTON1.centerx,BUTTON1.centery)
    button2rect.center = (BUTTON2.centerx,BUTTON2.centery)
    button3rect.center = (BUTTON3.centerx,BUTTON3.centery)
    button4rect.center = (BUTTON4.centerx,BUTTON4.centery)

    pygame.display.flip()

def highlightbutton():
    if highlight == "PLAY":
        pygame.draw.rect(DISPLAY,YELLOW,(BUTTONLEFT - 25, BUTTON4TOP - 25, BUTTONWIDTH + 50, BUTTONHEIGHT + 50))
    elif highlight == "OPTIONS":
        pygame.draw.rect(DISPLAY,YELLOW,(BUTTONLEFT - 25, BUTTON3TOP - 25, BUTTONWIDTH + 50, BUTTONHEIGHT + 50))
    elif highlight == "INSTRUCTIONS":
        pygame.draw.rect(DISPLAY,YELLOW,(BUTTONLEFT - 25, BUTTON2TOP - 25, BUTTONWIDTH + 50, BUTTONHEIGHT + 50))
    elif highlight == "QUIT":
        pygame.draw.rect(DISPLAY,YELLOW,(BUTTONLEFT - 25, BUTTON1TOP - 25, BUTTONWIDTH + 50, BUTTONHEIGHT + 50))
    displayonce = True
    pygame.display.flip()
    
def INSTRUCTIONS():
    DISPLAY.fill(BLUE)

    pygame.draw.rect(DISPLAY, YELLOW, (BACKBUTTONLEFT - 10, BACKBUTTONTOP -10, BACKBUTTONWIDTH + 20, BACKBUTTONHEIGHT + 20))
    
    instructionstext = pygame.font.Font("freesansbold.ttf",30)
    backbuttontext = pygame.font.Font("freesansbold.ttf",32)

    instructionssurface1 = instructionstext.render("Use the arrow keys to move.", True, WHITE, BLACK)
    instructionssurface2 = instructionstext.render("Press the space bar to fire.", True, WHITE, BLACK)
    instructionssurface3 = instructionstext.render("Your ship can take 10 hits", True, WHITE, BLACK)
    instructionssurface4 = instructionstext.render("before dying so watch out!", True, WHITE, BLACK)
    instructionssurface5 = instructionstext.render("Press 1 to enable god mode,", True, WHITE, BLACK)
    instructionssurface6 = instructionstext.render("Press 2 to disable god mode,",True, WHITE, BLACK)
    instructionssurface7 = instructionstext.render("Press 3 to enable rapid fire,", True, WHITE, BLACK)
    instructionssurface8 = instructionstext.render("Press 4 to disable rapid fire!", True, WHITE, BLACK)
    
    backbuttonsurface = backbuttontext.render("Back",True, WHITE, BLACK)

    instructionsrect1 = instructionssurface1.get_rect()
    instructionsrect2 = instructionssurface2.get_rect()
    instructionsrect3 = instructionssurface3.get_rect()
    instructionsrect4 = instructionssurface4.get_rect()
    instructionsrect5 = instructionssurface5.get_rect()
    instructionsrect6 = instructionssurface6.get_rect()
    instructionsrect7 = instructionssurface7.get_rect()
    instructionsrect8 = instructionssurface8.get_rect()
    
    backbuttonrect = backbuttonsurface.get_rect()

    instructionsrect1.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery-180)
    instructionsrect2.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery-135)
    instructionsrect3.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery-90)
    instructionsrect4.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery-45)
    instructionsrect5.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery)
    instructionsrect6.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery+45)
    instructionsrect7.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery+90)
    instructionsrect8.center = (INSTRUCTIONSBUTTON.centerx, INSTRUCTIONSBUTTON.centery+135)
    
    backbuttonrect.center = (BACKBUTTON.centerx, BACKBUTTON.centery)

    DISPLAY.blit(instructionssurface1, instructionsrect1)
    DISPLAY.blit(instructionssurface2, instructionsrect2)
    DISPLAY.blit(instructionssurface3, instructionsrect3)
    DISPLAY.blit(instructionssurface4, instructionsrect4)
    DISPLAY.blit(instructionssurface5, instructionsrect5)
    DISPLAY.blit(instructionssurface6, instructionsrect6)
    DISPLAY.blit(instructionssurface7, instructionsrect7)
    DISPLAY.blit(instructionssurface8, instructionsrect8)
    
    DISPLAY.blit(backbuttonsurface, backbuttonrect)

if __name__ == "__main__":
    main()

#!/usr/bin/python

from GIFImage import GIFImage
from PIL import Image
import pygame
import serial
import time
import datetime
import os

# SERIAL VARIABLES
state = 0    # CONNECT, CALIBRATE, ACTIVATE, ABORT
slaveState = 0
gameMode = 0
comPort = '/dev/ttyACM0'
comPort = 'COM39'
try:
	s = serial.Serial(comPort, 9600)
	information = ""
	# print ('try1')
except:
	s = serial.Serial()
	information = "NO DEVICE"
	# print ('except1')

# SET COLOR VARIABLES
red = (255,0,0)
green = (0,255,0)
blue = (160,200,250)
white = (255,255,255)
purple = (242, 217, 242)
color = purple

# PYGAME VARIABLES
pygame.init()
pygame.mouse.set_visible(False)

X, Y = 432, 768    # VERTICAL TV CONFIGURATION
# X, Y = 768, 1366    # VERTICAL TV CONFIGURATION
# X, Y = pygame.display.Info().current_w, pygame.display.Info().current_h
print (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode((X, Y))#, pygame.FULLSCREEN)
pygame.display.set_caption('TIMER')
fontSize = int(X//3.2)
# fontName = 'digital-7'
fontName = 'laser'
# josefin, laser, mazzard, neon, nidus sans, one day, ostrich sans, rajdhani, sulivan, swgdt, tw cent mt,  
font = pygame.font.SysFont(fontName, fontSize)

# BACKGROUND SCREEN
screen1 = pygame.Surface((X, Y))
screen1.set_alpha(225)
# hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/hud1-1120x702.gif")
hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/network2-432x768.gif")
# hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/network2-768x1366.gif")
# WINNER STICKER
winner = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/winner.png")
winner = pygame.transform.rotozoom(winner, 0, 0.5)

# TIMER VARIABLES
totalTime = 540 #in seconds
startTime = datetime.datetime.now()
pauseTime = datetime.datetime.now()
totalPause = 0
laserPenalty = 10
laserWallPenalty = 30
laserCuts = 0
laserWallCuts = 0
totalLasers = 90
pause = False

def displayPanel():
    hud1.render(screen1, (0, 0))
    # if (hud1.reversed == False and hud1.cur == hud1.breakpoint) or (hud1.reversed == True and hud1.cur == hud1.startpoint) :
        # hud1.reverse()
    screen.blit(screen1, (0,0))

def displayTime(minutes, seconds):
    timerFont = pygame.font.SysFont(fontName, int(X//4))
    if (gameMode == 0):
        text = timerFont.render(":", True, color)
        textRect = text.get_rect()
        textRect.center = (X//2, 5*Y//16)
        screen.blit(text, textRect)
        
        value = str(minutes//10)
        text = timerFont.render(value, True, color)
        textRect = text.get_rect()
        textRect.center = (X//2 - fontSize//1, 5*Y//16)
        screen.blit(text, textRect)
        value = str(minutes - 10*(minutes//10))
        text = timerFont.render(value, True, color)
        textRect = text.get_rect()
        textRect.center = (X//2 - fontSize//2.5, 5*Y//16)
        screen.blit(text, textRect)

        value = str(seconds - 10*(seconds//10))
        text = timerFont.render(value, True, color)
        textRect = text.get_rect()
        textRect.center = (X//2 + fontSize//1, 5*Y//16)
        screen.blit(text, textRect)
        value = str(seconds//10)
        text = timerFont.render(value, True, color)
        textRect = text.get_rect()
        textRect.center = (X//2 + fontSize//2.5, 5*Y//16)
        screen.blit(text, textRect)
    elif (gameMode == 1 or gameMode == 2):
        # font1 = pygame.font.SysFont(fontName, 300)
        font1 = pygame.font.SysFont('komika axis', 225)
        text = font1.render(":", True, color)
        textRect = text.get_rect()
        textRect.center = (X//2, Y//5)
        screen.blit(text, textRect)
        
        value = str(minutes//10)
        text = font1.render(value, True, color)
        textRect = text.get_rect()
        # textRect.center = (X//2 - fontSize//1.7, Y//5)
        textRect.center = (X//2 - fontSize//1.5, Y//5)
        screen.blit(text, textRect)
        value = str(minutes - 10*(minutes//10))
        text = font1.render(value, True, color)
        textRect = text.get_rect()
        # textRect.center = (X//2 - fontSize//4, Y//5)
        textRect.center = (X//2 - fontSize//3.5, Y//5)
        screen.blit(text, textRect)

        value = str(seconds - 10*(seconds//10))
        text = font1.render(value, True, color)
        textRect = text.get_rect()
        # textRect.center = (X//2 + fontSize//1.7, Y//5)
        textRect.center = (X//2 + fontSize//1.5, Y//5)
        screen.blit(text, textRect)
        value = str(seconds//10)
        text = font1.render(value, True, color)
        textRect = text.get_rect()
        # textRect.center = (X//2 + fontSize//4, Y//5)
        textRect.center = (X//2 + fontSize//3.5, Y//5)
        screen.blit(text, textRect)

def displayInfo(information):
    if (state == 2 and slaveState == 0):
        if (gameMode == 0):
            text = pygame.font.SysFont(fontName, int(X//16)).render(" WELCOME TO ", True, color)
            textRect = text.get_rect()
            x, y = X//2, Y//16
            textRect.center = (x, y)
            x, y = x, y + textRect.height/2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            srf = pygame.Surface((X, 3*textRect.height))
            srf.set_alpha(200)
            screen.blit(srf, (0, textRect.y))
            screen.blit(text, textRect)
            text = pygame.font.SysFont(fontName, int(X//8)).render("LASER WARS", True, color)
            textRect = text.get_rect()
            x, y = x, y + textRect.height/2
            textRect.center = (x, y)
            x, y = x, y + textRect.height/2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            screen.blit(text, textRect)

            text = pygame.font.SysFont(fontName, int(X//16)).render("PRESS START TO", True, color)
            textRect = text.get_rect()
            x, y = X//2, Y//2
            textRect.center = (x, y)
            x, y = x, y + textRect.height/2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            srf = pygame.Surface((X, 2.1*textRect.height))
            srf.set_alpha(200)
            screen.blit(srf, (0, textRect.y))
            screen.blit(text, textRect)
            text = pygame.font.SysFont(fontName, int(X//16)).render("STEAL THE DIAMOND", True, color)
            textRect = text.get_rect()
            x, y = x, y + textRect.height/2
            textRect.center = (x, y)
            x, y = x, y + textRect.height/2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            screen.blit(text, textRect)
        elif (gameMode == 1 or gameMode == 2):
            # font1 = pygame.font.SysFont(fontName, fontSize//4)
            font1 = pygame.font.SysFont('komika axis', fontSize//5)
            information = " PRESS START BUTTON"
            x = X//2
            # y = Y//1.5
            y = Y//1.8
            text = font1.render(information, True, (255,215,0))
            textRect = text.get_rect()
            textRect.center = (x, y)
            screen.blit(text, textRect)
            # font1 = pygame.font.SysFont(fontName, fontSize//4)
            font1 = pygame.font.SysFont('komika axis', fontSize//5)
            information = " TO START THE GAME"
            # y = Y//1.2
            y = Y//1.4
            text = font1.render(information, True, (255,215,0))
            textRect = text.get_rect()
            textRect.center = (x, y)
            screen.blit(text, textRect)
    elif ((state == 2 and slaveState == 1) or (state == 3 and gameMode != 0)):
        if (gameMode == 1):
            # font1 = pygame.font.SysFont(fontName, 350)
            font1 = pygame.font.SysFont('komika axis', 200)
            font2 = pygame.font.SysFont('komika axis', 70)
            information = str(laserCuts)
            text1 = font1.render(information, True, (255,215,0))
            text2 = font2.render("out", True, (255,215,0))
            text3 = font2.render("of", True, (255,215,0))
            text4 = font1.render(str(totalLasers), True, (255,215,0))
            textRect1 = (text1).get_rect()
            textRect2 = (text2).get_rect()
            textRect3 = (text3).get_rect()
            textRect4 = (text4).get_rect()
            textRect1.center = (X//5, Y//1.4)
            textRect2.center = (X//2, Y//1.5)
            textRect3.center = (X//2, Y//1.3)
            textRect4.center = (X//1.25, Y//1.4)
            screen.blit(text1, textRect1)
            screen.blit(text2, textRect2)
            screen.blit(text3, textRect3)
            screen.blit(text4, textRect4)
        elif (gameMode == 2):
            font1 = pygame.font.SysFont('komika axis', 100)
            font2 = pygame.font.SysFont(fontName, 170)
            font3 = pygame.font.SysFont('komika axis', 250)
            information = str(laserCuts)
            textA1 = font1.render("TEAM A", True, (255,215,0))
            textA2 = font2.render("A", True, (255,215,0))
            textA3 = font3.render(information, True, (255,215,0))
            textRectA1 = (textA1).get_rect()
            textRectA2 = (textA2).get_rect()
            textRectA3 = (textA3).get_rect()
            # textRectA1.center = (X//11, Y//1.75)
            # textRectA2.center = (X//11, Y//1.35)
            # textRectA3.center = (X//3, Y//1.5)
            textRectA1.center = (X//4, Y//2)
            textRectA2.center = (X//4, Y//1.75)
            textRectA3.center = (X//4, Y//1.35)
            screen.blit(textA1, textRectA1)
            # screen.blit(textA2, textRectA2)
            screen.blit(textA3, textRectA3)
            information = str(laserWallCuts)
            textB1 = font1.render("TEAM B", True, green)
            textB2 = font2.render("B", True, green)
            textB3 = font3.render(information, True, green)
            textRectB1 = (textB1).get_rect()
            textRectB2 = (textB2).get_rect()
            textRectB3 = (textB3).get_rect()
            # textRectB1.center = (X//1.1, Y//1.75)
            # textRectB2.center = (X//1.1, Y//1.35)
            # textRectB3.center = (X//1.5, Y//1.5)
            textRectB1.center = (X//1.33, Y//2)
            textRectB2.center = (X//1.33, Y//1.35)
            textRectB3.center = (X//1.33, Y//1.35)
            screen.blit(textB1, textRectB1)
            # screen.blit(textB2, textRectB2)
            screen.blit(textB3, textRectB3)
            if (state == 3):
                if (laserCuts > laserWallCuts):
                    # screen.blit(winner, (X//9, Y//1.5))
                    screen.blit(winner, (X//7, Y//1.5))
                elif (laserCuts < laserWallCuts):
                    # screen.blit(winner, (X//1.7, Y//1.5))
                    screen.blit(winner, (X//1.5, Y//1.5))
    elif (state == 3 and gameMode == 0):
        text = pygame.font.SysFont(fontName, int(X//9.6)).render("GAME OVER", True, color)
        textRect = text.get_rect()
        x, y = X//2, Y//2
        textRect.center = (x, y)
        srf = pygame.Surface((X, 1.1*textRect.height))
        srf.set_alpha(200)
        screen.blit(srf, (0, textRect.y))
        screen.blit(text, textRect)
    else:
        text = pygame.font.SysFont(fontName, int(X//7.5)).render(information, True, color)
        textRect = text.get_rect()
        x, y = X//2, 5*Y//16
        textRect.center = (x, y)
        if information != "":
            srf = pygame.Surface((X, 1.1*textRect.height))
            srf.set_alpha(200)
            screen.blit(srf, (0, textRect.y))
        screen.blit(text, textRect)

def processComm():
    global state, slaveState, gameMode, pause
    global totalTime, timer, startTime, pauseTime
    global information, laserCuts, laserWallCuts, totalLasers, totalPause

    inChar = s.readline().decode("utf-8")
    # inChar = s.read(1).decode("utf-8")  # FOR PYTHON3
    inChar = inChar.strip('\n')
    print (inChar)
    if (inChar == 'a'):
        state = 0
        slaveState = 0
        print (state)
        information = "CONNECTING"
    elif (inChar == 'b'):
        state = 1
        slaveState = 0
        totalTime = 0
        totalLasers = 0
        information = "CALIBRATING"
    elif (inChar == 'l'):
        state = 1
        slaveState = 0
        while (s.in_waiting <= 0):
            pass
        players = ord(s.read(1)) - 33
        # print players
        if (players <= 2):
            totalTime = 540
        elif (players <= 4):
            totalTime = 720
        elif (players <= 6):
            totalTime = 900
        else:
            totalTime = 540
        information = "CALIBRATING"
    elif (inChar == '}'):
        state = 1
        slaveState = 0
        while (s.in_waiting <= 0):
            pass
        mins = ord(s.read(1)) - 33
        totalTime = mins*60
    elif (inChar == '~'):
        state = 1
        slaveState = 0
        while (s.in_waiting <= 0):
            pass
        secs = ord(s.read(1)) - 33
        totalTime = totalTime + secs
    elif (inChar == 'c'):
        state = 2
        slaveState = 0
        gameMode = 0
        information = "PRESS START BUTTON TO START THE GAME"
    elif (state == 2 and inChar == 's'):
        gameMode = 0
        laserWallCuts = 0
        laserCuts = 0
    elif (state == 2 and inChar == '|'):
        gameMode = 1
        laserWallCuts = 0
        laserCuts = 0
    elif (state == 2 and inChar == '_'):
        gameMode = 2
        laserWallCuts = 0
        laserCuts = 0
    elif (state == 2 and inChar == 'r'):
        slaveState = 1
        laserWallCuts = 0
        laserCuts = 0
        totalPause = 0
        pause = 0
        startTime = datetime.datetime.now()
        pauseTime = startTime
        information = ""
    elif (inChar == 'y'):
        while (s.in_waiting <= 0):
            pass
        totalLasers = totalLasers + (ord(s.read(1)) - 33)*10
    elif (state == 2 and inChar == 'z'):
        if (pause == 1):
            totalPause = totalPause + (currentTime - pauseTime).seconds
        else:
            pauseTime = datetime.datetime.now()
        pause = not(pause)
    elif (state == 2 and slaveState == 1 and inChar == 'w'):
        laserCuts = laserCuts  + 1
    elif (state == 2 and slaveState == 1 and inChar == 'x'):
        laserWallCuts = laserWallCuts + 1
    elif (inChar == 'd'):
        state = 3
        slaveState = 2
    elif (state == 2 and slaveState == 1 and inChar == 'START_CROSSWORD'):
        startCrossword();

def startCrossword():
    pass

while True:
    #global state, slaveState
    #global totalTime, timer, startTime
    #global information, laserCuts, laserWallCuts

    screen.fill(0)
    displayPanel()

    try:
	    if (s.in_waiting > 0):
	        processComm()

	    if (slaveState == 1):
	        currentTime = datetime.datetime.now()
	        if (gameMode == 0):
	            timer = totalTime - (currentTime - startTime).seconds - laserPenalty*laserCuts - laserWallPenalty*laserWallCuts
	        elif ((gameMode == 1 or gameMode == 2) and pause == 0):
	            timer = totalTime - (currentTime - startTime).seconds + totalPause
	    elif (slaveState != 2):
	        timer = totalTime

	    if timer > 0: 
	        minutes = timer//60
	        seconds = timer%60
	    else:
	        minutes = 0
	        seconds = 0
	        if (state == 2 and gameMode == 0):
	            information = "GAME OVER"
	        if (state == 2):
	            state = 3

	    if (state == 2 or state == 3):
	        displayTime(minutes, seconds)
	    displayInfo(information)
    except:
    	displayInfo(information)
    	try:
    		s = serial.Serial(comPort, 9600)
    		information = ""
    	except:
            information = "NO DEVICE"
            s = serial.Serial()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
            
    pygame.display.update()
    #time.sleep(0.5)

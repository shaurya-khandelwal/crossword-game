
#!/usr/bin/python

from outlineText import outlineText
from GIFImage import GIFImage
from PIL import Image
import pygame
import serial
import time
import datetime
import os
import threading
import random


#------------------Word Bags-------------------
word_bag1 = {20 : "money", 21 : "past", 22 : "end", 23 : "late", 24 :"present", 25 : "future", 26 : "new", 27 : "gate", 28 : "window", 29 : "board"}
word_bag2 = {31 : "allow", 32 : "stop", 33 : "traffic", 21 : "gamma", 35 : "alpha", 36 : "beta", 37 : "delta", 38 : "drama", 39 : "data", 40 : "laptop"}
word_bag3 = {51 : "mon", 20 : "pat", 52 : "en", 53 : "lte", 54 :"pesent", 55 : "fuure", 21 : "ndew", 56 : "gadte", 57 : "winddow", 60 : "boadrd"}
word_bag4 = {80 : "all", 79 : "stopdc", 78 : "traff", 76 : "gama", 75 : "alph", 74 : "bea", 73 : "dela", 72 : "drma", 71 : "dat", 20 : "aptop"}
num_keys = [pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5 , pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
txtinp_disp = [""] * 6
lock = [False] * 6
global_result = [4] * 6
count1 = 500
# PYGAME VARIABLES
ptr = 0
pygame.init()
pygame.mouse.set_visible(False)
width, height = 432, 768



def combined_bag(bags):
    arr = []
    for bag in bags:
        for key in bag.keys():
            arr += [(key, bag[key])]
    new_bag = {}
    #print(arr)
    for val in arr:
        try:
            new_bag[val[0]] += [val[1]]
        except:
            new_bag[val[0]] = [val[1]]
    return new_bag


#------------------------------------------

def check_strings(param, words, window, ptr):
    result = ""
    master_bag = combined_bag([word_bag1, word_bag2, word_bag3, word_bag4])
    if len(param[ptr].strip()) >= 1:
        val = int(param[ptr].strip())
        try:
            if words[ptr] in master_bag[val]:
                result = True
            else:
                result = False
        except:
            result = False
    else:
        result = 4
    # print(result)
    default_pos = height // 2.21
    pos = default_pos
    offset = height // 10.55
    pos = pos + ptr * offset
    font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + 'digital-7.ttf', X//13)
    blank = font.render("     ", True, (255, 255, 255), None)
    right = pygame.image.load(r'./media/right.png')
    wrong = pygame.image.load(r'./media/wrong.png')
    print(param[ptr], result)
    if result == 4:
        lock[ptr] = False
        blank_rect = right.get_rect()
        blank_rect.center = ((3.4 * width // 4), pos)
        #pygame.draw.rect(screen, (255, 255, 255), txtinp_rect, 1)
        window.blit(blank, blank_rect)
    elif result:
        global_result[ptr] = result
        white = (255, 255, 255)
        red = (0, 255, 0)
        colour = [white, green]
        count = 0
        for j in range(8):
            count = 0
            while True:
                if len(param[ptr].strip()) == 1:
                    tex = font.render(param[ptr].strip() + "-", True, colour[j % 2], None)
                else:
                    tex = font.render(param[ptr], True, colour[j % 2], None)
                tex_rect = tex.get_rect()
                tex_rect.center = (3 * width // 4, pos)
                window.blit(tex, tex_rect)
                # pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
                pygame.display.flip()
                count += 1
                if count > j * 50:
                    break
        if len(param[ptr].strip()) == 1:
            tex = font.render(param[ptr].strip() + "-", True, (0, 255, 0), None)
        else:
            tex = font.render(param[ptr], True, (0, 255, 0), None)
        tex_rect = tex.get_rect()
        tex_rect.center = (3 * width // 4, pos)
        right_rect = right.get_rect()
        right_rect.center = (3.6 * width // 4, pos)
        #pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
        window.blit(tex, tex_rect)
        window.blit(right, right_rect)
        lock[ptr] = True
    else:
        global_result[ptr] = result
        white = (255, 255, 255)
        red = (255, 0, 0)
        colour = [white, red]
        count = 0
        for j in range(8):
            count = 0
            while True:
                if len(param[ptr].strip()) == 1:
                    tex = font.render(param[ptr].strip()+"-", True, colour[j % 2], None)
                else:
                    tex = font.render(param[ptr], True, colour[j % 2], None)
                tex_rect = tex.get_rect()
                tex_rect.center = (3 * width // 4, pos)
                window.blit(tex, tex_rect)
                #pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
                pygame.display.flip()
                count += 1
                if count > j*50:
                    break
                # count = 0
                # while True:
                #     tex = font.render(param[i], True, colour[0], None)
                #     tex_rect = tex.get_rect()
                #     tex_rect.center = (3 * width // 4, pos)
                #     window.blit(tex, tex_rect)
                #     pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
                #     pygame.display.flip()
                #     count += 1
                #     if count > 1000:
                #         break
                # count = 0
                # while True:
                #     tex = font.render(param[i], True, colour[1], None)
                #     tex_rect = tex.get_rect()
                #     tex_rect.center = (3 * width // 4, pos)
                #     window.blit(tex, tex_rect)
                #     pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
                #     pygame.display.flip()
                #     count += 1
                #     if count > 1000:
                #         break
        if len(param[ptr].strip()) == 1:
            tex = font.render(param[ptr].strip() + "-", True, (255, 0, 0), None)
        else:
            tex = font.render(param[ptr], True, (255, 0, 0), None)
        tex_rect = tex.get_rect()
        tex_rect.center = (3 * width // 4, pos)
        wrong_rect = wrong.get_rect()
        wrong_rect.center = (3.6 * width // 4, pos)
        # pygame.draw.rect(screen, (255, 255, 255), tex_rect, 1)
        window.blit(tex, tex_rect)
        window.blit(wrong, wrong_rect)
        lock[ptr] = False
     #for all check
    #for i in range(6):
     #   if not global_result[i]:
      #      return
    #pass#function call


# -----------------Random String----------------
enter = "ENTER !!"


def get_strings():
    lis = [word_bag1, word_bag2, word_bag3, word_bag4]
    bags = random.sample(list(lis), 2)
    print(lis[0])
    random_keys = random.sample(list(word_bag1.values()), 1) + random.sample(list(word_bag2.values()),1) + random.sample(list(word_bag3.values()), 1) + random.sample(list(word_bag4.values()), 1) + random.sample(list(lis[1].values()),1) + random.sample(list(lis[2].values()), 1)
    return random_keys


# ------------------Button---------------
def text_objects(text, font, black):
    if black:
        textSurface = font.render(text, True, None)
    else:
        textSurface = font.render(text, True, None)
    return textSurface, textSurface.get_rect()


def clear_screen(window):
    txtinp_disp = ["     "] * 6
    ptr = 0
    default_pos = height // 4
    pos = default_pos
    offset = height // 16
    image = pygame.image.load(r'./media/blank.png')
    for i in range(6):
        image_rect = image.get_rect()
        image_rect.center = ((4.5 * width // 8), pos)
        window.blit(image, image_rect)
        pos += offset

#------------------------------------------

# SERIAL VARIABLES
state = 0  # CONNECT, CALIBRATE, ACTIVATE, ABORT
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
red = (255, 0, 0)
green = (0, 255, 0)
blue = (160, 200, 250)
white = (255, 255, 255)
purple = (242, 217, 242)
color = purple


X, Y = 432, 768    # VERTICAL TV CONFIGURATION
# X, Y = 768, 1366    # VERTICAL TV CONFIGURATION
#X, Y = pygame.display.Info().current_w, pygame.display.Info().current_h
#print(pygame.display.Info().current_w, pygame.display.Info().current_h)


screen: None = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
pygame.display.set_caption('TIMER')
fontSize = int(X // 3.2)
# fontName = 'digital-7'
# font = pygame.font.SysFont(fontName, fontSize)
# josefin, laser, mazzard, neon, nidus sans, one day, ostrich sans, rajdhani, sulivan, swgdt, tw cent mt,
fontName = 'LASER REGULAR.ttf'
font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName, fontSize)

# BACKGROUND SCREEN
# hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/hud1-1120x702.gif")
hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/network2-432x768.gif")
# hud1 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/network2-768x1366.gif")
hud2 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/blueneon-432x768.gif")
# hud2 = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/blueneon-768x1366.gif")
# handaccess = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/handaccess1-432x507.gif")
handaccess = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/handaccess1.gif")
fingerscan = [GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/fingerscan-136x150.gif")] * 5
scanningtext = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/scanningtext-672x275.gif")
# scanningtext = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/scanningtext-613x720.gif")
diamond = GIFImage(os.path.dirname(os.path.abspath(__file__)) + "/" + "images/diamond.gif")

# TIMER VARIABLES
totalTime = 540  # in seconds
startTime = datetime.datetime.now()
pauseTime = datetime.datetime.now()
totalPause = 0
laserPenalty = 10
laserWallPenalty = 30
laserCuts = 0
laserWallCuts = 0
totalLasers = 90
pause = False


def get_sub_surface(screen, rect):
    sub = screen.subsurface(rect)
    pygame.image.save(sub, "screenshot.jpg")


def displayPanel():
    screen1 = pygame.Surface((X, Y))
    screen1.set_alpha(255)
    hud2.render(screen1, (0, 0))
    if (hud2.reversed == False and hud2.cur == hud2.breakpoint) or (
            hud2.reversed == True and hud2.cur == hud2.startpoint):
        hud2.reverse()
    screen.blit(screen1, (0, 0))
    black = pygame.Surface((X, 2 * Y // 17))
    black.fill((255, 255, 255))
    black.set_alpha(5)
    screen.blit(black, (0, Y // 15))


def displayScanning():
    global slaveState
    screen1 = pygame.Surface((613, 720))
    handaccess.render(screen1, (0, 0))
    if (handaccess.reversed == False and handaccess.cur == int(handaccess.breakpoint * 18 / 25)) or (
            handaccess.reversed == True and handaccess.cur == handaccess.startpoint):
        handaccess.reverse()
    screen.blit(screen1, ((X - 613) / 2, 320))
    # for x in range(0,5):
    # 	screen1 = pygame.Surface((136, 150))
    # 	fingerscan[x].render(screen1, (0, 0))
    # 	if (fingerscan[x].reversed == False and fingerscan[x].cur == fingerscan[x].breakpoint) or (fingerscan[x].reversed == True and fingerscan[x].cur == fingerscan[x].startpoint) :
    # 		fingerscan[x].reverse()
    # 	screen.blit(screen1, (44 + 136*x, 820))
    screen1 = pygame.Surface((672, 275))
    scanningtext.render(screen1, (0, 0))
    if (scanningtext.reversed == False and scanningtext.cur == int(scanningtext.breakpoint * 18 / 25)) or (
            scanningtext.reversed == True and scanningtext.cur == scanningtext.startpoint):
        scanningtext.reverse()
    screen.blit(screen1, ((X - 672) / 2, 1050))


def displayScanning1():
    global slaveState
    screen1 = pygame.Surface((613, 720))
    handaccess.render(screen1, (0, 0))
    if (handaccess.reversed == False and handaccess.cur == handaccess.breakpoint) or (
            handaccess.reversed == True and handaccess.cur == handaccess.startpoint):
        slaveState = 1
        return 0
        handaccess.reverse()
    screen.blit(screen1, ((X - 613) / 2, 100))
    for x in range(0, 5):
        screen1 = pygame.Surface((136, 150))
        fingerscan[x].render(screen1, (0, 0))
        if (fingerscan[x].reversed == False and fingerscan[x].cur == fingerscan[x].breakpoint) or (
                fingerscan[x].reversed == True and fingerscan[x].cur == fingerscan[x].startpoint):
            fingerscan[x].reverse()
        screen.blit(screen1, (44 + 136 * x, 820))
    screen1 = pygame.Surface((672, 275))
    scanningtext.render(screen1, (0, 0))
    if (scanningtext.reversed == False and scanningtext.cur == scanningtext.breakpoint) or (
            scanningtext.reversed == True and scanningtext.cur == scanningtext.startpoint):
        pass  # scanningtext.reverse()
    screen.blit(screen1, ((X - 672) / 2, 1000))


def displayTransition():
    global slaveState
    screen1 = pygame.Surface((X, Y))
    diamond.render(screen1, (0, 0))
    if (diamond.reversed == False and diamond.cur == diamond.breakpoint) or (
            diamond.reversed == True and diamond.cur == diamond.startpoint):
        diamond.reverse()
    # slaveState = 2
    # return 0
    screen.blit(screen1, ((X - 500) / 2, (Y - 500) / 2))


def displayTime(minutes, seconds, timerX, timerY, timerF, timerFsize, timerFColor, timerBColor=(255, 255, 255)):
    timerFont = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + timerF, timerFsize)
    if (gameMode == 0):
        text = timerFont.render(":", True, timerFColor)
        textRect = text.get_rect()
        textRect.center = (timerX, timerY)
        screen.blit(outlineText.render(":", timerFont, timerFColor, timerBColor), textRect)

        value = str(minutes // 10)
        text = timerFont.render(value, True, timerFColor)
        textRect = text.get_rect()
        textRect.center = (timerX - timerFsize // 0.8, timerY)
        screen.blit(outlineText.render(value, timerFont, timerFColor, timerBColor), textRect)
        value = str(minutes - 10 * (minutes // 10))
        text = timerFont.render(value, True, timerFColor)
        textRect = text.get_rect()
        textRect.center = (timerX - timerFsize // 2, timerY)
        screen.blit(outlineText.render(value, timerFont, timerFColor, timerBColor), textRect)

        value = str(seconds - 10 * (seconds // 10))
        text = timerFont.render(value, True, timerFColor)
        textRect = text.get_rect()
        textRect.center = (timerX + timerFsize // 0.8, timerY)
        screen.blit(outlineText.render(value, timerFont, timerFColor, timerBColor), textRect)
        value = str(seconds // 10)
        text = timerFont.render(value, True, timerFColor)
        textRect = text.get_rect()
        textRect.center = (timerX + timerFsize // 2, timerY)
        screen.blit(outlineText.render(value, timerFont, timerFColor, timerBColor), textRect)


def displayInfo(information):
    if (state == 2 and slaveState == 0):
        if (gameMode == 0):
            text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                    int(X // 16)).render(" WELCOME TO ", True, color)
            textRect = text.get_rect()
            x, y = timerX, Y // 16
            textRect.center = (x, y)
            x, y = x, y + textRect.height / 2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            srf = pygame.Surface((X, 3 * textRect.height))
            srf.set_alpha(200)
            screen.blit(srf, (0, textRect.y))
            screen.blit(text, textRect)
            text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                    int(X // 8)).render("LASER WARS", True, color)
            textRect = text.get_rect()
            x, y = x, y + textRect.height / 2
            textRect.center = (x, y)
            x, y = x, y + textRect.height / 2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            screen.blit(text, textRect)

            text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                    int(X // 16)).render("PRESS START TO", True, color)
            textRect = text.get_rect()
            x, y = timerX, Y // 2
            textRect.center = (x, y)
            x, y = x, y + textRect.height / 2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            srf = pygame.Surface((X, 2.1 * textRect.height))
            srf.set_alpha(200)
            screen.blit(srf, (0, textRect.y))
            screen.blit(text, textRect)
            text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                    int(X // 16)).render("STEAL THE DIAMOND", True, color)
            textRect = text.get_rect()
            x, y = x, y + textRect.height / 2
            textRect.center = (x, y)
            x, y = x, y + textRect.height / 2
            # srf = pygame.Surface(textRect.size)
            # srf.set_alpha(200)
            # screen.blit(srf, textRect)
            screen.blit(text, textRect)
        # elif (gameMode == 1 or gameMode == 2):
        #     # font1 = pygame.font.SysFont(fontName, fontSize//4)
        #     font1 = pygame.font.SysFont('komika axis', fontSize//5)
        #     information = " PRESS START BUTTON"
        #     x = timerX
        #     # y = Y//1
        #     y = Y//1.8
        #     text = font1.render(information, True, (255,215,0))
        #     textRect = text.get_rect()
        #     textRect.center = (x, y)
        #     screen.blit(text, textRect)
        #     # font1 = pygame.font.SysFont(fontName, fontSize//4)
        #     font1 = pygame.font.SysFont('komika axis', fontSize//5)
        #     information = " TO START THE GAME"
        #     # y = Y//1.2
        #     y = Y//1.4
        #     text = font1.render(information, True, (255,215,0))
        #     textRect = text.get_rect()
        #     textRect.center = (x, y)
        #     screen.blit(text, textRect)
    elif ((state == 2 and slaveState == 1) or (state == 3 and gameMode != 0)):
        if (gameMode == 1):
            # font1 = pygame.font.SysFont(fontName, 350)
            font1 = pygame.font.SysFont('komika axis', 200)
            font2 = pygame.font.SysFont('komika axis', 70)
            information = str(laserCuts)
            text1 = font1.render(information, True, (255, 215, 0))
            text2 = font2.render("out", True, (255, 215, 0))
            text3 = font2.render("of", True, (255, 215, 0))
            text4 = font1.render(str(totalLasers), True, (255, 215, 0))
            textRect1 = (text1).get_rect()
            textRect2 = (text2).get_rect()
            textRect3 = (text3).get_rect()
            textRect4 = (text4).get_rect()
            textRect1.center = (X // 5, Y // 1.4)
            textRect2.center = (timerX, Y // 1)
            textRect3.center = (timerX, Y // 1.3)
            textRect4.center = (X // 1.25, Y // 1.4)
            screen.blit(text1, textRect1)
            screen.blit(text2, textRect2)
            screen.blit(text3, textRect3)
            screen.blit(text4, textRect4)
        elif (gameMode == 2):
            font1 = pygame.font.SysFont('komika axis', 100)
            font2 = pygame.font.SysFont(fontName, 170)
            font3 = pygame.font.SysFont('komika axis', 250)
            information = str(laserCuts)
            textA1 = font1.render("TEAM A", True, (255, 215, 0))
            textA2 = font2.render("A", True, (255, 215, 0))
            textA3 = font3.render(information, True, (255, 215, 0))
            textRectA1 = (textA1).get_rect()
            textRectA2 = (textA2).get_rect()
            textRectA3 = (textA3).get_rect()
            # textRectA1.center = (X//11, Y//1.75)
            # textRectA2.center = (X//11, Y//1.35)
            # textRectA3.center = (X//3, Y//1)
            textRectA1.center = (X // 4, Y // 2)
            textRectA2.center = (X // 4, Y // 1.75)
            textRectA3.center = (X // 4, Y // 1.35)
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
            # textRectB3.center = (X//1, Y//1)
            textRectB1.center = (X // 1.33, Y // 2)
            textRectB2.center = (X // 1.33, Y // 1.35)
            textRectB3.center = (X // 1.33, Y // 1.35)
            screen.blit(textB1, textRectB1)
            # screen.blit(textB2, textRectB2)
            screen.blit(textB3, textRectB3)
            if (state == 3):
                if (laserCuts > laserWallCuts):
                    # screen.blit(winner, (X//9, Y//1))
                    screen.blit(winner, (X // 7, Y // 1))
                elif (laserCuts < laserWallCuts):
                    # screen.blit(winner, (X//1.7, Y//1))
                    screen.blit(winner, (X // 1, Y // 1))
    elif (state == 3 and gameMode == 0):
        text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                int(X // 9.6)).render("GAME OVER", True, color)
        textRect = text.get_rect()
        x, y = timerX, Y // 2
        textRect.center = (x, y)
        srf = pygame.Surface((X, 1.1 * textRect.height))
        srf.set_alpha(200)
        screen.blit(srf, (0, textRect.y))
        screen.blit(text, textRect)
    else:
        text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName,
                                int(X // 7.5)).render(information, True, color)
        textRect = text.get_rect()
        x, y = timerX, timerY
        textRect.center = (x, y)
        if information != "":
            srf = pygame.Surface((X, 1.1 * textRect.height))
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
    print(inChar)
    if (inChar == 'ENTER'):
        pass


def timerEnd():
    global secTimer, slaveState
    secTimer.cancel()
    slaveState = 2


# TIMER OBJECT
secTimer = threading.Timer(5.0, timerEnd)
words = get_strings()

while True:
    # global state, slaveState
    # global totalTime, timer, startTime
    # global information, laserCuts, laserWallCuts
    # global secTimer
    slaveState = 2
    screen.fill(0)
    if (slaveState == 0):
        displayScanning()
        displayTime(9, 32, X // 2, Y // 9, 'LASER REGULAR.ttf', int(X // 4), (153, 255, 153))
    elif (slaveState == 1):
        # print (threading.active_count())
        try:
            secTimer.start()
        except:
            pass
        displayTransition()
    elif (slaveState == 2):
        displayPanel()
        displayTime(9, 32, X // 2, Y // 9, 'LASER REGULAR.ttf', int(X // 4), (206, 230, 246), (68, 165, 221))

    try:
        if (s.in_waiting > 0):
            processComm()

    except:
        try:
            s = serial.Serial(comPort, 9600)
        except:
            information = "NO DEVICE"
            s = serial.Serial()
    font0 = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName, X // 15)
    heading1 = font0.render("DECRYPT WORD TO",True,(255,255,255),None)
    heading_rect=heading1.get_rect()
    heading_rect.center =(width // 2.0, Y // 3.8)
    screen.blit(heading1, heading_rect)
    unway = Y // 3.8+ Y//10.8
    heading2 = font0.render("UNLOCK DIAMOND ", True, (255, 255, 255), None)
    heading2_rect = heading2.get_rect()
    heading2_rect.center = (width // 2.0, unway)
    screen.blit(heading2, heading2_rect)
    default_pos = height //2.42
    default_pos0=height // 2.44
    offset = height // 10.8
    offset0=height // 11.2
    ques = default_pos0+ptr*offset
    #tem = offset
    black = (0,0,0)
    black_surface = pygame.Surface((X, offset0))
    black_surface.set_alpha(150)
    black_surface.fill(black)
    screen.blit(black_surface, (0, ques))
    #pygame.draw.rect(screen, bla ,(0, ques, X, tem ))
    font0 = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName, X//20)
    default_pos = height // 2.21
    pos = default_pos
    offset = height // 10.55
    for word in words:
        word_disp = font0.render(str(word), True, (255, 255, 255), None)
        words_rect = word_disp.get_rect()
        words_rect.center = (width // 2.5, pos)
        words_rect.topleft = (width // 5, words_rect.topleft[1])
        #box_rect.center = (width // 4.2, pos)
        screen.blit(word_disp, words_rect)
        pos += offset

    # ----------------------Input------------------------
    pos = default_pos
    font1 = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + fontName, X//13)
    for i in range(6):
        dash = font1.render("    ", True, (153, 255, 153), None)
        dash_rect = dash.get_rect()
        dash_rect.center = (3 * width // 4, pos)
        # pygame.Rect(3 * width // 4, pos, X // 10, Y // 15)
        pygame.draw.rect(screen, (206, 230, 246), dash_rect, 3)
        screen.blit(dash, dash_rect)
        pos += offset
    # ----------------------Input--
    pos = default_pos
    font1 = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/" + "fonts/" + 'digital-7.ttf', X//13)
    right = pygame.image.load(r'./media/right.png')
    wrong = pygame.image.load(r'./media/wrong.png')
    for i in range(6):
        if len(txtinp_disp[i].strip()) > 1:
            if global_result[i] == 4:
                txtinp = font1.render(txtinp_disp[i], True, (255, 255, 255), None)
            elif i == ptr and not global_result[ptr]:
                txtinp_disp[i] = ""
                global_result[i] = 4
                txtinp = font1.render(txtinp_disp[i], True, (255, 255, 255), None)
            elif global_result[i]:
                right_rect = right.get_rect()
                right_rect.center = (3.6 * width // 4, default_pos + i * offset)
                screen.blit(right, right_rect)
                txtinp = font1.render(txtinp_disp[i], True, (0, 255, 0), None)
            else:
                wrong_rect = wrong.get_rect()
                wrong_rect.center = (3.6 * width // 4, default_pos + i * offset)
                screen.blit(wrong, wrong_rect)
                txtinp = font1.render(txtinp_disp[i], True, (255, 0, 0), None)
        elif len(txtinp_disp[i].strip()) == 1:
            if global_result[i] == 4:
                txtinp = font1.render(txtinp_disp[i].strip()+'-', True, (255, 255, 255), None)
            elif i == ptr and not global_result[ptr]:
                txtinp_disp[i] = ""
                global_result[i] = 4
                txtinp = font1.render(txtinp_disp[i], True, (255, 255, 255), None)
            elif global_result[i]:
                right_rect = right.get_rect()
                right_rect.center = (3.6 * width // 4, default_pos + i * offset)
                screen.blit(right, right_rect)
                txtinp = font1.render(txtinp_disp[i].strip()+'-', True, (0, 255, 0), None)
            else:
                wrong_rect = wrong.get_rect()
                wrong_rect.center = (3.6 * width // 4, default_pos + i * offset)
                screen.blit(wrong, wrong_rect)
                txtinp = font1.render(txtinp_disp[i].strip()+'-', True, (255, 0, 0), None)
        else:
            txtinp = font1.render("--", True, (255, 255, 255), None)
        txtinp_rect = txtinp.get_rect()
        txtinp_rect.center = (3 * width // 4, pos)
        #pygame.draw.rect(screen, (255, 255, 255), txtinp_rect, 2)
        screen.blit(txtinp, txtinp_rect)
        pos += offset

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_RIGHT:
                slaveState += 1
            elif event.key == pygame.K_LEFT:
                slaveState -= 1
            elif event.key == pygame.K_RETURN:
                check_strings(txtinp_disp, words, screen, ptr)
                ptr = (ptr + 1) % 6
                if lock[ptr]:
                    for j in range(6):
                        ptr = (ptr + 1) % 6
                        if not lock[ptr]: break
            elif event.key == pygame.K_BACKSPACE:
                # if len(txtinp_disp[ptr].strip()) < 1 and ptr > 0:
                #        ptr -= 1
                if not lock[ptr]:
                    txtinp_disp[ptr] = "  " + txtinp_disp[ptr].strip()[
                                                        :len(txtinp_disp[ptr].strip()) - 1] + "  "
                # if len(txtinp_disp[ptr].strip()) < 1:
                #    ptr -= 1
            else:
                for i in range(10):
                    if event.key == num_keys[i] or event.key == keys[i]:
                        if ptr < 6 and len(txtinp_disp[ptr].strip()) < 2:
                            txtinp_disp[ptr] = "  " + txtinp_disp[ptr].strip() + str(i) + "  "

    pygame.display.update()
    # time.sleep(0.5)




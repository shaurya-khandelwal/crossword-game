import sys, datetime, time, random
import pygame
from pygame.locals import *


#------------------Word Bags-------------------
word_bag1 = {20 : "money", 21 : "past", 22 : "end", 23 : "late", 24 :"present", 25 : "future", 26 : "new", 27 : "gate", 28 : "window", 29 : "board"}
word_bag2 = {31 : "allow", 32 : "stop", 33 : "traffic", 34 : "gamma", 35 : "alpha", 36 : "beta", 37 : "delta", 38 : "drama", 39 : "data", 40 : "laptop"}
word_bag3 = {51 : "mon", 52 : "pat", 53 : "en", 54 : "lte", 55 :"pesent", 56 : "fuure", 57 : "ndew", 58 : "gadte", 59 : "winddow", 60 : "boadrd"}
word_bag4 = {80 : "all", 79 : "stopdc", 78 : "traff", 76 : "gama", 75 : "alph", 74 : "bea", 73 : "dela", 72 : "drma", 71 : "dat", 70 : "aptop"}
num_keys = [pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5 , pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
txtinp_disp = ["     "] * 6
lock = [False] * 6
global_result = [100] * 6
count1 = 500
ptr = 0
running0 = False

#------------------Check Words----------------
def check_strings(param, words, window):
    global lock, global_result
    result = []
    for i in range(6):
        if param[i].strip() != "" and len(param[i].strip()) == 2:
            val = int(param[i].strip())
            try:
                if word_bag1[val] == words[i]:
                    result += [True]
                else:
                    result += [False]
            except:
                try:
                    if word_bag2[val] == words[i]:
                        result += [True]
                    else:
                        result += [False]
                except:
                    try:
                        if word_bag3[val] == words[i]:
                            result += [True]
                        else:
                            result += [False]
                    except:
                        try:    
                            if word_bag4[val] == words[i]:
                                result += [True]
                            else:
                                result += [False]          
                        except:
                            result += [False]
        else:
            result += [10]
    #print(result) 
    size = width, height = 1280, 720
    default_pos = height // 4
    pos = default_pos
    offset = height // 16
    blank = pygame.image.load(r'./media/blank.png')
    right = pygame.image.load(r'./media/right.png')
    wrong = pygame.image.load(r'./media/wrong.png')
    font = pygame.font.Font('freesansbold.ttf', 32)
    for i in range(6):
        if result[i] == 10:
            lock[i] = False
            blank_rect = right.get_rect()
            blank_rect.center = ((4.5 * width // 8), pos) 
            window.blit(blank, blank_rect)
        elif result[i]: 
            if result[i] != global_result[i]:
                global_result[i] = result[i]
                runn = True
                white = (255, 255, 255)
                green = (0, 255, 0)
                colour = [green, green, white]
                count = 0
                while runn:
                    count += 1
                    if count % 2 == 0:
                        col = colour[1]
                    elif count % 3 == 0:
                        col = colour[1]
                    else:
                        col = colour[2]
                    tex = font.render(param[i], True, col, (255, 255, 255))
                    tex_rect = tex.get_rect()
                    tex_rect.center = (width // 2, pos)
                    window.blit(tex, tex_rect)
                    pygame.display.flip()
                    if count > 500:
                        break
            tex = font.render(param[i], True, (0, 255, 0), (255, 255, 255))
            tex_rect = tex.get_rect()
            tex_rect.center = (width // 2, pos)
            window.blit(tex, tex_rect)
            lock[i] = True
            blank_rect = right.get_rect()
            blank_rect.center = ((4.5 * width // 8), pos) 
            window.blit(blank, blank_rect)
            right_rect = right.get_rect()
            right_rect.center = ((4.5 * width // 8), pos) 
            window.blit(right, right_rect)
        else:
            if result[i] != global_result[i]:
                global_result[i] = result[i]
                runn = True
                white = (255, 255, 255)
                red = (255, 0, 0)
                colour = [red, red, white]
                count = 0
                while runn:
                    count += 1
                    if count % 2 == 0:
                        col = colour[1]
                    elif count % 3 == 0:
                        col = colour[1]
                    else:
                        col = colour[2]
                    tex = font.render(param[i], True, col, (255, 255, 255))
                    tex_rect = tex.get_rect()
                    tex_rect.center = (width // 2, pos)
                    window.blit(tex, tex_rect)
                    pygame.display.flip()
                    if count > 500:
                        break
            tex = font.render(param[i], True, (255, 0, 0), (255, 255, 255))
            tex_rect = tex.get_rect()
            tex_rect.center = (width // 2, pos)
            window.blit(tex, tex_rect)
            lock[i] = False
            blank_rect = right.get_rect()
            blank_rect.center = ((4.5 * width // 8), pos) 
            window.blit(blank, blank_rect)
            wrong_rect = wrong.get_rect()
            wrong_rect.center = ((4.5 * width // 8), pos)
            window.blit(wrong, wrong_rect)
        pos += offset
    

#-----------------Random String----------------
enter = "ENTER !!"
def get_strings():
    random_keys = random.sample(list(word_bag1.values()), 1) + random.sample(list(word_bag2.values()), 1) + random.sample(list(word_bag3.values()), 2) + random.sample(list(word_bag4.values()), 2)
    return random_keys

#------------------Button---------------
def text_objects(text, font, black):
    if black:     
        textSurface = font.render(text, True, (0, 0, 0))
    else:
        textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def clear_screen(window):
    global ptr, txtinp_disp
    txtinp_disp = ["     "] * 6
    ptr = 0
    size = width, height = 1280, 720
    default_pos = height // 4
    pos = default_pos
    offset = height // 16
    image = pygame.image.load(r'./media/blank.png')
    for i in range(6):
        image_rect = image.get_rect()
        image_rect.center = ((4.5 * width // 8), pos) 
        window.blit(image, image_rect)
        pos += offset

def button0(msg, xc, yc, w, h, ic, ac, window, action=None):
    x = xc - w // 2
    y = yc - h // 2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf1, textRect1 = text_objects(msg, smallText, True)
    textRect1.center = ((x + (w / 2)), (y + (h / 2)))
    textSurf2, textRect2 = text_objects(msg, smallText, False)
    textRect2.center = ((x + (w / 2)), (y + (h / 2)))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ic, (x,y,w,h))
        window.blit(textSurf2, textRect2)
        if click[0] == 1:
            render_window(window)     
    else:
        pygame.draw.rect(window, ac, (x,y,w,h))
        window.blit(textSurf1, textRect1)
    #window.blit(textSurf2, textRect2)

def button1(msg, xc, yc, w, h, ic, ac, window, ptr, param, words, action=None):
    x = xc - w // 2
    y = yc - h // 2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, False)
    textRect.center = ((x + (w / 2)), (y + (h / 2)) )
    if x + w > mouse[0] > x and y + h > mouse[1] > y and ptr >= 5:
        pygame.draw.rect(window, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            action(param, words, window)         
    else:
        pygame.draw.rect(window, ac,(x,y,w,h))
        window.blit(textSurf, textRect)
    window.blit(textSurf, textRect)

def button2(msg, xc, yc, w, h, ic, ac, window, action=None):
    x = xc - w // 2
    y = yc - h // 2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, False)
    textRect.center = ((x + (w / 2)), (y + (h / 2)) )
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            action(window)         
    else:
        pygame.draw.rect(window, ac,(x,y,w,h))
        window.blit(textSurf, textRect)
    window.blit(textSurf, textRect)

def render_start_window():
    pygame.init()  
    size = width, height = 1280, 720
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Decrypt Word')
    font0 = pygame.font.Font('freesansbold.ttf', 64)
    global running0
    running0 = True
    while running0:
        window.fill((255, 255, 255))
        title = font0.render("D E C R Y P T  W O R D", True, (0, 0, 0), (255, 255, 255))
        title_rect = title.get_rect()
        title_rect.center = (width // 2, height // 3)
        window.blit(title, title_rect)
        button0("PLAY GAME !!", width // 2, 3 * height // 5, 150, 60, (0, 0, 0), (255, 255, 255), window)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running0 = False

def render_window(window):
    window.fill((0, 0, 0))
    global ptr, txtinp_disp
    size = width, height = 1280, 720
    font = pygame.font.Font('freesansbold.ttf', 32)
    curr_time = datetime.datetime.now()
    total_time = curr_time + datetime.timedelta(minutes=15)
    start_toggle = -1
    words = get_strings()
    running = True
    while running: 
        #-----------------------Render timer------------------
        if start_toggle < 0: 
            curr_time = datetime.datetime.now()
        time_diff = total_time - curr_time
        mm, ss = (time_diff.seconds // 60), (time_diff.seconds % 60)
        time_disp = str(mm) + " : " + str(ss)
        timer = font.render(time_disp, True, (255, 255, 255), (0, 0, 0))
        timer_bg = font.render("        ", True, (255, 255, 255), (0, 0, 0))
        timer_bg_rect = timer_bg.get_rect()
        timer_bg_rect.center = (5 * width // 6, height // 2) 
        timer_rect = timer.get_rect()
        timer_rect.center = (5 * width // 6, height // 2)
        window.blit(timer_bg, timer_bg_rect)
        window.blit(timer, timer_rect)

        #----------------------Render Strings------------------
        default_pos = height // 4
        pos = default_pos
        offset = height // 16
        for word in words:
            word_disp = font.render(str(word), True, (0, 0, 0),  (255, 255, 255))
            spaces = "                      "
            box = font.render(spaces, True, (0, 0, 0),  (255, 255, 255))
            box_rect = box.get_rect()
            words_rect = word_disp.get_rect()
            words_rect.center = (width // 4.2, pos)
            box_rect.center = (width // 4.2, pos)
            window.blit(box, box_rect)
            window.blit(word_disp, words_rect)
            pos += offset

        #----------------------Render Button-------------- 
        button1(enter, width // 3, height // 2 + 3 * offset, 100, 60, (0, 0, 0), (0, 0, 0), window, ptr, txtinp_disp, words, check_strings)
        button2("CLEAR", width // 2, height // 2 + 3 * offset, 100, 60, (0, 0, 0), (0, 0, 0), window, clear_screen)
        #----------------------Input------------------------
        pos = default_pos
        offset = height // 16
        for i in range(6):
            txtinp = font.render(txtinp_disp[i], True, (0, 0, 0), (255, 255, 255))
            txtinp_rect = txtinp.get_rect()
            txtinp_rect.center = (2 * width // 4 , pos)
            window.blit(txtinp, txtinp_rect)
            check_strings(txtinp_disp, words, window)
            pos += offset
        #enter += str(click[0]) + str(click[1])
        #print(click, file=sys.stderr)
        

        #----------------------Display window------------------
        pygame.display.flip()

        #---------------------Event Handling-------------------
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start_toggle *= -1
                    total_time = time_diff + datetime.datetime.now()
                elif event.key == pygame.K_r:
                    total_time = datetime.datetime.now() + datetime.timedelta(minutes=15)
                    if start_toggle > 0:
                        curr_time = datetime.datetime.now()
                elif event.key == pygame.K_RETURN:
                    ptr = (ptr + 1) % 6
                    if lock[ptr]:    
                        for j in range(6):
                            ptr = (ptr + 1) % 6
                            if not lock[ptr]: break
                elif event.key == pygame.K_BACKSPACE:
                    #if len(txtinp_disp[ptr].strip()) < 1 and ptr > 0:
                    #        ptr -= 1
                    if not lock[ptr]:    
                        txtinp_disp[ptr] = "  " + txtinp_disp[ptr].strip()[:len(txtinp_disp[ptr].strip()) - 1] + "  "
                    #if len(txtinp_disp[ptr].strip()) < 1:
                    #    ptr -= 1
                else:
                    for i in range(10):
                        if event.key == num_keys[i] or event.key == keys[i]:
                            if ptr < 6 and len(txtinp_disp[ptr].strip()) < 2:
                                txtinp_disp[ptr] = "  " + txtinp_disp[ptr].strip() + str(i) + "  "
            if event.type == pygame.QUIT:
                running = False
                global running0
                running0 = False


if __name__ == "__main__":
    render_start_window()
import math
import random
import pygame
from file import Button
import sys
save_file_path = "save_data.txt"
width = 1280
height =720
pygame.init()
display = pygame.display.set_mode((width, height))
BG=pygame.image.load("data\images\wallpaperflare.com_wallpaper (2).jpg")
font=pygame.font.Font('thunderstrike.ttf',20)
music=pygame.mixer.music.load("1min-2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3")
pygame.mixer.music.play(-1)
popsound=pygame.mixer.Sound('laser-gun-19sf.mp3')
"""class playeable:
    def __init__(self,on,off):
        if on==0:
            self.on=popsound.play()
        elif off==2:
            self.off=popsound.stop()"""

def get_font(size):
    return pygame.font.Font("thunderstrikehalf.ttf", size)

#to save the score
def save_score(score):
    with open(save_file_path, "w") as file:
        file.write(str(score))
#to load the score
def load_score():
    try:
        with open(save_file_path, "r") as file:
            score = int(file.read())
            return score
    except FileNotFoundError:
        return 0

#this is the main menu window
def main_menu():
    pygame.display.set_caption("MAIN MENU")
    while True:
        display.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #color for logo defalult"#b68f40"
        MENU_TEXT = get_font(80).render(" AIM TRAINER", True, "#e6cc00")
        MENU_RECT = MENU_TEXT.get_rect(center=(640,140))
        PLAY_BUTTON = Button(image=pygame.image.load("data\images\Play Rect.png"), pos=(640,250),
                             text_input="PLAY", font=get_font(65), base_color="#ffffff", hovering_color="#90EE90")
        OPTIONS_BUTTON = Button(image=pygame.image.load("data\images\Quit Rect.png"), pos=(640,400),
                             text_input="OPTIONS", font=get_font(65), base_color="#ffffff", hovering_color="#90EE80")
        QUIT_BUTTON = Button(image=pygame.image.load("data\images\Quit Rect.png"), pos=(640,550 ),
                                text_input="QUIT", font=get_font(65), base_color="#ffffff", hovering_color="#ffb3b2")

        display.blit(MENU_TEXT,MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    setting()
        pygame.display.update()
text_font=pygame.font.SysFont('font.tiff',30)

def content(text,font,text_col,x,y):
    while True:
        img=font.render(text,True,text_col)
        display.blit(img,(x,y))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                main_menu()
            pygame.display.update()
black=(0,0,0)
white=(255,255,255)
sett=pygame.image.load("data\images\wallpaperflare.com_wallpaper.jpg")


#for the setting options
def setting():
    pygame.display.set_caption("settings")
    while True:
        display.blit(sett,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # color for logo defalult"#b68f40"
        MENU_TEXT = get_font(70).render(" SETTINGS", True, "#e6cc09")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("data\images\Play Rect.png"), pos=(640, 250),
                             text_input="MUSIC OFF", font=get_font(50), base_color="#ffffff", hovering_color="#ffb3b2")
        QUIT_BUTTON = Button(image=pygame.image.load("data\images\Quit Rect.png"), pos=(640, 400),
                             text_input="MUSIC ON", font=get_font(50), base_color="#ffffff", hovering_color="#90EE90")
        OPTIONS_BUTTON = Button(image=pygame.image.load("data\images\Quit Rect.png"), pos=(640, 550),
                                text_input="RETURN", font=get_font(50), base_color="#ffffff", hovering_color="#90EE90")
        """
        OPTIONS_BUTTON1 = Button(image=pygame.image.load("data\images\Quit Rect.png"), pos=(640,550),
                                text_input="SFX OFF", font=get_font(50), base_color="#ffffff", hovering_color="#ffb3b2")"""
        display.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, QUIT_BUTTON,OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                """if OPTIONS_BUTTON1.checkForInput(MENU_MOUSE_POS):
                    offvalue=2
                    playeable(offvalue,0)"""
        pygame.display.update()


#this is the main game loop
score_value=0
def game():
    global score_value
    pygame.display.set_caption("game play")
    black=(0,0,0)
    red=(255,0,0)
    colors=[red]
    display.fill(black)
    clock=pygame.time.Clock()
    cx = random.randint(20, width - 20)
    cy = random.randint(20, height - 20)
    width_circle = random.randint(14, 20)
    pygame.draw.circle(display,random.choice(colors),(cx,cy),width_circle)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                main_menu()
        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]
        click=pygame.mouse.get_pressed()
        sqx=(x-cx)**2
        sqy=(y-cy)**2
        if math.sqrt(sqx+sqy)<width_circle and click[0]==1:
            popsound.play()
            score_value = score_value + 10
            display.fill(black)
            cx = random.randint(20, width - 20)
            cy = random.randint(20, height - 20)
            width_circle = random.randint(14, 20)
            pygame.draw.circle(display, random.choice(colors), (cx, cy), width_circle)
            #playeable(onvalue,offvalue)
        textx = 10
        texty = 10

#this is for the score displaying
        def disply_scroe(x, y):
            score = font.render("score:" + str(score_value), True, (255, 255, 255))
            if score_value>100:
                score=font.render("Highscore:"+str(score_value),True,(255,255,255))
            display.blit(score, (x, y))
        disply_scroe(textx, texty)
        pygame.display.update()
        clock.tick()
main_menu()


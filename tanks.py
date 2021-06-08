import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
yellow = (200,200,0)
green = (34, 177, 76)
light_green = (0, 255, 0)
light_red = (255,0,0)
light_yellow = (255,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')

#icon = pygame.image.load('apple30px.png') #icon size is generally 32x32
#pygame.display.set_icon(icon)

#img = pygame.image.load('snakehead20px.png')
#appleimg = pygame.image.load('apple30px.png')

clock = pygame.time.Clock()


mainTankX = display_width * 0.9
mainTankY = display_height * 0.9

tankWidth = 40
tankHeight = 20

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
    paused = True

    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue or Q to quit", black, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)

        clock.tick(5)

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + (buttonwidth/2)), (buttony + (buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def tank(x, y):
    x = int(x)
    y = int(y)
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))

def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: Up and Down arrows", black, 10)
        message_to_screen("Move Tanks: Left and Right arrows", black, 50)
        message_to_screen("Pause: P", black, 90)
        
        button("play", 150, 500, 100, 50, green, light_green, "play")
        button("main", 350, 500, 100, 50, yellow, light_yellow, "main")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+width>cur[0]>x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "controls":
                game_controls()
            elif action == "play":
                gameLoop()
            elif action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    
    text_to_button(text, black, x, y, width, height)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0, 0])

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks", green, -100, "large")
        message_to_screen("The objective is to shoot and destroy", black, -30)
        message_to_screen("the enemy tank before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy the harder they get.", black, 50)
        #message_to_screen("Press C to play, P to pause or Q to quit", black, 180)
        
        button("play", 150, 500, 100, 50, green, light_green, "play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    gameExit = False
    gameOver = False

    FPS = 15

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game over", red, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to Quit", black, 50, size="medium")
            pygame.display.update()

        while gameOver == True:
            #gameDisplay.fill(white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)

        tank(mainTankX, mainTankY)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
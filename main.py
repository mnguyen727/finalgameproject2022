import pygame
import pygame as pg
from pygame.sprite import Sprite
from sys import exit
import random
from random import randint
from pygame import mixer

#SOURCES CITED -
#https://www.youtube.com/watch?v=AY9MnQ4x3zk&t (THIS GUY WAS THE MOST HELPFUL AT BUILDING FOUNDATION)
#https://www.youtube.com/watch?v=CasqhmeopnU&t
#https://pythonprogramming.net/adding-sounds-music-pygame/ (HELPED WITH MUSIC)
#https://youtu.be/MlWpE2uZ2QY (LINK TO SONG USED. 8-BIT CHAINSAW MAN OPENING)
#https://www.youtube.com/watch?v=GMBqjxcKogA&t (HELPED WITH MENU SCREEN CHANGE)
#https://www.youtube.com/watch?v=dQw4w9WgXcQ

#initialize pygame
pygame.init()

#normal start settings
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,550))

#screen blit space.png as background
bg = pygame.image.load('space.png')
screen.blit(bg,(0,0))

#variable we use for scoreboard
SCORE = 0

#def scoreboard 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('8-BIT WONDER.TTF')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

#loads ship sprite and sets parameters
ship = pygame.image.load('tiny_ship.png')
ship_y_pos = 225
ship_x_pos = 140

#loading all rocks sprites
rock = pygame.image.load('rock.png')
rock1 = pygame.image.load('rock.png')
rock2 = pygame.image.load('rock.png')
rock3 = pygame.image.load('rock.png')
rock4 = pygame.image.load('rock.png')
rock5 = pygame.image.load('rock.png')
rock6 = pygame.image.load('rock.png')
rock7 = pygame.image.load('rock.png')
rock8 = pygame.image.load('rock.png')
rock9 = pygame.image.load('rock.png')

#loads bullet sprite
bullet = pygame.image.load('bullet.png')
#sets the bullet pos to ship pos
bullet_x_pos = ship_x_pos

#all rocks position variables that are used later in the loop
rock_x_pos = 1472
rock_x_pos1 = 1600
rock_x_pos2 = 1092
rock_x_pos3 = 2274
rock_x_pos4 = 1400
rock_x_pos5 = 1893
rock_x_pos6 = 1375
rock_x_pos7 = 1321
rock_x_pos8 = 1893
rock_x_pos9 = 1283

#instantiates space shooter image on menu screen
spaceshooter = pygame.image.load('Space Shooter.png')
screen.blit(spaceshooter,(250, -140))

#instantiates start image on menu screen
start = pygame.image.load('Start.png')
screen.blit(start,(250,45))

#music
mixer.music.load('csm.wav')
mixer.music.play(-1)

#we need this variable for the while loop
a = 0

#game loop
while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #stops the ship from going further off the screen
    if ship_y_pos == (50):
        ship_y_pos += 5

    if ship_y_pos == (480):
        ship_y_pos -= 5

    #instantiates SPACE as start key for game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:

    #changed variable so that screen can be blit
        a = 1         
    while a > 0: 
        screen.blit(bg,(0,0))   

        #instantiates all rock sprites and moves the rocks to the left at varying speeds.
        screen.blit(rock,(rock_x_pos,50))
        rock_x_pos -= 10
        #once the rock reaches -100 on the x-axis it will blit the rock back to the right side of the screen.
        if rock_x_pos < -100: rock_x_pos = 1345

        screen.blit(rock1,(rock_x_pos1,150))
        rock_x_pos1 -= 8
        if rock_x_pos1 < -100: rock_x_pos1 = 1458
        
        screen.blit(rock2,(rock_x_pos2,250))
        rock_x_pos2 -= 11
        if rock_x_pos2 < -100: rock_x_pos2 = 1842

        screen.blit(rock3,(rock_x_pos3,350))
        rock_x_pos3 -= 9
        if rock_x_pos3 < -100: rock_x_pos3 = 1152

        screen.blit(rock4,(rock_x_pos4,450))
        rock_x_pos4 -= 7
        if rock_x_pos4 < -100: rock_x_pos4 = 1756

        screen.blit(rock5,(rock_x_pos5,200))
        rock_x_pos5 -= 7.5
        if rock_x_pos5 < -100: rock_x_pos5 = 1023

        screen.blit(rock6,(rock_x_pos6,300))
        rock_x_pos6 -= 9.5
        if rock_x_pos6 < -100: rock_x_pos6 = 1091
        
        screen.blit(rock7,(rock_x_pos7,400))
        rock_x_pos7 -= 10.5
        if rock_x_pos7 < -100: rock_x_pos7 = 1142






        #instantiates ship posiition and movement
        screen.blit(ship,(ship_x_pos,ship_y_pos))
        
        #if w is pressed ship moves up
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                ship_y_pos -= 5

        #if s is pressed ship moves down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
                ship_y_pos += 5

        #if a is pressed ship moves left
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
                ship_x_pos -= 7

        #if d is pressed ships moves right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
                ship_x_pos += 7

        #my attempt at instantiating a bullet (it just puts the bullet on top of ship) press p key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            screen.blit(bullet,(ship_x_pos,ship_y_pos)) 
            bullet_x_pos += 100

        #instantiates the score board on the screen
        draw_text("SCORE: " + str(SCORE), 22, (255,255,255), 930, 25)

        #uses clock.tick as the base for score
        if clock.tick(120):
            SCORE += 1

        #break command is needed or else this loop won't work
        break
        
#updates
    pygame.display.update() 
    clock.tick(120)

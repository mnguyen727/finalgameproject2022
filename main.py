import pygame
from sys import exit
import random
from random import randint
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,550))
bg = pygame.image.load('space.png')
screen.blit(bg,(0,0))

ship = pygame.image.load('tiny_ship.png')
ship_rect = ship.get_rect()

ship_y_pos = 225
ship_x_pos = 140

rock = pygame.image.load('rock.png')
rock1 = pygame.image.load('rock.png')
rock2 = pygame.image.load('rock.png')
rock3 = pygame.image.load('rock.png')
rock4 = pygame.image.load('rock.png')



bullet = pygame.image.load('bullet.png')
bullet_x_pos = ship_x_pos

rock_x_pos = 1000
rock_x_pos1 = 1000
rock_x_pos2 = 1000
rock_x_pos3 = 1000
rock_x_pos4 = 1000






text_x = 250
text_y = -140

spaceshooter = pygame.image.load('Space Shooter.png')
screen.blit(spaceshooter,(text_x, text_y))




start = pygame.image.load('Start.png')
screen.blit(start,(250,45))

#music
mixer.music.load('csm.wav')
mixer.music.play(-1)
pygame.mixer.music.play()


a = 0

#game loop
while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if ship_y_pos == (0):
        ship_y_pos += 5

    if ship_y_pos == (530):
        ship_y_pos -= 5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:

        a = 1         
    while a > 0: 
        screen.blit(bg,(0,0))   
        screen.blit(rock,(rock_x_pos,50))
        rock_x_pos -= 14
        if rock_x_pos < -100: rock_x_pos = 1000 

        screen.blit(rock1,(rock_x_pos1,150))
        rock_x_pos1 -= 16
        if rock_x_pos1 < -100: rock_x_pos1 = 1000

        screen.blit(rock2,(rock_x_pos2,250))
        rock_x_pos2 -= 13
        if rock_x_pos2 < -100: rock_x_pos2 = 1000

        screen.blit(rock3,(rock_x_pos3,350))
        rock_x_pos3 -= 12
        if rock_x_pos3 < -100: rock_x_pos3 = 1000

        screen.blit(rock4,(rock_x_pos4,450))
        rock_x_pos4 -= 15
        if rock_x_pos4 < -100: rock_x_pos4 = 1000
            

        screen.blit(ship,(ship_x_pos,ship_y_pos))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                ship_y_pos -= 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
                ship_y_pos += 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
                screen.blit(bullet,(ship_x_pos,ship_y_pos)) +1
            

        score_value = 0
        font = pygame.font.Font('8-BIT WONDER.TTF',32)

        score_x = 740
        score_y = 10



        def show_score(x, y):
            score = font.render("Score :" + str(score_value), True, (225, 255, 255))
            screen.blit(score, (x, y))

        show_score(score_x, score_y)

            
        break
        
#updates
    pygame.display.update() 
    clock.tick(60)

#Matthew Nguyen

import pygame
from sys import exit
import random
from random import randint
from pygame import mixer

#starts pygame
pygame.init()
screen = pygame.display.set_mode((1000,550))
pygame.display.set_caption('space shooter')
clock = pygame.time.Clock()

#MUSIC PRETTY COOL
mixer.music.load ('csm.wav')
mixer.music.play (-1)

ship_surface = pygame.Surface((100,100))

bg = pygame.image.load('space.png')

#bullet
bullet = pygame.image.load('new_bullet.png')

#ship/player
ship = pygame.image.load('tiny_ship.png')
ship_y_pos = 140

#rocks lol
rock = pygame.image.load('rock.png')
rock1 = pygame.image.load('rock.png')
rock2 = pygame.image.load('rock.png')
rock3 = pygame.image.load('rock.png')
rock4 = pygame.image.load('rock.png')

rock_x_pos = 1000
rock_x_pos1 = 1000
rock_x_pos2 = 1000
rock_x_pos3 = 1000
rock_x_pos4 = 1000

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#instantiates images and movement
    screen.blit(bg,(0,0))

    screen.blit(ship,(140,ship_y_pos))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ship_y_pos -= 5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        ship_y_pos += 5

    screen.blit(rock,(rock_x_pos,50))
    rock_x_pos -= 10
    if rock_x_pos < -100: rock_x_pos = 1000

    screen.blit(rock1,(rock_x_pos1,150))
    rock_x_pos1 -= 12
    if rock_x_pos1 < -100: rock_x_pos1 = 1000

    screen.blit(rock2,(rock_x_pos2,250))
    rock_x_pos2 -= 9
    if rock_x_pos2 < -100: rock_x_pos2 = 1000

    screen.blit(rock3,(rock_x_pos3,350))
    rock_x_pos3 -= 8
    if rock_x_pos3 < -100: rock_x_pos3 = 1000

    screen.blit(rock4,(rock_x_pos4,450))
    rock_x_pos4 -= 11
    if rock_x_pos4 < -100: rock_x_pos4 = 1000

    #updates
    pygame.display.update()
    clock.tick(60)
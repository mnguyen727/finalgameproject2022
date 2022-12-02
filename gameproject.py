# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
# from platform import platform
from operator import truediv
from tkinter import PhotoImage
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
from PIL import Image 
from tkinter import *
import tkinter as tk
import pygame

                                                                  
import pygame
from pygame.locals import *

#attempt at adding a background
pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('pixelartbg.png')
bg_img = pygame.transform.scale(bg_img,(width,height))
i = 0
runing = True
while runing:
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    window.blit(bg_img,(width+i,0))
    if (i==-width):
        window.blit(bg_img,(width+i,0))
        i=0
    i-=1
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()

vec = pg.math.Vector2



# game settings 
WIDTH = 1440
HEIGHT = 720
FPS = 60
CONTROLS = 1

# player settings
PLAYER_GRAV = 0.6
PLAYER_FRIC = 0.1
SCORE = 100

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# sprites...
# sprites...
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def controls(self):
        if CONTROLS == 1:
            keys = pg.key.get_pressed()
            # if keys[pg.K_w]:
            #     self.acc.y = -5
            if keys[pg.K_a]:
                self.acc.x = -2
            # if keys[pg.K_s]:
            #     self.acc.y = 5
            if keys[pg.K_d]:
                self.acc.x = 2
    
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -22
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        # self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.9 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Mob2(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x += 1

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

  
# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiate classes
player = Player()
plat = Platform(1, 690, 2000, 35)
plat2 = Platform(400, 365, 200, 25)

for i in range(5):
    m = Mob(1300, 190, 300, 300)
    all_sprites.add(m)
    mobs.add(m)
    print(m)

# add player to all sprites group
all_sprites.add(player)
all_plats.add(plat, plat2)

# add platform to all sprites group
all_sprites.add(plat)
all_sprites.add(plat2)

# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    mobhits = pg.sprite.spritecollide(player, mobs, False)
    if mobhits:
        print("ive struck a mob")
        player.vel.x = -8
        
        player.vel.y = 0
        SCORE -= 1
        CONTROLS = 0
    else:
        CONTROLS = 1

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw text
    draw_text("HEALTH: " + str(SCORE), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
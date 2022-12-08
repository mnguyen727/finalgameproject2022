from settings import *
from pygame.locals import *

vec = pg.math.Vector2

# game settings 
WIDTH = 1200
HEIGHT = 600
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

#instantiate the class
class player(pygame.sprite.Sprite):
    def __inity__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('tiny_ship.png')
            self.rect = self.image.get_rect()
            self.rect.center = [x,y]

player_group = pygame.sprite.Sprite.groups()

ship = player(100, int(HEIGHT / 2))

player_group.add(ship)


#moving background
pygame.init()
width = 1200
height = 600
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('space.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

player_group.draw(window)

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
pygame.quit()
pygame.quit()

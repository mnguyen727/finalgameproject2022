from settings import *

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

#instantiate the class
player = Player()

pygame.init()
width = 1200
height = 600
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('space.png')
bg_img = pygame.transform.scale(bg_img,(width,height))
clock = pg.time.Clock()

running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
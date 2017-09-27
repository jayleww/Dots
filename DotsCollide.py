import pygame, math, sys, random
from pygame.locals import *

width, height = 800,700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        playerx = position[0]
        playery = position[1]
        self.health = 100
        self.exp = 0
        self.colour = (0,0,255)
        self.size = (30,15)
        #self.rect takes surface, colour, location, size coords
        self.rect = pygame.draw.rect(screen,self.colour, ((playerx,playery),self.size))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-1,0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(1,0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0,-1)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0,1)

    def update(self, surface):
        pygame.draw.rect(screen, self.colour, self.rect)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemyx = random.randint(0,width)
        enemyy = random.randint(0,height)
        self.enemyhealth = random.randint(5,205)
        self.enemycolour = 255 - self.enemyhealth
        self.rect = pygame.draw.rect(screen, (self.enemycolour,0,0), ((enemyx, enemyy),(10,10)))

    def draw_enemy(self, surface):
        pygame.draw.rect(screen, (self.enemycolour,0,0), self.rect)

rect = screen.get_rect()
player = Player(rect.center)
##enemyx = random.randint(0,width)
##enemyy = random.randint(0,height)
enemy = Enemy()
expover = 0

while 1:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    if player.rect.colliderect(enemy):
        luckroll = random.randint(1,3)
        playerstrength = player.health*luckroll + 50
        if playerstrength > enemy.enemyhealth:
            player.exp += playerstrength - enemy.enemyhealth
            if player.exp > 100:
                expover += player.exp - 100
                player.exp = 0
                player.size = (expover,expover)
        else:
            playerloss = enemy.enemyhealth - playerstrength
            player.size = (playerloss,playerloss)
        enemy = Enemy()
    
    player.handle_keys()            
    player.update(screen)
    enemy.draw_enemy(screen)
    pygame.display.update()
    
    
            
            
        

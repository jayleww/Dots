import pygame, math, sys, random
from pygame.locals import *

width, height = 1024,768
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        playerx = position[0]
        playery = position[1]
        #self.rect takes surface, colour, location, size coords
        self.rect = pygame.draw.rect(screen,(0,0,255), ((playerx,playery),(15,15)))

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
        pygame.draw.rect(screen, (0,0,255), self.rect)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemyx = random.randint(0,width)
        enemyy = random.randint(0,height)
        self.rect = pygame.draw.rect(screen, (255,0,0), ((enemyx, enemyy),(10,10)))

    def draw_enemy(self, surface):
        pygame.draw.rect(screen, (255,0,0), self.rect)

rect = screen.get_rect()
player = Player(rect.center)
##enemyx = random.randint(0,width)
##enemyy = random.randint(0,height)
enemy = Enemy()

while 1:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    if player.rect.colliderect(enemy):
        enemy = Enemy()
    
    player.handle_keys()            
    player.update(screen)
    enemy.draw_enemy(screen)
    pygame.display.update()
    
    
            
            
        

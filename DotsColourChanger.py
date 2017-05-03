import pygame, math, sys, random
from pygame.locals import *

pygame.init()
width, height = 800,700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
##Playing with ways to show the results of "battles". Trying colour changes, or size adjustments.
class Player(pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        playerx = position[0]
        playery = position[1]
        self.health = 100
        self.exp = 0
        self.colour = (0,0,255)
        self.size = (15,15)
        #self.rect takes surface, colour, location, size coords
        self.rect = pygame.draw.rect(screen,self.colour, ((playerx,playery),self.size))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-2,0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(2,0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0,-2)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0,2)

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
enemydeft = 0
running = 1
exitcode = 0
while running:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit(0)
    if player.rect.colliderect(enemy):
        enemydeft += 1
        if enemydeft <= 25:
            rcolourmod = 10*enemydeft
            player.colour = (rcolourmod,0,255)
        if (enemydeft > 25 and enemydeft <= 50):
            gcolourmod = 10*(enemydeft-25)
            player.colour = (rcolourmod,gcolourmod,255)
        if enemydeft > 50:
            running = 0
            
        enemy = Enemy()
    font = pygame.font.Font(None,24)
    currentcolour = font.render(str(player.colour), True, (255,255,255))
    textRect = currentcolour.get_rect()
    textRect.topright = [635,5]
    screen.blit(currentcolour,textRect)
    
    player.handle_keys()            
    player.update(screen)
    enemy.draw_enemy(screen)
    pygame.display.update()


if exitcode == 0:
    pygame.font.init()
    text = font.render("Enemies eaten: "+str(enemydeft), True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(text,textRect)
    
    
    
    
            
            
        

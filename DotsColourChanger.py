import pygame, math, sys, random, time
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
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height
        pygame.draw.rect(screen, self.colour, self.rect)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemyx = random.randint(10,width-10)
        enemyy = random.randint(10,height-10)
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
#starttime = time.time()
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
            exitcode = 1
        enemy = Enemy()
    #playtime = time.time() - starttime
    font = pygame.font.Font(None,24)
    currentcolour = font.render(str(player.colour), True, (255,255,255))
    textRect = currentcolour.get_rect()
    textRect.topright = [width-10,5]
    timedisplay = font.render(str((pygame.time.get_ticks())/60000)+":"+str((pygame.time.get_ticks())/1000%60), True, (255,255,255))
    timerRect = timedisplay.get_rect()
    timerRect.topright = [35,5]
    screen.blit(timedisplay,timerRect)
    screen.blit(currentcolour,textRect)
    
    player.handle_keys()            
    player.update(screen)
    enemy.draw_enemy(screen)
    pygame.display.update()


if exitcode == 1:
    #endtime = time.time() - starttime
    pygame.font.init()
    font = pygame.font.Font(None,24)
    text = font.render("Enemies eaten: "+str(enemydeft), True, (255,255,255))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(text,textRect)
    pygame.display.update()
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit(0)
    
    
    
    
            
            
        

import pygame, sys, time
pygame.init()

black = 0, 0, 0
playerlist = []
alienlist = []
obstaclelist = []
elementdic = []

def screenupdate(screen):
    pygame.time.delay(1000)
    screen.fill(black)
    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
    
    pygame.display.flip()
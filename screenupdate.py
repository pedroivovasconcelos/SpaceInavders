import pygame, sys, time
pygame.init()

black = 0, 0, 0

def screenupdate(objectslist):
    size = width, height = 224, 256
    screen = pygame.display.set_mode(size)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(black)
        for mob in objectslist:
            screen.blit(mob, mob.rect)
        pygame.display.flip()
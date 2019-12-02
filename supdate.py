import pygame, sys, time

black = 0, 0, 0

def screenupdate(size, playerdict):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')
    while True:
        print(playerdict)
        time.sleep(1/30)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        if not playerdict:
            if 'shoots' in playerdict and len(playerdict['shoots'][1] != 0):
                for shoots in playerdict['shoots'][1]:
                    screen.blit(playerdict['shoots'][0], shoots)

            if 'player' in playerdict:
                screen.blit(playerdict['player'][0],playerdict['player'][0])
    
        pygame.display.flip()
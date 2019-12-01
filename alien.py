import threading, pygame, sys
pygame.init()    

black = 0, 0, 0

if __name__ == "__main__":
    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    x = 20
    y = 20
    alien = pygame.image.load("alien.png")
    alienrect = alien.get_rect()
    alienlist = []
    laser = pygame.image.load("laser.png")
    laserlist = []

    for level in range(0,20):
        counter = 0
        row = 0
        for a in range(level+1):
            newalienrect = alienrect.move(a*50-row*250,alienrect.top+50*row)
            alienlist.append(newalienrect)
            counter+=1
            if counter == 5:
                counter = 0
                row+=1
            
        while 1:
            pygame.time.delay(1000)
            screen.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()


            if len(laserlist) != 0:
                for index, aliens in enumerate(laserlist):
                    laserlist[index] = aliens.move(0,-5)
                    if 0 > laser.bottom:
                        laserlist.pop(index)
                    else:
                        screen.blit(alien, laserlist[index])
            
            for aliens in alienlist:
                screen.blit(alien, aliens)
            pygame.display.flip()

            break

import pygame, sys, time, gamestart

def alien(gv):
    alien = pygame.image.load("images/alien.png")
    alienrect = alien.get_rect()
    alienlist = []
    laser = pygame.image.load("images/laser.png")
    laserlist = []

    for gv.level in range(0,20):
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

            if len(laserlist) != 0:
                for index, aliens in enumerate(laserlist):
                    laserlist[index] = aliens.move(0,-5)
                    if 0 > laser.bottom:
                        laserlist.pop(index)

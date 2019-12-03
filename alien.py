import pygame, time, gamestart, threading
from random import random

counter = 0
row = 0

def lasershot(gv, index, lt, isshooting):
    #cria e move se houver criado
    if(isshooting == False):
        isshooting = True
        alienrect = gv.aliendict['alien'][1][index]
        laserrect = gv.aliendict['laser'][0].get_rect()
        laserrect = laserrect.move(alienrect.left+15,alienrect.bottom)
        gv.aliendict['laser'][1][lt] = laserrect
    else:
        if lt in gv.aliendict['laser'][1].keys():
            laserrect = gv.aliendict['laser'][1][lt]
            laserrect = laserrect.move(0,3)
            gv.aliendict['laser'][1][lt] = laserrect
            if gv.size[1] < laserrect.top:
                gv.aliendict['laser'][1].pop(lt)
                isshooting = False
        else:
            isshooting = False

    return isshooting

def movealien(gv, index, direction, limitmove):
    alienrect = gv.aliendict['alien'][1][index]
    #em linha e em coluna
    if(gv.size[0] != alienrect.right and direction and limitmove > 0):
        alienrect = alienrect.move(1,0)
        limitmove-=1
    elif(0 != alienrect.left and not direction and limitmove > 0):
        alienrect = alienrect.move(-1,0)
        limitmove-=1
    else:
        alienrect = alienrect.move(0,10)
        direction = not direction
        limitmove = 50
        if gv.size[1] < alienrect.top:
            gv.aliendict['alien'][1].pop(index)
            index = -1
    if index != -1:
        gv.aliendict['alien'][1][index] = alienrect

    return direction, limitmove, index


def talien(gv, alienrect, alock):
    global counter
    global row
    alock.acquire
    alienrect = alienrect.move(counter*50,alienrect.top+50*row)
    gv.aliendict['alien'][1].append(alienrect)
    index = gv.aliendict['alien'][1].index(alienrect)
    counter+=1
    indexline = counter
    if counter == 5:
        counter = 0
        row+=1
    alock.release

    direction = True
    limitmove = 50
    isshooting = False
    while True:
        time.sleep(gv.fps)

        if random() > 0.999 and not isshooting:
            isshooting = lasershot(gv, index, threading.currentThread().getName(), isshooting)
        elif(isshooting):
            isshooting = lasershot(gv, index, threading.currentThread().getName(), isshooting)

        direction, limitmove, index = movealien(gv,index, direction, limitmove)
        if index == -1:
            break
        if len(gv.aliendict['alien'][1]) == 0:
            break
        
    gv.level+=1
    if(gv.level <= 20):
        for _ in range(gv.level):
            at = threading.Thread(target = talien, args = (gv,alienrect,alock,))
            at.daemon = True
            at.start
    super.join()
        

def aliens(gv):
    alien = pygame.image.load("images/alien.png")
    alienrect = alien.get_rect()
    alienlist = []
    laser = pygame.image.load("images/laser.png")
    laserdict = dict()

    gv.aliendict['alien'] = [alien,alienlist]
    gv.aliendict['laser'] = [laser,laserdict]
    
    #para ir ao level desejado
    alock = threading.Lock()
    for t in range(gv.level-1):
        at = threading.Thread(target = talien, args = (gv,alienrect,alock,))
        at.daemon = True
        at.start()
    talien(gv,alienrect,alock)

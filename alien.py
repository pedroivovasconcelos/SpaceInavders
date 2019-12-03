import pygame, sys, time, gamestart, threading

counter = 0
row = 0
def talien(gv, alienrect, alock):
    global counter
    global row
    alock.acquire
    newalienrect = alienrect.move(counter*50-row*250,alienrect.top+50*row)
    gv.aliendict['alien'][1].append(newalienrect)
    counter+=1
    if counter == 5:
        counter = 0
        row+=1
    alock.release
    print(counter,row)

    while True:
        time.sleep(gv.fps)
        # laser = gv.aliendict['laser'][0]
        # laserlist = gv.aliendict['laser'][1]
        # if len(laserlist) != 0:
        #     for index, aliens in enumerate(laserlist):
        #         laserlist[index] = aliens.move(0,-5)
        #         if 0 > laser.bottom:
        #             laserlist.pop(index)

        if len(gv.aliendict['alien'][1]) == 0:
            break
        
    gv.level+=1
    if(gv.level <= 20):
        for _ in range(gv.level):
            at = threading.Thread(target = talien, args = (gv,alienrect,alock))
            at.daemon = True
            at.start
    super.join()
        

def aliens(gv):
    aliendict = gv.aliendict
    alien = pygame.image.load("images/alien.png")
    alienrect = alien.get_rect()
    alienlist = []
    laser = pygame.image.load("images/laser.png")
    laserlist = []

    aliendict['alien'] = [alien,alienlist]
    aliendict['laser'] = [laser,laserlist]
    
    #para ir ao level desejado
    alock = threading.Lock()
    for _ in range(gv.level-1):
        at = threading.Thread(target = talien, args = (gv,alienrect,alock))
        at.daemon = True
        at.start
    talien(gv,alienrect,alock)

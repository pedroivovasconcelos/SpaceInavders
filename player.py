import pygame, sys, time   

def player(size, playerdict):
    
    print("iniciado")
    x = 125
    y = 400
    spaceship = pygame.image.load("images/spaceship.png")
    spaceshiprect = spaceship.get_rect()
    spaceshiprect = spaceshiprect.move(x,y)
    playerdict['player'] = [spaceship,spaceshiprect]

    shoot = pygame.image.load("images/shoot.png")
    shootlist = []
    playerdict['shoots'] = [shoot,shootlist]
    charger = 0
    while 1:
        time.sleep(1/30)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if (0 != spaceshiprect.left):
                spaceshiprect = spaceshiprect.move(-5,0)
        if key[pygame.K_RIGHT]:
            if (size[0] != spaceshiprect.right):
                spaceshiprect = spaceshiprect.move(5,0)
        if key[pygame.K_SPACE]:
            if charger == 0:
                shootrect = shoot.get_rect()
                shootrect = shootrect.move(spaceshiprect.left+15,spaceshiprect.top-15)
                shootlist.append(shootrect)
                charger = 400
        if charger > 0:
                charger-=1

        if len(shootlist) != 0:
            for index, shoots in enumerate(shootlist):
                shootlist[index] = shoots.move(0,-5)
                if 0 > shoots.top:
                    shootlist.pop(index)
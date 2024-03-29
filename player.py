import pygame, sys, time, gamestart, datetime 

def player(gv):
    x = 125
    y = 400
    size = gv.size
    #listas são compostas por retângulos dos respectivos objetos, para destruir um objeto
    #uma lista fixa de produtor consumidor é gerada para destruir os objetos
    #{'player':[spaceship,spaceshiprect],'shoots':[shoot,shootlist]}
    playerdict = gv.playerdict
    spaceship = pygame.image.load("images/spaceship.png")
    spaceshiprect = spaceship.get_rect()
    spaceshiprect = spaceshiprect.move(x,y)

    shoot = pygame.image.load("images/shoot.png")
    shootlist = []
    charger = 0
    while 1:
        time.sleep(gv.fps)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if (0 != spaceshiprect.left):
                spaceshiprect = spaceshiprect.move(-5,0)
        if key[pygame.K_RIGHT]:
            if (gv.size[0] != spaceshiprect.right):
                spaceshiprect = spaceshiprect.move(5,0)
        if key[pygame.K_SPACE]:
            if charger == 0:
                shootrect = shoot.get_rect()
                shootrect = shootrect.move(spaceshiprect.left+15,spaceshiprect.top-15)
                shootlist.append(shootrect)
                charger = 40
        if charger > 0:
                charger-=1

        if len(shootlist) != 0:
            for index, shoots in enumerate(shootlist):
                shootlist[index] = shoots.move(0,-5)
                if 0 > shoots.top:
                    shootlist.pop(index)

        for lt in list(gv.aliendict['laser'][1].items()):
            if spaceshiprect.colliderect(lt[1]):
                gv.creditgame-=1
                gv.aliendict['laser'][1].pop(lt[0])
            if gv.creditgame == 0:
                gv.fim = datetime.now()

        playerdict['player'] = [spaceship,spaceshiprect]
        playerdict['shoots'] = [shoot,shootlist]
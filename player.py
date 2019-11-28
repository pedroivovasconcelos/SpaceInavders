import threading, pygame
pygame.init()    

black = 0, 0, 0
        
def shooting(shoot,shootrect):
    while True:
        if (shootrect.top != 0):
            shootrect = shootrect.move(0,-5)
            print("tiro andando")
        else:
            shootrect = shootrect.move(x+15,y-50)
            print("tiro chegou")
            return
        screen.blit(shoot, shootrect)
        pygame.time.delay(41)

if __name__ == "__main__":
    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    x = 125
    y = 400
    spaceship = pygame.image.load("spaceship.png")
    spaceshiprect = spaceship.get_rect()
    spaceshiprect = spaceshiprect.move(x,y)

    shoot = pygame.image.load("shoot.png")
    shootlist = []
    charger = 0

    while 1:
        pygame.time.delay(41)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if (0 != spaceshiprect.left):
                spaceshiprect = spaceshiprect.move(-5,0)
        if key[pygame.K_RIGHT]:
            if (width != spaceshiprect.right):
                spaceshiprect = spaceshiprect.move(5,0)
        if key[pygame.K_SPACE]:
            print("space")

            if charger == 0:
                shootrect = shoot.get_rect()
                shootrect = shootrect.move(spaceshiprect.left+15,spaceshiprect.top-15)
                shootlist.append(shootrect)
                charger = 40
        if charger > 0:
            charger-=1
        print(charger)

        if len(shootlist) != 0:
            for index, shoots in enumerate(shootlist):
                shootlist[index] = shoots.move(0,-5)
                if 0 > shoots.top:
                    shootlist.pop(index)
                else:
                    screen.blit(shoot, shootlist[index])

        screen.blit(spaceship, spaceshiprect)
        pygame.display.flip()
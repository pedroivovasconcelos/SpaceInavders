import threading, pygame, sys
pygame.init()    

black = 0, 0, 0

if __name__ == "__main__":
    speed = 5
    lives = 3
    #tplayer = threading.Thread(target=player, args=(speed,lives))
    #tplayer.join

    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    spaceship = pygame.image.load("spaceship.png")
    spaceshiprect = spaceship.get_rect()
    x = 125
    y = 400
    spaceshiprect = spaceshiprect.move(x,y)

    while 1:
        pygame.time.delay(41)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            print("up")
            spaceshiprect = spaceshiprect.move(0,-5)
        if key[pygame.K_DOWN]:
            print("down")
            spaceshiprect = spaceshiprect.move(0,5)
        if key[pygame.K_LEFT]:
            print("left")
            spaceshiprect = spaceshiprect.move(-5,0)
        if key[pygame.K_RIGHT]:
            print("right")
            spaceshiprect = spaceshiprect.move(5,0)
        if key[pygame.K_SPACE]:
            print("space")
            pygame.draw.rect(screen,(255,255,0),(250,250,50,50))
        
        screen.blit(spaceship, spaceshiprect)
        #pygame.draw.rect(screen,(255,0,0),(x,y,50,50))
        pygame.display.flip()
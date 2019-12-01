import threading, pygame, sys
pygame.init()    

black = 0, 0, 0

if __name__ == "__main__":
    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    x = 50
    y = 300
    obstacle = pygame.image.load("obstacles.png")
    obstaclerect = obstacle.get_rect()
    obstaclelist = []

    for a in range(4):
        newobstaclerect = obstaclerect.move(20+a*70, obstaclerect.top+y)
        obstaclelist.append(newobstaclerect)
        
    while 1:
        pygame.time.delay(1000)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        for obstacles in obstaclelist:
            screen.blit(obstacle, obstacles)
        pygame.display.flip()
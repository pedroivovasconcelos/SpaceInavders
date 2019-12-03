import pygame, time

x = 40
y = 375
damage = 0
level = 0

def renewobs(gv):
    obstaclelist = []
    obstacle = pygame.image.load("images/obstacles0.png")
    obstaclerect = obstacle.get_rect()
    for a in range(4):
        obstaclelist.append([obstacle,damage,obstaclerect.move(x+a*65, obstaclerect.top+y)])
    gv.obstaclelist = obstaclelist

def obstacles(gv):
    global level
    global damage
        
    while 1:
        if level != gv.level:
            level = gv.level
            damage = 0
            renewobs(gv)
        
        time.sleep(gv.fps)
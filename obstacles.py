import pygame, time

x = 40
y = 375
damage = 0
level = 0

def renewobs(obstaclelist):
    obstacle = pygame.image.load("images/obstacles0.png")
    obstaclerect = obstacle.get_rect()
    for a in range(4):
        print(a)
        obstaclelist.append([obstacle,damage,obstaclerect.move(x+a*65, obstaclerect.top+y)])

def obstacles(gv):
    global level
    renewobs(gv.obstaclelist)
        
    while 1:
        if level != gv.level:
            level = gv.level
            obstaclelist = []
            damage = 0
            
            
        # for a in range(4):
        #     image = "images/obstacles{}.png".format(damage)
        #     obstacle = pygame.image.load(image)
        #     obstaclerect = obstacle.get_rect()
        #     obstaclelist.append([obstacle,damage,obstaclerect.move(x+a*65, obstaclerect.top+y)])
        
        time.sleep(gv.fps)
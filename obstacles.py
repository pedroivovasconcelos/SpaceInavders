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
    index = -1
    while 1:
        if level != gv.level:
            level = gv.level
            damage = 0
            renewobs(gv)

        if 'laser' in gv.aliendict:
            for lt in list(gv.aliendict['laser'][1].items()):
                for obstacles in gv.obstaclelist:
                    if obstacles[2].colliderect(lt[1]):
                        index = gv.obstaclelist.index(obstacles)
                        gv.obstaclelist[index][1]+=1
                        if(gv.obstaclelist[index][1] > 2):
                            gv.obstaclelist[index][0] = None
                        gv.obstaclelist[index][0] = pygame.image.load(f"images/obstacles{gv.obstaclelist[index][1]}.png")
                        gv.aliendict['laser'][1].pop(lt[0])

        time.sleep(gv.fps)
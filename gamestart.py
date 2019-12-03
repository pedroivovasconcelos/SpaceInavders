import threading, sys, pygame, time
#importações das threads do jogo
import supdate, player, alien, obstacles

class gamevariables:
    def __init__(self):
        super().__init__()

    size = width, height = 300, 500
    creditgame = 3
    level = 17
    fps = 1/30
    screen = None
    #listas são compostas por retângulos dos respectivos objetos, para destruir um objeto
    #uma lista fixa de produtor consumidor é gerada para destruir os objetos
    playerdict = dict() #{'player':[spaceship,spaceshiprect],'shoots':[shoot,shootlist]}
    aliendict = dict() #{'aliens':[alien,alienlist],'laser':[laser,laserlist]}

def main():
    if len(sys.argv) == 3:
        creditgame = sys.argv[1]
        if(creditgame <= 0):
            sys.exit()
        level = sys.argv[2]
        if(level <= 0 or level > 20):
            sys.exit()

if __name__ == "__main__":
    pygame.init()
    gv = gamevariables()
    gv.screen = pygame.display.set_mode(gv.size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')
    main()
    s = threading.Thread(target = supdate.screenupdate, args = (gv,))
    s.daemon = True
    p = threading.Thread(target = player.player, args = (gv,))
    p.daemon = True
    a = threading.Thread(target = alien.aliens, args = (gv,))
    a.daemon = True
    s.start()
    p.start()
    a.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        time.sleep(0.01)

    quit()
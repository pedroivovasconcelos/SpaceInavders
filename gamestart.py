import threading, sys, pygame
#importações das threads do jogo
import supdate, player, alien, obstacles

size = width, height = 300, 500
creditgame = 3
level = 1
fps = 1/30
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
    main()
    s = threading.Thread(target = supdate.screenupdate, args = (size, playerdict))
    p = threading.Thread(target = player.player, args = (size, playerdict))
    s.start()
    p.start()
    #a = alien.alien(size,aliendict)
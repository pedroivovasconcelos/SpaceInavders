import pygame, screenupdate, time, threading
#importações das threads do jogo
import screenupdate, player
pygame.init()

if __name__ == "__main__":
    tscreen = threading.start_new_thread()
    tplayer = threading.start_new_thread()
    talien = []
    for _ in range(19):
        talien.append(threading.start_new_thread())
    tscenery = threading.start_new_thread()
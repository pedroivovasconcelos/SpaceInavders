import pygame, screenupdate, time, threading
#importações das threads do jogo
import screenupdate, player
pygame.init()

if __name__ == "__main__":
    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')

    screenupdate(screen)
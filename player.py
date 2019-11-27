import threading, pygame, sys
pygame.init()

def player(speed):
    if lives == 0:
        print('dead')

black = 0, 0, 0

if __name__ == "__main__":
    speed = 5
    lives = 3
    tplayer = threading.Thread(target=player, args=(speed,lives))
    tplayer.join

    size = width, height = 300, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Invaders - 2019 ATR/UFMG')
    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()
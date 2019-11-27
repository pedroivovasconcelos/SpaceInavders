import pygame, thread, screenupdate
pygame.init()

if __name__ == "__main__":
    tscreen = thread.start_new_thread(screenupdate)
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK



def main():
  
    init_pygame()

    screen = get_sreen()

    while True :
        if not handle_events():
            return
        screen.fill(BLACK)
        pygame.display.flip()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def get_sreen():
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def init_pygame():
    numpass, numfail = pygame.init()
    print(f"pygame init : fail count : {numfail}, pass count : {numpass}")

if __name__ == "__main__":
    main()



# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, FRAM_RATE



def main():
  
    init_pygame()

    screen = get_sreen()

    clock = pygame.time.Clock()
    delta_time = 0
    total_time = 0
    frame_count = 0

    while True :

        total_time += delta_time
        
        if not handle_events():
            print(f"FPS : {frame_count/total_time}")
            return
        else:
            frame_count += 1
       
        
        fill_and_flip(screen)
        
        delta_time = clock.tick(FRAM_RATE) / 1000
    

def fill_and_flip(screen):
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



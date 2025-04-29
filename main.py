# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, BLACK, FRAM_RATE
from player import Player

def main():
  
    init_pygame()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    player = Player(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)

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

        updatables.update(delta_time)       
        
        draw_frame(screen, drawables)
        
        delta_time = clock.tick(FRAM_RATE) / 1000
    

def draw_frame(screen, drawables):
    
    screen.fill(BLACK)

    draw_group(screen, drawables)

    pygame.display.flip()

def draw_group(sreen, drawables):
    for drawable in drawables:
        drawable.draw(sreen)

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



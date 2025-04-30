# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, BACKROUND_COLOR , FRAM_RATE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  
    init_pygame()
            
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group() 
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (astroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)     
    
    player = Player(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)

    _ = AsteroidField()

    screen = get_sreen()

    clock = pygame.time.Clock()
    
    delta_time = 0
    total_time = 0
    frame_count = 0

    while True :

        total_time += delta_time

        if not handle_events():
            print_fps(total_time, frame_count)
            return
        else:
            frame_count += 1
        
        updatables.update(delta_time)       

        check_game_over(player, astroids, total_time, frame_count)
        check_hitted_astroids(astroids, shots)
        draw_frame(screen, drawables)

        delta_time = clock.tick(FRAM_RATE) / 1000

def print_fps(total_time, frame_count):
    print(f"FPS : {frame_count/total_time}")
    
  
def check_game_over(player, astroids, total_time, frame_count):
    for astroid in astroids:
        if player.collides_with(astroid):
            print_fps(total_time, frame_count)
            print("Game over!")
            raise SystemExit(0)

def check_hitted_astroids(astroids, shoots):
    for shot in shoots:
        for astroid in astroids:
            if shot.collides_with(astroid):
                shot.kill()
                astroid.split()
 

def draw_frame(screen, drawables):    
    screen.fill(BACKROUND_COLOR)
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



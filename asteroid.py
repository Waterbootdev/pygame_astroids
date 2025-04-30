import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_WIDTH, ASTEROID_COLOR, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)
        
    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()

        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            self.split_random()

    def split_random(self):
            random_angle = random.uniform(20, 50)
            self.create_splitted(random_angle)
            self.create_splitted(-random_angle)

    def create_splitted(self, angle):
         x, y = self.position
         astroid = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
         astroid.velocity = self.velocity.rotate(angle) * 1.2

         

   




        
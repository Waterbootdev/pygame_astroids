import pygame

from circleshape import CircleShape
from constants import ASTEROID_WIDTH, ASTEROID_COLOR

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)
        
    def update(self, delta_time):
        self.position += self.velocity * delta_time
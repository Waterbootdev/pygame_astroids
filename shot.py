import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_COLOR, SHOT_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, SHOT_WIDTH)
        
    def update(self, delta_time):
        self.position += self.velocity * delta_time
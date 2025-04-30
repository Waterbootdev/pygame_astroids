import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_COLOR, PLAYER_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from pygame import Vector2

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = self.direction()
        right = self.direction(rotation= 90, scale= self.radius / 1.5)        
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    
    def direction(self, rotation = 0, scale=1):
        return Vector2(0, 1).rotate(self.rotation + rotation) * scale

    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_WIDTH)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        self.handle_pressed_key(delta_time)
        self.timer -= delta_time

    def handle_pressed_key(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)

        if keys[pygame.K_d]:
            self.rotate(delta_time)

        if keys[pygame.K_w]:
            self.move(delta_time)
   
        if keys[pygame.K_s]:
            self.move(-delta_time)
            
        if keys[pygame.K_SPACE]:
            self.shoot()
   
   
    def move(self, delta_time):
        forward = self.direction()
        self.position += forward * PLAYER_SPEED * delta_time
        
    def shoot(self):
        if self.timer > 0:
            pass
        else:
            x, y = self.position
            shot = Shot(x, y)
            shot.velocity = self.direction(scale=PLAYER_SHOOT_SPEED)
            self.timer += PLAYER_SHOOT_COOLDOWN




        
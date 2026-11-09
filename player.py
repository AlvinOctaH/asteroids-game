from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt: float) -> float:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> float:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer >= 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(self.rotation)
        velocity *= PLAYER_SHOOT_SPEED
        shot.velocity = velocity

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

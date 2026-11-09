from circleshape import CircleShape
from constants import *
import pygame, random
from logger import *


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2

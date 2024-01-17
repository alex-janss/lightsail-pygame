import pygame
from pathlib import Path
from pygame.math import Vector2 as Vec

DRAG = 0.03


def wind_field(pos: Vec):
    magnitude = 0.1
    direction = (1, 1)
    return Vec(direction).normalize() * magnitude


def wrap(pos: Vec, surface: pygame.Surface):
    pos.x %= surface.get_width()
    pos.y %= surface.get_height()


class Sail(pygame.sprite.Sprite):
    def __init__(self, player: 'Player', *groups):
        super().__init__(*groups)
        self.image = pygame.Surface([3, 40])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.player = player

    def update(self, *args, **kwargs):
        self.rect.center = self.player.rect.center


class Player(pygame.sprite.Sprite):
    rotspeed = 1.5

    def __init__(self, position, *groups):
        super().__init__(*groups)
        im_path = Path(__file__) / '../graphics/player/up_0.png'
        self.display_surface = pygame.display.get_surface()
        self._image = pygame.image.load(im_path).convert_alpha()
        self.image = self._image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos = position
        self.acceleration = Vec()
        self.velocity = Vec()
        self.angle = 0.0
        self.sail = Sail(self, *groups)

    def update(self):
        self.acceleration = wind_field(self.rect.center) - self.velocity * DRAG
        self.velocity += self.acceleration
        self.pos += self.velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += self.rotspeed
            self.image = pygame.transform.rotate(self._image, self.angle)
            self.rect = self.image.get_rect()
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotspeed
            self.image = pygame.transform.rotate(self._image, self.angle)
            self.rect = self.image.get_rect()
        if keys[pygame.K_UP]:
            self.sail_vec.rotate_ip(1)
        if keys[pygame.K_DOWN]:
            self.sail_vec.rotate_ip(-1)

        wrap(self.pos, self.display_surface)
        self.rect.center = self.pos

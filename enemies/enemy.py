import pygame
from traitlets import Bool


class Enemy:
    imgs = []
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.animation_count = 0
        self.health = 1
        self.path = []

    def draw(self, win: pygame.Surface) -> None:
        pass

    def collide(self, x: int, y: int) -> Bool:
        return False

    def move(self) -> None:
        pass

    def hit(self) -> Bool:
        self.health -= 1
        if self.health <= 0:
            return True
        return False

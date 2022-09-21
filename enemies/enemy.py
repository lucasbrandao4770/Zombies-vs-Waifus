from turtle import width
import pygame
from traitlets import Bool


class Enemy:
    imgs = []
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

    def draw(self, win: pygame.Surface) -> None:
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, x: int, y: int) -> Bool:
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def move(self) -> None:
        pass

    def hit(self) -> Bool:
        self.health -= 1
        if self.health <= 0:
            return True
        return False

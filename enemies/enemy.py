import pygame
import math


class Enemy:
    imgs = []
    def __init__(self) -> None:
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(16, 226), (173, 227), (274, 278), (534, 274), (602, 228), (627, 149), (671, 67),
                    (732, 50), (793, 73), (831, 142), (862, 251), (943, 277), (1025, 317), (1047, 381),
                    (1024, 456), (959, 499), (768, 500), (667, 552), (401, 555), (164, 547), (93, 475),
                    (76, 393), (16, 343)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0

    def draw(self, win: pygame.Surface) -> None:
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, x: int, y: int) -> bool:
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def move(self, change) -> None:
        x1, y1 = self.path[self.path_pos]
        if self.path_pos >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]

        slope = (y2-y1) / (x2-x1)
        move_y = slope*change + y2

    def hit(self) -> bool:
        self.health -= 1
        if self.health <= 0:
            return True
        return False

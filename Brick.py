import pygame
from Ball import Ball

class Brick():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    LIGHTYELLOW = (255, 204, 0)

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isHidden = False

    def draw(self, surface):z
        if not self.isHidden:
            pygame.draw.rect(surface, Brick.RED, self.rect(), 1)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

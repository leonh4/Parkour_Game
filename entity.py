import pygame


class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.flipped = False

    def move(self, x, y):
        self.x += x
        self.y += y


    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

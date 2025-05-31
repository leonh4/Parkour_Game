import pygame

class Floor:
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.images = images

    def render(self, surface):
        img = self.images[1]
        for i in range(0, 320, 16):
            surface.blit(img, (self.x + i, self.y))
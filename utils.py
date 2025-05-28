import os

import pygame

ASSETS_PATH = "assets/"

def load_image(path):
    image = pygame.image.load(ASSETS_PATH + path).convert()
    image.set_colorkey((0, 0, 0)) # black = transparent
    return image

def load_images(path):
    images = []
    for fname in sorted(os.listdir(ASSETS_PATH + path)):
        images.append(load_image(path + "/" + fname))
    return images

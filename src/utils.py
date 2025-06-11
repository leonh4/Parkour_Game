import os

import pygame

from score import Score

ASSETS_PATH = "assets/"

def load_image(path):
    """
    This function loads an image from a given path and sets black as it's transparent colour.

    Args:
         path (str): The path to the image.

    Returns:
        pygame.Surface: The loaded image.
    """
    image = pygame.image.load(ASSETS_PATH + path).convert()
    image.set_colorkey((0, 0, 0)) # black = transparent
    return image

def load_mirrored_image(path):
    """
    This function loads an image from a given path, flips it horizontally and sets black as it's transparent colour.

    Args:
        path (str): The path to the image.

    Returns:
        pygame.Surface: The loaded image.
    """
    image = pygame.transform.flip(pygame.image.load(ASSETS_PATH + path).convert(), True, False)
    image.set_colorkey((0, 0, 0))  # black = transparent
    return image

def load_images(path):
    """
    This function loads all the images in a directory and returns them as a list.

    Args:
         path (str): The path to the directory.

    Returns:
        list[pygame.Surface]: The loaded images.
    """
    images = []
    for fname in sorted(os.listdir(ASSETS_PATH + path)):
        images.append(load_image(path + "/" + fname))
    return images

def load_mirrored_images(path):
    """
    This function loads all the images in a directory, flips them horizontally and returns them as a list.

    Args:
        path (str): The path to the directory.

    Returns:
        list[pygame.Surface]: The loaded and flipped images.
    """
    images = []
    for fname in sorted(os.listdir(ASSETS_PATH + path)):
        images.append(load_mirrored_image(path + "/" + fname))
    return images

def load_scores():
    """
    This function loads all the scores from the scores.txt file.

    Returns:
         list[Score]: List of Score objects from the scores.txt file.
    """
    scores = []
    with open("assets/scores.txt", "r") as f:
        for line in f:
            if line != "\n":
                tokens = line.split(" | ")
                scores.append(Score(int(tokens[2]), tokens[1]))
    return scores

def append_score(score):
    """
    This function appends a score to the scores.txt file.

    Args:
        score (Score): The score to append.
    """
    with open("assets/scores.txt", "a") as f:
        f.write(str(score) + "\n")


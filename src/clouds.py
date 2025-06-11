import random

from cloud import Cloud


class Clouds:
    def __init__(self, images, count=16):
        """
        This function initializes the Clouds object

        Args:
            images (list): list of images to use
            count (int): number of clouds to create
        """
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud(random.randrange(0,320), random.randrange(0, 180), random.random() * 0.05 + 0.05, random.choice(images)))


    def move(self):
        """
        This function moves all the clouds in the Clouds object.
        """
        for cloud in self.clouds:
            cloud.move()

    def render(self, surface):
        """
        This function renders all the clouds int the Clouds object.

        Args:
            surface (pygame.Surface): The surface to blit all cloud on.
        """
        for cloud in self.clouds:
            cloud.render(surface)
import random

from cloud import Cloud


class Clouds:
    def __init__(self, images, count=16):
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud(random.randrange(0,320), random.randrange(0, 180), random.random() * 0.05 + 0.05, random.choice(images)))


    def move(self):
        for cloud in self.clouds:
            cloud.move()

    def render(self, surface):
        for cloud in self.clouds:
            cloud.render(surface)
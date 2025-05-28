from sys import exit
import utils
import pygame

from clouds import Clouds


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        self.images = {
            "background": utils.load_image("background.png"),
            "clouds": utils.load_images("clouds"),
        }
        self.clouds = Clouds(self.images["clouds"], count=16)

    def run(self):
        while True:
            self.display.blit(self.images["background"], (0, 0))
            self.screen.blit(self.display, (0, 0))

            self.clouds.move()
            self.clouds.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    Game().run()
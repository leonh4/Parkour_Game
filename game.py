from sys import exit
import utils
import pygame

import Tilemap
from clouds import Clouds
from entity import Entity


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        self.images = {
            "background": utils.load_image("background.png"),
            "clouds": utils.load_images("clouds"),
            "player_left": pygame.transform.flip(utils.load_image("entities/player.png"), True, False),
            "player_right": utils.load_image("entities/player.png"),
            "grass_tiles": utils.load_images("tiles/grass")
        }
        self.clouds = Clouds(self.images["clouds"], count=16)
        self.player = Entity(160, 200, self.images["player_right"])

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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move(-1,0)
                self.player.image = self.images["player_left"]
            if keys[pygame.K_RIGHT]:
                self.player.move(1,0)
                self.player.image = self.images["player_right"]

            Tilemap.Floor(0, 216, self.images["grass_tiles"]).render(self.display)

            self.player.render(self.display)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    Game().run()
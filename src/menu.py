import pygame
from button import Button


class Menu:
    def __init__(self, play_button_image, exit_button_image, score_button_image, load_button_image):
        """
        This function initializes the Menu object.

        Args:
            play_button_image (pygame.Surface): the image of the play button.
            exit_button_image (pygame.Surface): the image of the exit button.
            score_button_image (pygame.Surface): the image of the score button.
            load_button_image (pygame.Surface): the image of the load button.
        """
        self.play_button = Button(320 // 2 - play_button_image.get_width() // 2, 240 // 2 - play_button_image.get_height() // 2 - 60,
                                  play_button_image,
                                  play_button_image.get_size(),
                                  "play")

        self.score_button = Button(320 // 2 - score_button_image.get_width() // 2, 240 // 2 - score_button_image.get_height() // 2 - 30,
                                   score_button_image,
                                   score_button_image.get_size(),
                                   "score")

        self.load_button = Button(320// 2 - score_button_image.get_width() // 2, 240 // 2 - score_button_image.get_height() // 2 + 0,
                                  load_button_image,
                                  load_button_image.get_size(),
                                  "load")

        self.exit_button = Button(320 // 2 - exit_button_image.get_width() // 2, 240 // 2 - exit_button_image.get_height() // 2 + 30,
                                  exit_button_image,
                                  exit_button_image.get_size(),
                                  "exit")


    def render(self, surface):
        """
        This function renders all the buttons in the menu.

        Args:
             surface (pygame.Surface): The surface to blit the buttons on.
        """
        self.load_button.render(surface)
        self.score_button.render(surface)
        self.play_button.render(surface)
        self.exit_button.render(surface)



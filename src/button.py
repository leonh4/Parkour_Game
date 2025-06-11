import pygame


class Button:
    def __init__(self, x, y, image, size, name):
        """
        This function initializes the Button object.

        Args:
            x (float): x coordinate of the button.
            y (float): y coordinate of the button.
            image (pygame.Surface): image of the button.
            size (tuple): size of the button.
            name (str): name of the button.
        """
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.name = name

    def get_rect(self):
        """
        This function returns the rectangle of the button.

        Returns:
            pygame.Rect: rect of the button. Used for mouse click detection.
        """
        return pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def render(self, surface):
        """
        This function renders the button.

        Args:
            surface (pygame.Surface): surface to blit the button on.
        """
        surface.blit(self.image, (self.x, self.y))
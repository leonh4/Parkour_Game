import pygame

class Trophy:
    def __init__(self, x, y, image, size):
        """
        This function initializes the Trophy object.

        Args:
             x (float): The x coordinate of the trophy.
             y (float): The y coordinate of the trophy.
             image (pygame.Surface): The image of the trophy.
             size (tuple): The size of the trophy.
        """
        self.x = x
        self.y = y
        self.image = image
        self.size = size

    def get_rect(self):
        """
        This function returns the rect of the trophy.

        Returns:
             pygame.Rect: The rect of the trophy. Used for collision detection
        """
        return pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def render(self, surface, camera_y):
        """
        This function renders the trophy on the given surface.

        Args:
             surface (pygame.Surface): The surface to blit the trophy on.
             camera_y (float): The y coordinate of the camera.
        """
        surface.blit(self.image, (self.x, self.y - camera_y))
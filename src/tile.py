import pygame


class Tile:
    def __init__(self, x, y, name, number,  tile_size=16):
        """
        This function initializes the tile object.

        Args:
            x (float): The x coordinate of the tile
            y (float): The y coordinate of the tile
            name (str): The name of the tile
            number (int): The number of the tile
            tile_size (int): The  size of the tile
        """
        self.x = x
        self.y = y
        self.name = name
        self.number = number
        self.tile_size = tile_size
        self.rect = pygame.Rect(self.x, self.y, self.tile_size, self.tile_size)

    def render(self, surface, image, camera_y):
        """
        This function renders the tile on the given surface.

        Args:
            surface (pygame.Surface): The surface to blit the tile on.
            image (pygame.Surface): The image of the tile.
            camera_y (float): The y coordinate of the camera.
        """
        surface.blit(image, (self.x, self.y - camera_y))

    def __str__(self):
        """
        This function returns a string representation of the tile.

        Returns:
            str: The string representation of the tile.
        """
        return f"{self.x};{self.y};{self.name};{self.number}"





import os

from tile import Tile


class Map:
    def __init__(self, game, tile_size=16 ):
        """
        This function initializes the Map object.

        Args:
             game (Game): Game object. Used for getting the games assets.
             tile_size (int): The size of the tiles.
        """
        self.tile_size = tile_size
        self.tiles = []
        self.game = game


    def render(self, surface, camera_y):
        """
        This function renders all the tiles in the map onto a given surface. The image of the tile is pulled from games assets.

        Args:
            surface (Surface): The surface to blit every tile on.
            camera_y (float): The y coordinate of the camera.
        """
        for tile in self.tiles:
            tile.render(surface, self.game.assets[tile.name][tile.number], camera_y)

    def __repr__(self):
        """
        This function returns a string representation of all tiles in the map.

        Returns:
            str: A string representation of all tiles separated by new line in the map.
        """
        tiles = ""
        for tile in self.tiles:
            tiles += str(tile) + "\n"
        return tiles

    def load_from_dir(self, path):
        """
        This function loads all the tiles located in a directory.

        Every tile is formated as follows:
        x;y;tile_name;tile_number

        Args:
             path (str): The path to the directory.
        """
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), 'r') as file:
                for line in file:
                    if line != "\n":
                        tmp = line.split(";")
                        self.tiles.append(Tile(int(tmp[0]), int(tmp[1]), tmp[2], int(tmp[3])))


import pygame


class Entity:
    def __init__(self, x, y, image, size):
        """
        This function initializes the Entity object.

        Args:
             x (float): The x coordinate of the entity
             y (float): The y coordinate of the entity
             image (pygame.Surface): The image of the entity
             size (tuple): The size of the entity
        """
        self.x = x
        self.y = y
        self.image = image
        self.flipped = False
        self.velocity_y = 0
        self.size = size
        self.standing = False
        self.running = False

    def get_rect(self):
        """
        This function returns the entity's rectangle

        Returns:
             pygame.Rect: Rect of the entity. Used for collision detection.
        """
        return pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def move(self, t_map, x=0, y=0):
        """
        This function moves the entity according to the given coordinates and handles collisions with tiles that the entity can walk on.

        Args:
             t_map (Map): Object containing all tiles that the player can walk on.
             x (float): Movement direction on x-axis
             y (float): Movement direction on y-axis
        """
        self.velocity_y = min(5.0, self.velocity_y + 0.2)

        if not (self.x + x <= 0 or self.x + x >= 320 - self.size[0]):
            self.x += x
        entity_rect = self.get_rect()
        for tile in t_map.tiles:
            if tile.rect.colliderect(entity_rect):
                if x > 0:
                    self.x = tile.rect.left - self.size[0]
                elif x < 0:
                    self.x = tile.rect.right

        self.y += y + self.velocity_y
        if self.y > 448:
            self.y = 224
            self.x = 112
        entity_rect = self.get_rect()
        for tile in t_map.tiles:
            if tile.rect.colliderect(entity_rect):
                if self.velocity_y > 0:
                    self.y = tile.rect.top - self.size[1]
                    self.velocity_y = 0
                    self.standing = True
                elif self.velocity_y < 0:
                    self.y = tile.rect.bottom
                    self.velocity_y = 0

    def check_if_got_hit(self, projectile_rect):
        """
        This function checks if the entity got hit by a projectile.

        Args:
            projectile_rect (pygame.Rect): Rect of the projectile

        Returns:
            bool: True if the entity got hit by a projectile, False otherwise.
        """
        return projectile_rect.colliderect(self.get_rect())

    def die(self):
        """
        This function resets the position of the entity.
        """
        self.x = 128
        self.y = 225

    def render(self, surface, camera_y):
        """
        This function renders the entity on the given surface and uses an optional offset to render a moving entity.

        Args:
            surface (pygame.Surface): The surface to blit the entity on.
            camera_y (float): The y coordinate of the camera position
        """
        offset = [-3, -3] if self.running else [0, 0]
        surface.blit(self.image, (self.x + offset[0], self.y - camera_y + offset[1]))



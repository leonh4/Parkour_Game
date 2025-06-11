import pygame

class Projectile:
    def __init__(self, x, y, image, size, max_x , speed):
        """
        This function initializes the Projectile object.

        Args:
            x (float): x coordinate of the projectile.
            y (float): y coordinate of the projectile.
            image (pygame.Surface): image of the projectile.
            size (tuple): size of the projectile.
            max_x (float): maximum x coordinate that the projectile can have.
            speed (float): speed of the projectile.
        """
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.max_x = max_x + size[0]
        self.right = True
        self.speed = speed

    def get_rect(self):
        """
        This function returns the projectile's rectangle

        Returns:
             pygame.Rect: Rect of the projectile. Used for collision detection
        """
        return pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def move(self):
        """
        This function moves the projectile from the left side to the right side of the screen.
        """
        if self.right:
            self.x += (1 + self.speed)
        else:
            self.x -= (1 + self.speed)
        if self.x > self.max_x:
            self.right = False
        if self.x < self.size[0]:
            self.right = True


    def render(self, surface, camera_y):
        """
        This function renders the projectile on the given surface.

        Args:
            surface (pygame.Surface): The surface to blit the projectile on.
            camera_y (float): The y coordinate of the camera position
        """
        surface.blit(self.image, (self.x, self.y - camera_y))

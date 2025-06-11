class Cloud:
    def __init__(self, x, y, speed, image):
        """
        This function initializes the Cloud object.

        Args:
             x (float): The x coordinate of the cloud
             y (float): The y coordinate of the cloud
             speed (float): The speed of the cloud
             image (pygame.Surface): The image of the cloud
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def move(self):
        """
        This function moves the cloud by changing the x coordinate.
        """
        self.x += self.speed

    def render(self, surface):
        """
        This function renders the cloud on the given surface.

        If the cloud is moved out of the screen the function moves it to the beginning of the screen.

        Args:
            surface (pygame.Surface): The surface to blit the cloud on.
        """
        if self.x + 10 >= surface.get_width():
            self.x = -10 - self.image.get_width()
        surface.blit(self.image, (self.x, self.y))
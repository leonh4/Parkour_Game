class Cloud:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def move(self):
        self.x += self.speed

    def render(self, surface):
        if self.x + 10 >= surface.get_width():
            self.x = -10 - self.image.get_width()
        surface.blit(self.image, (self.x, self.y))
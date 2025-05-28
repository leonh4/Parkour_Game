class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def render(self, surface, entity_image):
        surface.blit(entity_image, (self.x, self.y))

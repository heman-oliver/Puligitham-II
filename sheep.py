import pygame

class Sheep():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def spawn(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.x, self.y, self.rect)
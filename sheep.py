import pygame

class Sheep():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def spawn(self):
        pygame.draw.rect(self.x, self.y, self.rect)
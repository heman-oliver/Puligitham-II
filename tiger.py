import pygame
from color import Color

class Tiger(object):
    def __init__(self,x , y):
        self.x = x
        self.y = y
        self.pos = [x, y]
        self.size = 20
        self.rect_size = 35
        self.color = Color.RED
        self.selected = False
        self.rect = pygame.Rect(self.x, self.y, self.rect_size, self.rect_size)
        self.rect.center = [x, y]

    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.rect_size, self.rect_size)
        self.rect.center = [self.x, self.y]
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def click(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.selected = True

    def get_valid_moves(self, sheep):
        pass
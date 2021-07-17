# IMPORTS
import pygame

# ///////////////////////////////////////////////////////////|
# SHEEP CLASS, ATTRIBUTES: WIDTH, HEIGHT, RECTANGLE COLLISION|
# ///////////////////////////////////////////////////////////|

class Sheep():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # MAKING THE [X, Y] as CENTER OF THE RECTANGLE
        self.rect.centerx = self.x
        self.rect.centery = self.y

    # SPAWNING (OR) DRAWING THE SHEEP
    def spawn(self):
        pygame.draw.rect(self.x, self.y, self.rect)
# IMPORTS
import pygame
from color import Color

# ////////////////////////////////////////////////////////|
# TIGER CLASS, ATTRIBUTES: X, Y, SIZE, RECTANGLE COLLISION|
# ////////////////////////////////////////////////////////|
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

    # DRAWING THE TIGER
    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, self.rect) # DEBUG
        # UPDATING THE RECT AND THE CENTER
        self.rect = pygame.Rect(self.x, self.y, self.rect_size, self.rect_size)
        self.rect.center = [self.x, self.y]
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def get_pos(self):
        return [self.x, self.y]

    # CHECKING FOR COLLISION OF THE MOUSE TO THE TIGER
    def click(self, pos) -> list:
        if self.rect.collidepoint(pos[0], pos[1]):
            self.selected = True
        return [self.x, self.y]

    # CREATE VALIID MOVES FOR TIGER
    def get_valid_moves(self, pos: list) -> list:
        # ---------------------------------------------------
        # POINTS CALCULATION DONE IN THE GRAPHING CALCULATOR|
        # ---------------------------------------------------
        if pos == [100, 900]: # POINT E
            return [[175, 750], [500, 900]]
        elif pos == [500, 900]: # POINT P
            return [[100, 900], [500, 750], [900, 900]]
        elif pos == [900, 900]: # POINT G
            return [[500, 900], [825, 750]]
        elif pos == [100, 750]: # POINT O
            return [[100, 600], [175, 750]]
        elif pos == [175, 750]: # POINT W
            return [[100, 750], [100, 900], [250, 600], [500, 750]]
        elif pos == [500, 750]: # POINT T
            return [[175, 750], [500, 900], [500, 600], [825, 750]]
        elif pos == [825, 750]: # POINT D1
            return [[500, 750], [900, 750], [750, 600], [900, 900]]
        elif pos == [900, 750]: # POINT N
            return [[825, 750], [900, 900], [900, 600]]
        elif pos == [100, 600]: # POINT L
            return [[250, 600], [100, 750]]
        elif pos == [250, 600]: # POINT V
            return [[100, 600], [175, 750], [325, 450], [500, 600]]
        elif pos == [500, 600]: # POINT S
            return [[250, 600], [500, 750], [500, 450], [750, 600]]
        elif pos == [750, 600]: # POINT C1
            return [[500, 600], [825, 750], [675, 450], [900, 600]]
        elif pos == [900, 600]: # POINT M
            return [[750, 600], [900, 750]]
        elif pos == [100, 450]: # POINT I
            return [[100, 300], [325, 450]]
        elif pos == [325, 450]: # POINT U
            return [[100, 450], [250, 600], [400, 300], [500, 450]]
        elif pos == [500, 450]: # POINT R
            return [[325, 450], [500, 600], [500, 300], [675, 450]]
        elif pos == [675, 450]: # POINT B1
            return [[500, 450], [750, 600], [600, 300], [900, 450]]
        elif pos == [900, 450]: # POINT K
            return [[675, 450], [900, 300]]
        elif pos == [100, 300]: # POINT H
            return [[100, 450], [400, 300]]
        elif pos == [400, 300]: # POINT Z
            return [[325, 450], [500, 100], [500, 300], [100, 300]]
        elif pos == [500, 300]: # POINT Q
            return [[400, 300], [500, 450], [600, 300], [500, 100]]
        elif pos == [600, 300]: # POINT A1
            return [[500, 300], [675, 450], [500, 100], [900, 300]]
        elif pos == [900, 300]: # POINT J
            return [[600, 300], [900, 450]]
        elif pos == [500, 100]: # POINT F
            return [[400, 300], [500, 300], [600, 300]]

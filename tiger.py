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

    # CHECKING FOR COLLISION OF THE MOUSE TO THE TIGER
    def click(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.selected = True

    # CREATE VALIID TIGER MOVES FOR TIGER
    def get_valid_moves(self, pos: list) -> list:
        # ---------------------------------------------------
        # POINTS CALCULATION DONE IN THE GRAPHING CALCULATOR|
        # ---------------------------------------------------
        if pos == [100, 100]: # POINT E
            return [[175, 250], [500, 100]]
        elif pos == [500, 100]: # POINT P
            return [[100, 100], [500, 250], [900, 100]]
        elif pos == [900, 100]: # POINT G
            return [[500, 100], [825, 250]]
        elif pos == [100, 250]: # POINT O
            return [[100, 400], [175, 250]]
        elif pos == [175, 250]: # POINT W
            return [[100, 250], [100, 100], [250, 400], [500, 250]]
        elif pos == [500, 250]: # POINT T
            return [[175, 250], [500, 100], [500, 400], [825, 250]]
        elif pos == [825, 250]: # POINT D1
            return [[500, 250], [900, 250], [750, 400], [900, 100]]
        elif pos == [900, 250]: # POINT N
            return [[825, 250], [900, 100], [900, 400]]
        elif pos == [100, 400]: # POINT L
            return [[250, 400], [100, 250]]
        elif pos == [250, 400]: # POINT V
            return [[100, 400], [175, 250], [325, 550], [500, 400]]
        elif pos == [500, 400]: # POINT S
            return [[250, 400], [500, 250], [500, 550], [750, 400]]
        elif pos == [750, 400]: # POINT C1
            return [[500, 400], [825, 250], [675, 550], [900, 400]]
        elif pos == [900, 400]: # POINT M
            return [[750, 400], [900, 250]]
        elif pos == [100, 550]: # POINT I
            return [[100, 700], [325, 550]]
        elif pos == [325, 550]: # POINT U
            return [[100, 550], [250, 400], [400, 700], [500, 550]]
        elif pos == [500, 550]: # POINT R
            return [[325, 550], [500, 400], [500, 700], [675, 550]]
        elif pos == [675, 550]: # POINT B1 
            return [[500, 550], [750, 400], [600, 700], [900, 550]]
        elif pos == [900, 550]: # POINT K
            return [[675, 550], [900, 700]]
        elif pos == [100, 700]: # POINT H
            return [[100, 550], [400, 700]]
        elif pos == [100, 700]: # POINT Z
            return [[325, 550], [500, 900], [500, 700], [100, 700]]
        elif pos == [500, 700]: # POINT Q
            return [[400, 700], [500, 550], [600, 700], [500, 900]]
        elif pos == [600, 700]: # POINT A1
            return [[500, 700], [675, 550], [500, 900], [900, 700]]
        elif pos == [900, 700]: # POINT J
            return [[600, 700], [900, 550]]
        elif pos == [500, 900]: # POINT F
            return [[400, 700], [500, 700], [600, 700]]
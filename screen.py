# IMPORTS
import pygame
from color import Color

# /////////////////////////|
# SCREEN CLASS FOR THE GAME|
# /////////////////////////|

class Screen(object):
    
    # CONTAINS THE ATTRIBUTES: WIDTH, HEIGHT, FONT, CLOCK
    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.line_thickness = 5

        self.clock = pygame.time.Clock()
        self.set_title()

     # FILLS THE BACKGROUND 
    def fill_background(self, color=Color.BLACK):
        self.screen.fill(color)

    # SETTING THE TITLE IN THE SCREEN
    @staticmethod
    def set_title(title="Puligitham"):
        pygame.display.set_caption(title)

    # UPDATES THE SCREEN
    @staticmethod
    def update():
        pygame.display.flip()
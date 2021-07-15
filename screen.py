# IMPORTS
import pygame
from color import Color

class Screen(object):
    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.line_thickness = 5

        self.clock = pygame.time.Clock()
        self.set_title()

    def fill_background(self, color=Color.BLACK):
        self.screen.fill(color)

    @staticmethod
    def set_title(title="Puligitham"):
        pygame.display.set_caption(title)

    @staticmethod
    def update():
        pygame.display.flip()
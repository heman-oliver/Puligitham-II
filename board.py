import pygame
from color import Color

class Board(object):
    def __init__(self):
        self.line_thickness = 5
        self.rect_width = 35
        self.rect_height = 35
        self.rects = []
        self.color = Color.BLACK

        # VALUES FOR VALID MOVES AS WELL AS VISUALISATION OF COLLISION
        self.mid_valid_pos = [[500, 100], [500, 300], [500, 450], [500, 600], [500, 750], [500, 900]]
        self.right_valid_pos = [[600, 300], [675, 450], [750, 600], [825, 750], [900, 900]]
        self.right_rect_pos = [[900, 300], [900, 450], [900, 600], [900, 750]]
        self.left_valid_pos = [[400, 300], [325, 450], [250, 600], [175, 750], [100, 900]]
        self.left_rect_pos = [[100, 750], [100, 600], [100, 450], [100, 300]]
        self.valid_pos = self.mid_valid_pos + self.right_valid_pos + self.left_valid_pos + self.left_rect_pos + self.right_rect_pos

        self.create_rects()

    # CREATING RECT in THAT PLACE TO CHECK FOR COLLISION FOR FUTURE USE
    def create_rects(self):
        self.rects.clear()
        for pos in self.valid_pos:
            rect = pygame.Rect(pos[0], pos[1], self.rect_width, self.rect_height)
            rect.center = (pos[0], pos[1])
            self.rects.append(rect)

    def draw_rects(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, self.color, rect)

    def draw_background(self, screen):
        pygame.draw.line(screen, self.color, (100, 900), (500, 100), self.line_thickness)
        pygame.draw.line(screen, self.color, (900, 900), (500, 100), self.line_thickness)
        pygame.draw.line(screen, self.color, (100, 900), (900, 900), self.line_thickness)
        pygame.draw.line(screen, self.color, (500, 900), (500, 100), self.line_thickness)

    def draw_board_rect(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(100, 300, 800, 150), 5)
        pygame.draw.rect(screen, self.color, pygame.Rect(100, 600, 800, 150), 5)
    
    def reset_valid_pos(self):
        self.valid_pos = self.mid_valid_pos + self.right_valid_pos + self.left_valid_pos + self.left_rect_pos + self.right_rect_pos
    
    def get_empty_moves(self, tiger):
        for rect in self.rects:
            if tiger.rect == rect:
                self.valid_pos.remove([rect.centerx, rect.centery])
                self.create_rects()

    def check_collision(self, pos):
        for rect in self.rects:
            if rect.collidepoint(pos):
                return [rect.centerx, rect.centery]
        return None
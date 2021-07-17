# IMPORTS
import pygame
from board import Board
from tiger import Tiger
from color import Color
from screen import Screen

pygame.init()

# SCREEN, BOARD
win = Screen()
board = Board()

# CREATING THE FIRST FOUR TIGER CLASSES
x1, y1 = 500, 100 # POS OF TIGER-1
tiger_1 = Tiger(x1, y1)
x2, y2 = 500, 300 # POS OF TIGER-2
tiger_2 = Tiger(x2, y2)
x3, y3 = 500, 450 # POS OF TIGER-3
tiger_3 = Tiger(x3, y3)
x4, y4 = 500, 600 # POS OF TIGER-4
tiger_4 = Tiger(x4, y4)

# CHECK FOR CLICKS
def tiger_click(pos):
    tiger_1.click(pos)
    tiger_2.click(pos)
    tiger_3.click(pos)
    tiger_4.click(pos)

# CHECK FOR TIGER SELECTION FROM THE USER
def tiger_move(pos) -> bool:
    # CHECK FOR TIGER CLICKS
    tiger_click(pos)
    # NEW_POS -> CENTER OF THE RECT POS
    new_pos = board.check_collision(pos)
    # CHECK FOR TIGER-1 SELECTION
    if tiger_1.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            clicked_pos = tiger_1.get_pos()
            valid_moves = tiger_1.get_valid_moves(clicked_pos)
            print(clicked_pos)
            print(valid_moves)
            tiger_1.x, tiger_1.y = new_pos[0], new_pos[1]
            tiger_1.draw(win.screen)
            board.reset_valid_pos()
            tiger_1.selected = False
            return True
    # CHECK FOR TIGER-2 SELECTION
    elif tiger_2.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            clicked_pos = tiger_2.get_pos()
            valid_moves = tiger_2.get_valid_moves(clicked_pos)
            print(clicked_pos)
            print(valid_moves)
            tiger_2.x, tiger_2.y = new_pos[0], new_pos[1]
            tiger_2.draw(win.screen)
            board.reset_valid_pos()
            tiger_2.selected = False
            return True
    # CHECK FOR TIGER-3 SELECTION
    elif tiger_3.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            clicked_pos = tiger_3.get_pos()
            valid_moves = tiger_3.get_valid_moves(clicked_pos)
            print(clicked_pos)
            print(valid_moves)
            tiger_3.x, tiger_3.y = new_pos[0], new_pos[1]
            board.reset_valid_pos()
            tiger_3.selected = False
            return True
    # CHECK FOR TIGER-4 SELECTION
    elif tiger_4.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            clicked_pos = tiger_4.get_pos()
            valid_moves = tiger_4.get_valid_moves(clicked_pos)
            print(clicked_pos)
            print(valid_moves)
            tiger_4.x, tiger_4.y = new_pos[0], new_pos[1]
            tiger_4.draw(win.screen)
            board.reset_valid_pos()
            tiger_4.selected = False
            return True

# TURN
sheep_move = True

# DRAWING THE TIGER
def draw_tiger():
    tiger_1.draw(win.screen)
    tiger_2.draw(win.screen)
    tiger_3.draw(win.screen)
    tiger_4.draw(win.screen)

# GETTING THE VALID MOVES FROM THE BOARD CLASS
def get_valid_moves():
    board.get_empty_moves(tiger_1)
    board.get_empty_moves(tiger_2)
    board.get_empty_moves(tiger_3)
    board.get_empty_moves(tiger_4)

run = True
# MAIN LOOP
while run:
    win.fill_background(color=Color.WHITE)
    board.draw_border(win.screen)
    board.draw_board_rect(win.screen)
    get_valid_moves()
    # board.draw_rects(win.screen)  # VISUALISATION OF COLLISION OF RECTS

    # EVENT LOOP
    for event in pygame.event.get():
        # CLOSING THE WINDOW
        if event.type == pygame.QUIT:
            run = False
            break
        # MOUSE BUTTON PRESS
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # pos : TUPLE -> THE CLICKEd POINT OF THE MOUSE
            pos = pygame.mouse.get_pos()
            # THE CENTER OF THE COLLIDED POS -> new_pos
            new_pos = board.check_collision(pos)
            # CHECKING TURN, TURN: SHEEP
            if sheep_move:
                # CHECK IF THE POSITION IS NOT AWAY FROM COLLISION RECT
                if new_pos != None:
                    # ADDING SHEEP CLASS TO THE SHEEP LIST
                    board.add_sheep(new_pos)
                    # CHANGING THE TURN
                    sheep_move = False
            # TURN : TIGER
            else:
                if tiger_move(pos):
                    # CHANGING THE TURN
                    sheep_move = True

    # DRAWING THE TIGER
    draw_tiger()

    # DRAWING THE SHEEP FROM THE SHEEP LIST
    board.draw_sheep(win.screen)
    # UPDATING THE WINDOW (OR) SCREEN
    win.update()

# QUIT THE PYGAME MODULE
pygame.quit()
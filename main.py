import pygame
from board import Board
from tiger import Tiger
from color import Color
from screen import Screen

pygame.init()

win = Screen()
board = Board()

x1, y1 = 500, 100
tiger_1 = Tiger(x1, y1)
x2, y2 = 500, 300
tiger_2 = Tiger(x2, y2)
x3, y3 = 500, 450
tiger_3 = Tiger(x3, y3)
x4, y4 = 500, 600
tiger_4 = Tiger(x4, y4)

run = True

def tiger_move():
    tiger_1.click(pos)
    tiger_2.click(pos)
    tiger_3.click(pos)
    tiger_4.click(pos)
    new_pos = board.check_collision(pos)
    if tiger_1.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            tiger_1.x, tiger_1.y = new_pos[0], new_pos[1]
            tiger_1.draw(win.screen)
            board.reset_valid_pos()
            tiger_1.selected = False
            return True
    elif tiger_2.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            tiger_2.x, tiger_2.y = new_pos[0], new_pos[1]
            tiger_2.draw(win.screen)
            board.reset_valid_pos()
            tiger_2.selected = False
            return True
    elif tiger_3.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            tiger_3.x, tiger_3.y = new_pos[0], new_pos[1]
            board.reset_valid_pos()
            tiger_3.selected = False
            return True
    elif tiger_4.selected:
        print('CLICKED')
        if new_pos != None:
            print(new_pos)
            tiger_4.x, tiger_4.y = new_pos[0], new_pos[1]
            tiger_4.draw(win.screen)
            board.reset_valid_pos()
            tiger_4.selected = False
            return True

sheep_move = True

while run:
    win.fill_background(color=Color.WHITE)
    board.draw_background(win.screen)
    board.draw_board_rect(win.screen)
    board.get_empty_moves(tiger_1)
    board.get_empty_moves(tiger_2)
    board.get_empty_moves(tiger_3)
    board.get_empty_moves(tiger_4)
    # board.draw_rects(win.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            new_pos = board.check_collision(pos)
            if sheep_move:
                if new_pos != None:
                    board.add_sheep(new_pos)
                    sheep_move = False
            else:
                if tiger_move():
                    sheep_move = True

    tiger_1.draw(win.screen)
    tiger_2.draw(win.screen)
    tiger_3.draw(win.screen)
    tiger_4.draw(win.screen)

    board.draw_sheep(win.screen)

    win.update()

pygame.quit()
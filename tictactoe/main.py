import pygame
import sys
from game import TicTacToe
from ai import get_best_move

# Global game instance for ai.py
game = TicTacToe()

pygame.init()
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
WIN_LINE_COLOR = (253, 242, 98)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI - Unbeatable Minimax')
screen.fill(BG_COLOR)

# Board
board = pygame.Surface((WIDTH, WIDTH))
board.fill(BG_COLOR)

def draw_board():
    # Horizontal lines
    for i in range(1, 3):
        pygame.draw.line(board, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    for i in range(1, 3):
        pygame.draw.line(board, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if game.board[row * 3 + col] == 'X':
                pygame.draw.line(board, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(board, CROSS_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif game.board[row * 3 + col] == 'O':
                pygame.draw.circle(board, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                 int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                pygame.draw.circle(board, BG_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                 int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS * 0.7, CIRCLE_WIDTH)

def draw_win_line():
    # TODO: Implement win line animation if needed
    pass

def restart():
    global game
    game.reset()
    screen.fill(BG_COLOR)
    draw_board()
    pygame.display.update()

draw_board()
pygame.display.update()

font = pygame.font.SysFont('Arial', 50, bold=True)

human_turn = True
running = True
winner = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()
                winner = None
                human_turn = True
                screen.fill(BG_COLOR)
                board.fill(BG_COLOR)
                draw_board()
                pygame.display.flip()
                pygame.time.wait(500)
        if human_turn and event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            position = clicked_row * 3 + clicked_col
            if game.make_move(position, 'X'):
                if game.is_winner('X'):
                    winner = 'X'
                elif game.is_board_full():
                    winner = 'Tie'
                else:
                    human_turn = False
                    pygame.time.delay(1000)

        if not human_turn and not winner:  # AI turn
            move = get_best_move(game.get_board_copy())
            if move is not None:
                game.make_move(move, 'O')
                if game.is_winner('O'):
                    winner = 'O'
                elif game.is_board_full():
                    winner = 'Tie'
                else:
                    human_turn = True
                pygame.time.delay(1000)

    draw_figures()
    screen.blit(board, (0, 0))

    # Status text
    if winner is None and human_turn:
        text = font.render('Your Turn (X)', True, (255, 255, 255))
    elif winner is None and not human_turn:
        text = font.render('AI Thinking...', True, (255, 255, 255))
    elif winner == 'Tie':
        text = font.render('Tie Game!', True, (255, 0, 0))
    elif winner == 'X':
        text = font.render('You Win! (Rare)', True, (255, 0, 0))
    else:
        text = font.render('AI Wins!', True, (255, 0, 0))
    screen.blit(text, (20, 610))

    if winner:
        text2 = font.render('Press R to Restart', True, (255, 255, 255))
        screen.blit(text2, (150, 660))

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


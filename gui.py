import pygame
import sys
from classes.Board import Board


pygame.init()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Chess Game')

font = pygame.font.SysFont('Arial', 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_selection_menu():
    screen.fill(WHITE)
    title = font.render("Choose your color:", True, BLACK)
    screen.blit(title, (300, 200))

    white_button = pygame.Rect(250, 300, 100, 50)
    black_button = pygame.Rect(450, 300, 100, 50)

    pygame.draw.rect(screen, BLACK, white_button)
    pygame.draw.rect(screen, WHITE, black_button)

    screen.blit(font.render('White', True, WHITE), (270, 310))
    screen.blit(font.render('Black', True, BLACK), (470, 310))

    pygame.display.update()

def draw_captured_pieces(white_captures, black_captures):
    screen.fill(WHITE, (600, 0, 200, 600))  # Clear the side panel
    y_offset = 20
    screen.blit(font.render('Captured Pieces:', True, BLACK), (610, 20))

    screen.blit(font.render('White:', True, BLACK), (610, 60))
    for i, piece in enumerate(white_captures):
        screen.blit(font.render(piece, True, BLACK), (610, 90 + i * 30))

    screen.blit(font.render('Black:', True, BLACK), (610, 180))
    for i, piece in enumerate(black_captures):
        screen.blit(font.render(piece, True, BLACK), (610, 210 + i * 30))

def display_endgame(winner):
    screen.fill(WHITE)
    winner_text = f'{winner.capitalize()} wins!'
    play_again_text = 'Play again? (Y/N)'

    screen.blit(font.render(winner_text, True, BLACK), (300, 250))
    screen.blit(font.render(play_again_text, True, BLACK), (300, 300))
    pygame.display.update()

def game_loop():
    running = True
    game_active = False
    player_color = None
    board = None
    white_captures = []
    black_captures = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if 250 < mx < 350 and 300 < my < 350:
                        player_color = 'white'
                        board = Board(600, 600)
                        game_active = True
                    elif 450 < mx < 550 and 300 < my < 350:
                        player_color = 'black'
                        board = Board(600, 600)
                        game_active = True

            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if mx < 600:
                        board.handle_click(mx, my)

            if board:
                if board.is_in_checkmate('black'):
                    display_endgame('white')
                    game_active = False
                elif board.is_in_checkmate('white'):
                    display_endgame('black')
                    game_active = False

            if not game_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_active = True
                    board = Board(600, 600)
                    white_captures = []
                    black_captures = []
                elif event.key == pygame.K_n:
                    running = False

        if game_active and board:
            board.draw(screen)
            draw_captured_pieces(white_captures, black_captures)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    draw_selection_menu()
    game_loop()

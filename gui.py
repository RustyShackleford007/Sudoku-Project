import pygame
import button
import sudoku_generator

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_LENGTH = 600
BACKGROUND_COLOR = (159, 159, 159)
TEXT_COLOR = (48, 48, 48)

pygame.display.set_caption("Sudoku")

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_LENGTH))
screen.fill(BACKGROUND_COLOR)

font = pygame.font.Font(None, 32)
easy_text = font.render("EASY", True, TEXT_COLOR, (147, 226, 146))
med_text = font.render("MEDIUM", True, TEXT_COLOR, (147, 226, 146))
hard_text = font.render("HARD", True, TEXT_COLOR, (147, 226, 146))
font = pygame.font.Font(None, 50)
welcome_text = font.render("SELECT A GAME MODE", True, TEXT_COLOR, BACKGROUND_COLOR)
font = pygame.font.Font(None, 175)
title = font.render("SUDOKU", True, (0, 0, 0), BACKGROUND_COLOR)
font = pygame.font.Font(None, 35)
print(title.get_width())

easy_button = button.Button(100, 450, 80, "easy")
medium_button = button.Button(250, 450, 100, "medium")
hard_button = button.Button(420, 450, 80, "hard")

clock = pygame.time.Clock()
refresh_buttons = True
ok = False
txt = ""

def create_board(level):
    myBoard = sudoku_generator.generate_sudoku(9, level)
    return myBoard


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                txt = txt[:1]
            else:
                txt += event.unicode
        if event.type == pygame.QUIT:
            pygame.quit()

    if refresh_buttons:
        if easy_button.draw(screen):
            board = create_board(30)
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False
        if medium_button.draw(screen):
            board = create_board(40)
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False
        if hard_button.draw(screen):
            board = create_board(50)
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False

    if refresh_buttons:
        screen.blit(easy_text, (110, 460))
        screen.blit(med_text, (256, 460))
        screen.blit(hard_text, (428, 460))
        screen.blit(welcome_text, (102, 300))
        screen.blit(title, (40, 100))
    else:
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.line(screen, (0, 0, 0), (598, 0), (598, 600), 4)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 600), 4)
        pygame.draw.line(screen, (0, 0, 0), (0, 530), (600, 530), 4)
        pygame.draw.line(screen, (0, 0, 0), (0, 597), (600, 597), 4)
        for x in range(601):
            if x % 67 == 0:
                if x % 201 == 0:
                    pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 530), 4)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 530), 2)
        for x in range(531):
            if x % 59 == 0:
                if x % 177 == 0:
                    pygame.draw.line(screen, (0, 0, 0), (0, x), (600, x), 4)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (0, x), (600, x), 2)
        for a in range(9):
            for b in range(9):
                if board[a][b] != 0:
                    font = pygame.font.Font(None, 50)
                    text = font.render(str(board[a][b]), True, (0, 0, 0), BACKGROUND_COLOR)
                    screen.blit(text, ((600 // 18) + (600 // 18) * 2 * a - 5, (530 // 18) + (530 // 18) * 2 * b - 10))
                else:
                    Rect = pygame.Rect
                    square = Rect((600 // 18) + (600 // 18) * 2 * a - 26, (530 // 18) + (530 // 18) * 2 * b - 23,
                                  600 // 9, 530 // 9)
                    # pygame.draw.rect(screen, (255, 0, 0), square)
                    pos = pygame.mouse.get_pos()
                    clicked = False
                    if square.collidepoint(pos) and pygame.mouse.get_pressed()[0] and clicked == False:
                        clicked = True
                        #pygame.draw.rect(screen, (255, 0, 0), square)
                        x_val = (600 // 18) + (600 // 18) * 2 * a - 20
                        while x_val % 67 != 0:
                            x_val -= 1
                        x_val2 = (600 // 18) + (600 // 18) * 2 * a + 45
                        while x_val2 % 67 != 0:
                            x_val2 -= 1
                        y_val1 = (530 // 18) + (530 // 18) * 2 * b - 15
                        while y_val1 % 59 != 0:
                            y_val1 -= 1
                        y_val2 = (530 // 18) + (530 // 18) * 2 * b + 40
                        while y_val2 % 59 != 0:
                            y_val2 -= 1
                        if x_val2 > 590:
                            x_val2 = 598
                        ok = True
                    if ok:
                        pygame.draw.line(screen, (255, 0, 0), (x_val, y_val1), (x_val, y_val2), 4)
                        pygame.draw.line(screen, (255, 0, 0), (x_val, y_val2), (x_val2, y_val2), 4)
                        pygame.draw.line(screen, (255, 0, 0), (x_val, y_val1), (x_val2, y_val1), 4)
                        pygame.draw.line(screen, (255, 0, 0), (x_val2, y_val1), (x_val2, y_val2), 4)
                        rectangle = Rect(x_val, y_val1, x_val2 - x_val, y_val2 - y_val1)
                        #pygame.draw.rect(screen, (0, 0, 0), rectangle)
                        #pygame.draw.rect(screen, (0, 23, 0), rectangle)
                        if len(txt) != 0:
                            txt_surface = font.render(txt, True, (72, 72, 72))
                            screen.blit(txt_surface, (300, 300))
                            if len(txt) != 0:
                                new_a = x_val2
                                board[a][b] = int(txt)
                        txt = ""
    clock.tick(60)




    pygame.display.update()

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

easy_button = button.Button(100, 450, 80, "easy")
medium_button = button.Button(250, 450, 100, "medium")
hard_button = button.Button(420, 450, 80, "hard")
exit = button.Button(200, 400, 200, "exit")
exit2 = button.Button(100, 540, 100, "exit")
restart2 = button.Button(270, 540, 80, "restart")
reset2 = button.Button(420, 540, 80, "reset")

clock = pygame.time.Clock()
refresh_buttons = True
runny = True
ok = False
global newtxt
global txt
txt = ""
newtxt = ""
bool = False
global changed_x
global changed_y
global booly
list = []
copyBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


booly = False
changed_x = 0
changed_y = 0

run = True
while run:
    if not runny:
        screen.fill(BACKGROUND_COLOR)
    runny = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_BACKSPACE:
                #txt = txt[:1]
            if event.key == pygame.K_KP_ENTER:
                board[changed_x][changed_y] = int(newtxt)
                print("WORKED")
                booly = True
            if event.key == pygame.K_BACKSPACE:
                board[changed_x][changed_y] = int(newtxt)
                print("WORKED")
                booly = True
                txt = ""
            else:
                txt += event.unicode
        if event.type == pygame.QUIT:
            pygame.quit()

    if refresh_buttons:
        if easy_button.draw(screen):
            sudoku = sudoku_generator.SudokuGenerator(9, 1)
            sudoku.fill_values()
            board = sudoku.get_board()
            sudoku.remove_cells()
            board = sudoku.get_board()
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False
            for a in range(9):
                for b in range(9):
                    copyBoard[a][b] = board[a][b]
        if medium_button.draw(screen):
            sudoku = sudoku_generator.SudokuGenerator(9, 40)
            sudoku.fill_values()
            board = sudoku.get_board()
            sudoku.remove_cells()
            board = sudoku.get_board()
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False
            for a in range(9):
                for b in range(9):
                    copyBoard[a][b] = board[a][b]
        if hard_button.draw(screen):
            sudoku = sudoku_generator.SudokuGenerator(9, 15)
            sudoku.fill_values()
            board = sudoku.get_board()
            sudoku.remove_cells()
            board = sudoku.get_board()
            screen.fill(BACKGROUND_COLOR)
            refresh_buttons = False
            for a in range(9):
                for b in range(9):
                    copyBoard[a][b] = board[a][b]

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
                    if reset2.draw(screen):
                        for abe in range(9):
                            for luca in range(9):
                                board[abe][luca] = copyBoard[abe][luca]
                    if restart2.draw(screen):
                        run = False
                    if exit2.draw(screen):
                        refresh_buttons = True
                        screen.fill(BACKGROUND_COLOR)
                        runny = False
                    font = pygame.font.Font(None, 30)
                    reset_text = font.render("RESET", True, (0, 0, 0), (147, 226, 146))
                    restart_text = font.render("RESTART", True, (0, 0, 0), (147, 226, 146))
                    exit_text = font.render("EXIT", True, (0, 0, 0), (147, 226, 146))
                    screen.blit(restart_text, (105, 552))
                    screen.blit(exit_text, (290, 552))
                    screen.blit(reset_text, (428, 552))
                else:
                    Rect = pygame.Rect
                    square = Rect((600 // 18) + (600 // 18) * 2 * a - 26, (530 // 18) + (530 // 18) * 2 * b - 23,
                                  600 // 9, 530 // 9)
                    pos = pygame.mouse.get_pos()
                    clicked = False
                    if square.collidepoint(pos) and pygame.mouse.get_pressed()[0] and clicked == False:
                        clicked = True
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
                        if len(txt) != 0:
                            newtxt = txt
                            bool = True
                            x1 = x_val
                            y1 = y_val1
                            changed_x = (x_val2 - 15) // (600 // 9)
                            changed_y = (y_val2 - 15) // (530 // 9)
                        if bool:
                            txt_surface = font.render(newtxt, True, (72, 72, 72))
                            screen.blit(txt_surface, (x1 + 10, y1 + 10))
                        txt = ""
                        if booly:
                            bool = False
                            txt = ""
        won = False
        def checkWin():
            for a in range(9):
                for b in range(9):
                    if board[a][b] != sudoku.solved_board[a][b]:
                        return False
            return True
        def checkIfFull():
            for a in range(9):
                for b in range(9):
                    if board[a][b] == 0:
                        return False
            return True

        win_message = ""
        if checkWin():
            screen.fill(BACKGROUND_COLOR)
            font = pygame.font.Font(None, 150)
            winner = font.render("You Won!", True, (0, 0, 0), BACKGROUND_COLOR)
            screen.blit(winner, (70, 200))

            if exit.draw(screen):
                pass
            font = pygame.font.Font(None, 40)
            exit_text = font.render("EXIT", True, TEXT_COLOR, (147, 226, 146))
            screen.blit(exit_text, (270, 408))
            pos = pygame.mouse.get_pos()
            rectangly = Rect(exit.x, exit.y, exit.width, exit.height)
            if rectangly.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                run = False
        if not checkWin() and checkIfFull():
            screen.fill(BACKGROUND_COLOR)
            font = pygame.font.Font(None, 150)
            winner = font.render("You Lost!", True, (0, 0, 0), BACKGROUND_COLOR)
            screen.blit(winner, (70, 200))
            if exit.draw(screen):
                pass
            font = pygame.font.Font(None, 40)
            exit_text = font.render("RESTART", True, TEXT_COLOR, (147, 226, 146))
            screen.blit(exit_text, (240, 408))
            pos = pygame.mouse.get_pos()
            rectangly = Rect(exit.x, exit.y, exit.width, exit.height)
            if rectangly.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                refresh_buttons = True
                screen.fill(BACKGROUND_COLOR)
    clock.tick(20)




    pygame.display.update()

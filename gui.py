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
print(title.get_width())

easy_button = button.Button(100, 450, 80, "easy")
medium_button = button.Button(250, 450, 100, "medium")
hard_button = button.Button(420, 450, 80, "hard")

refresh_buttons = True
board = None
def create_board(level):
  myBoard = sudoku_generator.generate_sudoku(9, level)
  return myBoard


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  if refresh_buttons:
    if easy_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 30)
      board = create_board(30)
      screen.fill(BACKGROUND_COLOR)
      refresh_buttons = False
    if medium_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 40)
      board = create_board(40)
      screen.fill(BACKGROUND_COLOR)
      refresh_buttons = False
    if hard_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 50)
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


  pygame.display.update()
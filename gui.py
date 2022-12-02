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

easy_button = button.Button(100, 450, 80, "easy")
medium_button = button.Button(250, 450, 100, "medium")
hard_button = button.Button(420, 450, 80, "hard")

refresh_buttons = True

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  if refresh_buttons:
    if easy_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 30)
      print("easy")
      screen.fill(BACKGROUND_COLOR)
      refresh_buttons = False
    if medium_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 40)
      print("medium")
      screen.fill(BACKGROUND_COLOR)
      refresh_buttons = False
    if hard_button.draw(screen):
      board = sudoku_generator.SudokuGenerator(9, 50)
      print("hard")
      screen.fill(BACKGROUND_COLOR)
      refresh_buttons = False

  if refresh_buttons:
    screen.blit(easy_text, (110, 460))
    screen.blit(med_text, (256, 460))
    screen.blit(hard_text, (428, 460))
    screen.blit(welcome_text, (102, 300))
  else:
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, SCREEN_HEIGHT), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 530), (600, 530), 4)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_LENGTH - 1, 0), (SCREEN_LENGTH - 1, SCREEN_HEIGHT), 6)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (SCREEN_LENGTH, 0), 4)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_LENGTH // 3, 0), (SCREEN_LENGTH // 3, 530), 4)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_LENGTH // 3 + SCREEN_LENGTH // 3, 0), (SCREEN_LENGTH // 3 + SCREEN_LENGTH // 3, 530), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 177), (SCREEN_LENGTH, 177), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 353), (SCREEN_LENGTH, 353), 4)

    pygame.draw.line(screen, (0, 0, 0), ((SCREEN_LENGTH // 3) // 3, 0), ((SCREEN_LENGTH // 3) // 3, 530), 2)
    pygame.draw.line(screen, (0, 0, 0), (((SCREEN_LENGTH // 3) // 3) * 2, 0), (((SCREEN_LENGTH // 3) // 3) * 2, 530), 2)
    pygame.draw.line(screen, (0, 0, 0), ((SCREEN_LENGTH // 3) + ((SCREEN_LENGTH // 3) // 3), 0), ((SCREEN_LENGTH // 3) + ((SCREEN_LENGTH // 3) // 3), 530), 2)
    pygame.draw.line(screen, (0, 0, 0), ((SCREEN_LENGTH // 3) + ((SCREEN_LENGTH // 3) // 3) * 2, 0), ((SCREEN_LENGTH // 3) + ((SCREEN_LENGTH // 3) // 3) * 2, 530), 2)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_LENGTH - (SCREEN_LENGTH // 3) // 3, 0), (SCREEN_LENGTH - (SCREEN_LENGTH // 3) // 3, 530), 2)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_LENGTH - ((SCREEN_LENGTH // 3) // 3) * 2, 0), (SCREEN_LENGTH - ((SCREEN_LENGTH // 3) // 3) * 2, 530), 2)

    pygame.draw.line(screen, (0, 0, 0), (0, (SCREEN_LENGTH // 3) // 3 - 1), (SCREEN_LENGTH, (SCREEN_LENGTH // 3) // 3 - 1), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, ((530 // 3) // 3) * 2 + 1), (SCREEN_LENGTH, ((530 // 3) // 3) * 2 + 1), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 236), (SCREEN_LENGTH, 236), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, (530 // 3) + ((530 // 3) // 3) * 2), (SCREEN_LENGTH, (530 // 3) + ((530 // 3) // 3) * 2), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, (530 // 3) + ((530 // 3) // 3) * 4 + 1), (SCREEN_LENGTH, (530 // 3) + ((530 // 3) // 3) * 4 + 1), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 530 - (530 // 3) // 3), (SCREEN_LENGTH, (530 - (530 // 3) // 3)), 2)
  pygame.display.update()
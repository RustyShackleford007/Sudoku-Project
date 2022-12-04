import pygame
pygame.init()

clicked = False

class Button():

    height = 40

    BUTTON_COLOR = (147, 226, 146)

    def __init__(self, x, y, width, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.text = text

    def draw(self, surface):
        global clicked

        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        pygame.draw.rect(surface, self.BUTTON_COLOR, button_rect)

        pygame.draw.line(surface, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(surface, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(surface, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(surface, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        action = False
        pos = pygame.mouse.get_pos()

        if button_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and clicked == False:
            clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        return action

    def click(self, surface):
        global clicked


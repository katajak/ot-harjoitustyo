import pygame
from ui.title_screen import TitleScreen

pygame.init()
pygame.display.set_caption("Pong")

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

PLAYERS = 2
ENDLESS = False

screen = pygame.display.set_mode(DISPLAY_SIZE)
fps = pygame.time.Clock()

titlescreen = TitleScreen(screen, fps, DISPLAY_SIZE, PLAYERS, ENDLESS)

while True:
    if titlescreen.inputs() is True:
        titlescreen.start_game()

    titlescreen.draw_title_screen()

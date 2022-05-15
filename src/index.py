import pygame
import database
from ui.title_screen import TitleScreen

pygame.init()
pygame.display.set_caption("Pong")

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

PLAYERS = 1
ENDLESS = False
DIFFICULTY = "Medium"

screen = pygame.display.set_mode(DISPLAY_SIZE)
fps = pygame.time.Clock()

db_connection = database.create_connection()
database.create_table(db_connection)
database.close_connection(db_connection)

titlescreen = TitleScreen(screen, fps, DISPLAY_SIZE, PLAYERS, ENDLESS, DIFFICULTY)

while True:
    if titlescreen.inputs() is True:
        titlescreen.start_game()

    titlescreen.draw_title_screen()

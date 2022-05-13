import pygame
import database
from sprites.paddle import Paddle
from sprites.ball import Ball
from gameloop import GameLoop
from ui.renderer import Renderer
from eventhandler import EventHandler

pygame.init()
pygame.display.set_caption("Pong")
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

screen = pygame.display.set_mode(DISPLAY_SIZE)

PLAYERS = 2
ENDLESS = False
score = [0, 0]

paddle1_color = [0, 255, 0]
paddle2_color = [0, 0, 255]
ball_color = [255, 255, 255]

PADDLE_HEIGHTS = (80, 80)
PADDLE_SPEEDS = (7, 7)

paddle1 = Paddle(paddle1_color, 8, PADDLE_HEIGHTS[0], DISPLAY_SIZE[1])
paddle1.rect.x = 30
paddle1.rect.y = int(DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[0]/2)

paddle2 = Paddle(paddle2_color, 8, PADDLE_HEIGHTS[1], DISPLAY_SIZE[1])
paddle2.rect.x = DISPLAY_SIZE[0] - 30 - 8
paddle2.rect.y = int(DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[1]/2)

paddles = (paddle1, paddle2)

ball = Ball(ball_color, 8, DISPLAY_SIZE)
ball.rect.x = DISPLAY_SIZE[0]/2 - 4
ball.rect.y = DISPLAY_SIZE[1]/2 - 4

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

fps = pygame.time.Clock()

db_connection = database.create_connection()
database.create_table(db_connection)

renderer = Renderer(screen, all_sprites, fps, score, DISPLAY_SIZE)
eventhandler = EventHandler(paddles, PADDLE_SPEEDS, ball, DISPLAY_SIZE, score, PLAYERS, ENDLESS, db_connection)
gameloop = GameLoop(renderer, eventhandler, ENDLESS)

gameloop.main_loop()

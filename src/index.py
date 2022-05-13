import pygame
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

SINGLEPLAYER = False
ENDLESS = False
rally = 0

paddle1_color = [0, 255, 0]
paddle2_color = [0, 0, 255]
ball_color = [255, 255, 255]

PADDLE1_SPEED = 7
PADDLE2_SPEED = 7

PLAYER1_SCORE = 0
PLAYER2_SCORE = 0
score = [PLAYER1_SCORE, PLAYER2_SCORE]

paddle1 = Paddle(paddle1_color, 8, 80, DISPLAY_SIZE[1])
paddle1.rect.x = 30
paddle1.rect.y = int(DISPLAY_SIZE[1]/2 - 40)

paddle2 = Paddle(paddle2_color, 8, 80, DISPLAY_SIZE[1])
paddle2.rect.x = DISPLAY_SIZE[0] - 30 - 8
paddle2.rect.y = int(DISPLAY_SIZE[1]/2 - 40)

ball = Ball(ball_color, 8, DISPLAY_SIZE)
ball.rect.x = DISPLAY_SIZE[0]/2 + 8
ball.rect.y = DISPLAY_SIZE[1]/2 + 8

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

fps = pygame.time.Clock()

renderer = Renderer(screen, all_sprites, fps, score, DISPLAY_SIZE)
eventhandler = EventHandler(paddle1, paddle2, PADDLE1_SPEED, PADDLE2_SPEED,
                            ball, DISPLAY_SIZE, score, rally)
gameloop = GameLoop(renderer, eventhandler, ENDLESS)

gameloop.main_loop()

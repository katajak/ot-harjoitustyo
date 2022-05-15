import unittest
import pygame
import database
from ui.renderer import Renderer
from sprites.ball import Ball
from sprites.paddle import Paddle
from eventhandler import EventHandler
from gameloop import GameLoop

class TestGameloop(unittest.TestCase):
    def setUp(self):
        DISPLAY_WIDTH = 800
        DISPLAY_HEIGHT = 600
        self.DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

        screen = pygame.display.set_mode(self.DISPLAY_SIZE)

        PLAYERS = 1
        ENDLESS = False
        DIFFICULTY = "Medium"

        self.score = [0, 0]

        paddle1_color = [0, 255, 0]
        paddle2_color = [0, 0, 255]
        ball_color = [255, 255, 255]

        PADDLE_HEIGHTS = (80, 80)
        PADDLE_SPEEDS = (7, 7)

        paddle1 = Paddle(paddle1_color, 8, PADDLE_HEIGHTS[0], self.DISPLAY_SIZE[1])
        paddle1.rect.x = 30
        paddle1.rect.y = int(self.DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[0]/2)

        paddle2 = Paddle(paddle2_color, 8, PADDLE_HEIGHTS[1], self.DISPLAY_SIZE[1])
        paddle2.rect.x = self.DISPLAY_SIZE[0] - 30 - 8
        paddle2.rect.y = int(self.DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[1]/2)

        self.paddles = (paddle1, paddle2)

        self.ball = Ball(ball_color, 8, self.DISPLAY_SIZE)
        self.ball.rect.x = self.DISPLAY_SIZE[0]/2 - 4
        self.ball.rect.y = self.DISPLAY_SIZE[1]/2 - 4

        all_sprites = pygame.sprite.Group()
        all_sprites.add(paddle1)
        all_sprites.add(paddle2)
        all_sprites.add(self.ball)

        fps = pygame.time.Clock()

        conf = (PLAYERS, DIFFICULTY)

        self.renderer = Renderer(screen, all_sprites, fps, self.score, self.DISPLAY_SIZE)
        self.eventhandler = EventHandler(self.paddles, PADDLE_SPEEDS, self.ball, self.DISPLAY_SIZE, self.score, conf)
        self.gameloop = GameLoop(self.renderer, self.eventhandler, self.paddles, self.ball, ENDLESS, conf)

    def test_ai(self):
        self.paddles[1].ai_move(self.ball, 7)
        self.assertEqual(self.paddles[1].rect.y, 260)
        self.ball.rect.y = 100
        self.paddles[1].ai_move(self.ball, 7)
        self.assertEqual(self.paddles[1].rect.y, 253)

    def test_loop(self):
        self.score[0] = 11
        self.assertEqual(self.gameloop.main_loop(), None)
        db_connection = database.create_connection()
        database.delete_latest(db_connection)
        database.close_connection(db_connection)

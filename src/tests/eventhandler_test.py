import unittest
import pygame
from eventhandler import EventHandler
from sprites.paddle import Paddle
from sprites.ball import Ball

class TestEventhandler(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.display_size = (self.display_width, self.display_height)

        self.paddle1_color = [0, 255, 0]
        self.paddle2_color = [0, 0, 255]
        self.ball_color = [255, 255, 255]

        self.paddle1_speed = 7
        self.paddle2_speed = 7

        self.player1_score = 0
        self.player2_score = 0
        self.score = [self.player1_score, self.player2_score]

        self.paddle1 = Paddle(self.paddle1_color, 8, 80, self.display_size[1])
        self.paddle1.rect.x = 30
        self.paddle1.rect.y = int(self.display_size[1]/2 - 40)

        self.paddle2 = Paddle(self.paddle2_color, 8, 80, self.display_size[1])
        self.paddle2.rect.x = self.display_size[0] - 30 - 8
        self.paddle2.rect.y = int(self.display_size[1]/2 - 40)

        self.ball = Ball(self.ball_color, 8, self.display_size)
        self.ball.rect.x = self.display_size[0]/2 + 8
        self.ball.rect.y = self.display_size[1]/2 + 8

        self.eventhandler = EventHandler(self.paddle1, self.paddle2, self.paddle1_speed, self.paddle1_speed,
                                         self.ball, self.display_size, self.score)

    def test_update(self):
        for i in range(30):
            self.eventhandler.update_ball_pos()
        self.assertEqual(self.ball.rect.x, 400+8+3*30)
        self.assertEqual(self.ball.rect.y, 300+8)

import unittest
from sprites.paddle import Paddle
from sprites.ball import Ball

class TestPaddle(unittest.TestCase):
    def setUp(self):
        display_width = 800
        display_height = 600
        
        self.paddle1 = Paddle([255, 255, 255], 8, 80, display_height)
        self.paddle2 = Paddle([255, 255, 255], 8, 80, display_height)
        
        self.paddle1.rect.x = 20
        self.paddle1.rect.y = int(display_height/2 - 40)

        self.paddle2.rect.x = display_width - 30
        self.paddle2.rect.y = int(display_height/2 - 40)

        self.ball = Ball((255, 255, 255), 8, (800, 600))
        self.ball.rect.x = 800/2 - 4
        self.ball.rect.y = 600/2 - 4

    def test_paddle_init_height(self):
        self.assertEqual(self.paddle1.rect.y, self.paddle2.rect.y)

    def test_paddle_movement(self):
        self.paddle1.move_up(10)
        self.paddle2.move_down(20)
        self.paddle2.move_up(30)
        self.assertEqual(self.paddle1.rect.y, self.paddle2.rect.y)

    def test_paddle_movement_ai(self):
        self.paddle1.ai_move(self.ball, 10)
        self.paddle2.ai_move(self.ball, 20)
        self.paddle2.ai_move(self.ball, 30)
        self.assertEqual(self.paddle1.rect.y, self.paddle2.rect.y)

    def test_paddle_cant_go_offscreen(self):
        self.paddle1.move_up(9999)
        self.paddle2.move_down(9999)
        self.assertEqual(self.paddle1.rect.y, 0)
        self.assertEqual(self.paddle2.rect.y, 600-80)
        
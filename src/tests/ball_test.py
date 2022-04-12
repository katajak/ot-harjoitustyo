from turtle import update
import unittest
from sprites.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball([255, 255, 255], 8)
        self.ball.rect.x = 400
        self.ball.rect.y = 300

    def test_ball_pos(self):
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 403)
        self.assertEqual(self.ball.rect.y, 303)
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 409)
        self.assertEqual(self.ball.rect.y, 309)

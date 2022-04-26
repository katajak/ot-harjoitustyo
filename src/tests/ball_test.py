import unittest
from sprites.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball([255, 255, 255], 8, (800, 600))
        self.ball.rect.x = 400
        self.ball.rect.y = 300

    def test_ball_pos(self):
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 403)
        self.assertEqual(self.ball.rect.y, 300)
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 409)
        self.assertEqual(self.ball.rect.y, 300)

    def test_reset_ball_pos(self):
        for i in range(10):
            self.ball.update()
        self.ball.reset_pos(1)
        self.assertEqual(self.ball.rect.x, 408)
        self.assertEqual(self.ball.rect.y, 308)
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 405)
        self.assertEqual(self.ball.rect.y, 308)
        for i in range(10):
            self.ball.update()
        self.ball.reset_pos(2)
        self.assertEqual(self.ball.rect.x, 408)
        self.assertEqual(self.ball.rect.y, 308)
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 411)
        self.assertEqual(self.ball.rect.y, 308)
    
    def test_wall_rebound(self):
        self.ball.rect.x = 400
        self.ball.rect.y = 3
        self.ball.speed_x = 3
        self.ball.speed_y = -3
        self.ball.update()
        self.ball.wall_rebound()
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.rect.x, 400+9)
        self.assertEqual(self.ball.rect.y, 3-3+3+3)

    def test_paddle_rebound(self):
        self.ball.paddle_rebound(1)
        self.assertGreater(self.ball.speed_x, 0)
        self.assertGreater(self.ball.speed_y, 0)
        self.ball.paddle_rebound(2)
        self.assertLess(self.ball.speed_x, 0)
        self.assertLess(self.ball.speed_y, 0)

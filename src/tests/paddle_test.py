import unittest
from sprites.paddle import Paddle

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

    def test_paddle_init_height(self):
        self.assertEqual(self.paddle1.rect.y, self.paddle2.rect.y)

    def test_paddle_movement(self):
        self.paddle1.move_up(10)
        self.paddle2.move_down(20)
        self.paddle2.move_up(30)
        self.assertEqual(self.paddle1.rect.y, self.paddle2.rect.y)
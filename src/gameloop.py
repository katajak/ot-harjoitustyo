from eventhandler import EventHandler
from renderer import Renderer

class GameLoop:
    def main_loop(paddle1, paddle2, paddle1_speed, paddle2_speed, ball,
                  screen, display_width, display_height, all_sprites, fps):
        print("Player 1: W, S")
        print("Player 2: Up Arrow, Down Arrow")
        while True:
            EventHandler.check_inputs(paddle1, paddle2, paddle1_speed, paddle2_speed)
            EventHandler.update_ball_pos(ball)
            EventHandler.wall_rebound(ball, display_width, display_height)
            Renderer.draw_screen(screen, all_sprites, fps)

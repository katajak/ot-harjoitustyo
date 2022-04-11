from eventhandler import EventHandler
from renderer import Renderer

class GameLoop:
    def main_loop(paddle1, paddle2, paddle1_speed, paddle2_speed, screen, all_sprites, fps):
        while True:
            EventHandler.check_inputs(paddle1, paddle2, paddle1_speed, paddle2_speed)
            Renderer.draw_screen(screen, all_sprites, fps)

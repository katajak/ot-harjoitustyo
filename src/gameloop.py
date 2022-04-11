from eventhandler import EventHandler
from renderer import Renderer

class GameLoop:
    def main_loop(paddle1, paddle2, paddle1_speed, paddle2_speed, screen, all_sprites, fps):
        while True:
            EventHandler.gameplay_events(paddle1, paddle2, paddle1_speed, paddle2_speed)
            Renderer.draw_screen(screen, all_sprites, fps)
            print(paddle1.rect.y)
            print(paddle2.rect.y)

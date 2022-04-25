class GameLoop:
    def __init__(self, renderer, eventhandler):
        self.renderer = renderer
        self.eventhandler = eventhandler

    def main_loop(self):
        print("Player 1: W, S")
        print("Player 2: Up Arrow, Down Arrow")
        while True:
            self.eventhandler.check_inputs()
            self.eventhandler.update_ball_pos()
            self.eventhandler.paddle_rebound()
            self.eventhandler.wall_rebound()
            self.renderer.draw_screen()

class GameLoop:
    def __init__(self, renderer, eventhandler, endless):
        self.renderer = renderer
        self.eventhandler = eventhandler
        self.endless = endless

    def main_loop(self):
        print("Player 1: W, S")
        print("Player 2: Up Arrow, Down Arrow")
        print("ESC to quit game")
        while True:
            self.eventhandler.check_inputs()
            self.eventhandler.update_ball_pos()
            self.eventhandler.paddle_rebound()
            self.eventhandler.wall_rebound()
            if self.endless is False:
                self.eventhandler.check_game_clear()
            self.renderer.draw_screen()

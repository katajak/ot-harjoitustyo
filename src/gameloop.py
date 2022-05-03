class GameLoop:
    """Luokka, joka vastaa pelin kulusta.

    Attributes:
        renderer: näytön piirto ja päivitys
        eventhandler: tapahtumakäsittelijä
        endless: onko loputon moodi käytössä
    """

    def __init__(self, renderer, eventhandler, endless):
        """Luokan konstruktori

        Args:
            renderer: näytön piirto ja päivitys
            eventhandler: tapahtumakäsittelijä
            endless: onko loputon moodi käytössä
        """

        self.renderer = renderer
        self.eventhandler = eventhandler
        self.endless = endless

    def main_loop(self):
        """Käy läpi pelin kulun.

        """

        print("Player 1: W, S")
        print("Player 2: Up Arrow, Down Arrow")
        print("ESC to quit game")
        while True:
            if self.eventhandler.quit_game() is True:
                break
            self.eventhandler.check_inputs()
            self.eventhandler.update_ball_pos()
            self.eventhandler.paddle_rebound()
            self.eventhandler.wall_rebound()
            if self.endless is False:
                if self.eventhandler.check_game_clear() is True:
                    break
            self.renderer.draw_screen()

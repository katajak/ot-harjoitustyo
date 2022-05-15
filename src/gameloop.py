class GameLoop:
    """Luokka, joka vastaa pelin kulusta.

    Attributes:
        renderer: näytön piirto ja päivitys
        eventhandler: tapahtumakäsittelijä
        paddles: molemmat mailaobjektit
        ball: pallo-objekti
        endless: onko loputon moodi käytössä
        conf: tuple jossa pelaajamäärä ja vaikeustaso
    """

    def __init__(self, renderer, eventhandler, paddles, ball, endless, conf):
        """Luokan konstruktori

        Args:
            renderer: näytön piirto ja päivitys
            eventhandler: tapahtumakäsittelijä
            paddles: molemmat mailaobjektit
            ball: pallo-objekti
            endless: onko loputon moodi käytössä
            conf: tuple jossa pelaajamäärä ja vaikeustaso
        """

        self.renderer = renderer
        self.eventhandler = eventhandler
        self.paddles = paddles
        self.ball = ball
        self.endless = endless
        self.conf = conf

    def main_loop(self):
        """Käy läpi pelin kulun.

        """

        while True:
            self.eventhandler.quit_game()
            self.eventhandler.check_inputs()

            if self.conf[0] == 1:
                if self.conf[1] == "Easy":
                    self.paddles[1].ai_move(self.ball, 5)
                if self.conf[1] == "Medium":
                    self.paddles[1].ai_move(self.ball, 7)
                if self.conf[1] == "Hard":
                    self.paddles[1].ai_move(self.ball, 9)

            self.eventhandler.update_ball_pos()

            self.eventhandler.paddle_rebound()
            self.eventhandler.wall_rebound()

            if self.endless is False:
                if self.eventhandler.check_game_clear() is True:
                    break

            self.renderer.draw_screen()

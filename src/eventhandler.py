import sys
import pygame
import database

class EventHandler:
    """Luokka, joka vastaa erilaisten tapahtumien käsittelystä.

    Attributes:
        paddles: mailat
        paddle_speeds: mailojen nopeudet tuplessa
        ball: pallo
        display_size: näytön koko (800x600)
        score: pistetilanne listassa
        conf: pelaajamäärä ja vaikeustaso tuplessa
    """

    def __init__(self, paddles, paddle_speeds, ball,
                 display_size, score, conf):
        """Luokan konstruktori

        Args:
            paddles: mailat
            paddle_speeds: mailojen nopeudet tuplessa
            ball: pallo
            display_size: näytön koko (800x600)
            score: pistetilanne listassa
            conf: pelaajamäärä ja vaikeustaso tuplessa
            rally: nykyisen pallorallin pituus
            max_rally: käynnissä olevan pelin korkein rallyn pituus
        """

        self.paddles = paddles
        self.paddle_speeds = paddle_speeds
        self.ball = ball
        self.display_size = display_size
        self.score = score
        self.conf = conf
        self.rally = 0
        self.max_rally = 0

    def quit_game(self):
        """Pelistä poistuminen.

        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def check_inputs(self):
        """Käyttäjän näppäinten painallukset, joilla määrätään minne ja kumpi maila liikkuu.

        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddles[0].move_up(self.paddle_speeds[0])
        if keys[pygame.K_s]:
            self.paddles[0].move_down(self.paddle_speeds[0])

        if self.conf[0] == 2:
            if keys[pygame.K_UP]:
                self.paddles[1].move_up(self.paddle_speeds[1])
            if keys[pygame.K_DOWN]:
                self.paddles[1].move_down(self.paddle_speeds[1])

    def update_ball_pos(self):
        """Päivittää pallon sijainnin joka framella.

        """

        self.ball.update()

    def wall_rebound(self):
        """Pallon kimpoaminen ylä- ja alaseinistä sekä pisteiden lasku ja pallon palautus.

        """

        if self.ball.rect.x <= 0:
            self.score[1] += 1
            if self.rally > self.max_rally:
                self.max_rally = self.rally
            self.ball.reset_pos(2)
            self.rally = 0
        if self.ball.rect.x >= self.display_size[0] - self.ball.size:
            self.score[0] += 1
            if self.rally > self.max_rally:
                self.max_rally = self.rally
            self.ball.reset_pos(1)
            self.rally = 0
        if self.ball.rect.y <= 0:
            self.ball.wall_rebound()
        if self.ball.rect.y >= self.display_size[1] - self.ball.size:
            self.ball.wall_rebound()

    def paddle_rebound(self):
        """Pallon kimpoaminen mailasta. Kasvattaa pallorallia.

        """

        if pygame.sprite.collide_rect(self.paddles[0], self.ball) == 1:
            self.ball.paddle_rebound(1)
            self.rally += 1
        if pygame.sprite.collide_rect(self.paddles[1], self.ball) == 1:
            self.ball.paddle_rebound(2)
            self.rally += 1

    def check_game_clear(self):
        """Tarkistaa onko peli päättynyt.

        Returns:
            True, jos peli on päättynyt.
            False, jos peli ei ole vielä päättynyt.
        """

        if self.score[0] == 11 or self.score[1] == 11:
            if self.score[0] == 11:
                print("\nGame ended. Player 1 won!")
            if self.score[1] == 11:
                if self.conf[0] == 1:
                    print("\nGame ended. Computer won!")
                if self.conf[0] == 2:
                    print("\nGame ended. Player 2 won!")
            print("\nFinal result:")
            print(f"{self.score[0]} - {self.score[1]}")
            print("\nLongest rally this game:")
            print(self.max_rally)
            db_connection = database.create_connection()
            database.insert_data(db_connection, self.conf[0],
                                 self.conf[1], self.score, self.max_rally)
            database.close_connection(db_connection)
            return True
        return False

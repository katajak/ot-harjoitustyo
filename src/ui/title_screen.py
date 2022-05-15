import sys
import pygame
import database
from sprites.paddle import Paddle
from sprites.ball import Ball
from gameloop import GameLoop
from ui.renderer import Renderer
from eventhandler import EventHandler

class TitleScreen:
    """Luokka, joka vastaa aloitusruudusta.

    Attributes:
        screen: pygame näyttö
        fps: pygame kello
        display_size: näytön koko (800x600)
        players: pelaajamäärä
        endless: loputon moodi (True tai False)
        difficulty: vaikeustaso
    """

    def __init__(self, screen, fps, display_size, players, endless, difficulty):
        """Luokan konstruktori

        Args:
            screen: pygame näyttö
            fps: pygame kello
            display_size: näytön koko (800x600)
            players: pelaajamäärä
            endless: loputon moodi (True tai False)
            difficulty: vaikeustaso
        """

        self.screen = screen
        self.fps = fps
        self.display_size = display_size
        self.players = players
        self.endless = endless
        self.difficulty = difficulty

    def inputs(self):
        """Käyttäjän syötteet aloitusruudussa.

        Returns:
            True, jos peli aloitetaan
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_e:
                    self.endless = True
                if event.key == pygame.K_n:
                    self.endless = False
                if event.key == pygame.K_1:
                    self.players = 1
                if event.key == pygame.K_2:
                    self.players = 2
                if event.key == pygame.K_7:
                    self.difficulty = "Easy"
                if event.key == pygame.K_8:
                    self.difficulty = "Medium"
                if event.key == pygame.K_9:
                    self.difficulty = "Hard"

    def draw_title_screen(self):
        """Aloitusruudun piirto.

        """

        titlefont = pygame.font.SysFont("Impact", 128)
        normalfont = pygame.font.SysFont("Helvetica", 24)
        self.screen.fill([0, 0, 0])

        title = titlefont.render("Pong", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.display_size[0]/2, 80))

        if self.endless is True:
            endless = normalfont.render("Endless Mode", True, (255, 255, 255))
        if self.endless is False:
            endless = normalfont.render("Normal Mode", True, (255, 255, 255))
        endless_rect = endless.get_rect(center=(self.display_size[0]/4 - 60, self.display_size[1]/2))

        if self.players == 1:
            players = normalfont.render("One Player", True, (255, 255, 255))
        if self.players == 2:
            players = normalfont.render("Two Players", True, (255, 255, 255))
        players_rect = players.get_rect(center=(self.display_size[0]/4 - 60 + self.display_size[0]/2
                                        + players.get_width(), self.display_size[1]/2))
        if self.difficulty == "Easy":
            difficulty = normalfont.render("Easy", True, (255, 255, 255))
        if self.difficulty == "Medium":
            difficulty = normalfont.render("Medium", True, (255, 255, 255))
        if self.difficulty == "Hard":
            difficulty = normalfont.render("Hard", True, (255, 255, 255))
        difficulty_rect = difficulty.get_rect(center=(self.display_size[0]/4 - 60 + self.display_size[0]/2
                                              + players.get_width(), self.display_size[1]/2 + difficulty.get_height()))

        controls = normalfont.render("Controls:", True, (255, 255, 255))
        controls_rect = controls.get_rect(center=(self.display_size[0]/2, self.display_size[1] - controls.get_height()*5))
        player1 = normalfont.render("Player 1: W, S", True, (255, 255, 255))
        player1_rect = player1.get_rect(center=(self.display_size[0]/2, self.display_size[1] - player1.get_height()*4))
        player2 = normalfont.render("Player 2: Up Arrow, Down Arrow", True, (255, 255, 255))
        player2_rect = player2.get_rect(center=(self.display_size[0]/2, self.display_size[1] - player2.get_height()*3))
        start = normalfont.render("Start Game: Return or Space", True, (255, 255, 255))
        start_rect = start.get_rect(center=(self.display_size[0]/2, self.display_size[1] - start.get_height()*2))
        esc = normalfont.render("Quit Game: ESC", True, (255, 255, 255))
        esc_rect = esc.get_rect(center=(self.display_size[0]/2, self.display_size[1] - esc.get_height()))

        db_connection = database.create_connection()
        last_game = database.last_game(db_connection)
        games_played = database.games_played(db_connection)
        max_rally_all_time = database.max_rally_ever(db_connection)
        last = normalfont.render(f"Last game: {last_game[0]} - {last_game[1]}", True, (255, 255, 255))
        last_rect = last.get_rect(center=(self.display_size[0]/2, self.display_size[0]/2 - last.get_height()*5))
        games = normalfont.render(f"Games played: {games_played}", True, (255, 255, 255))
        games_rect = games.get_rect(center=(self.display_size[0]/2, self.display_size[0]/2 - games.get_height()*2))
        max_rally = normalfont.render(f"Longest rally of all time: {max_rally_all_time}", True, (255, 255, 255))
        max_rally_rect = max_rally.get_rect(center=(self.display_size[0]/2, self.display_size[0]/2 - max_rally.get_height()))
        database.close_connection(db_connection)

        self.screen.blit(title, title_rect)
        self.screen.blit(endless, endless_rect)
        self.screen.blit(players, players_rect)
        if self.players == 1:
            self.screen.blit(difficulty, difficulty_rect)
        self.screen.blit(controls, controls_rect)
        self.screen.blit(player1, player1_rect)
        self.screen.blit(player2, player2_rect)
        self.screen.blit(start, start_rect)
        self.screen.blit(esc, esc_rect)
        self.screen.blit(last, last_rect)
        self.screen.blit(games, games_rect)
        self.screen.blit(max_rally, max_rally_rect)

        pygame.display.flip()

        self.fps.tick(30)

    def start_game(self):
        """Aloittaa pelin.

        """

        DISPLAY_WIDTH = 800
        DISPLAY_HEIGHT = 600
        DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

        screen = pygame.display.set_mode(DISPLAY_SIZE)

        score = [0, 0]

        paddle1_color = [0, 255, 0]
        paddle2_color = [0, 0, 255]
        ball_color = [255, 255, 255]

        PADDLE_HEIGHTS = (80, 80)
        PADDLE_SPEEDS = (7, 7)

        paddle1 = Paddle(paddle1_color, 8, PADDLE_HEIGHTS[0], DISPLAY_SIZE[1])
        paddle1.rect.x = 30
        paddle1.rect.y = int(DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[0]/2)

        paddle2 = Paddle(paddle2_color, 8, PADDLE_HEIGHTS[1], DISPLAY_SIZE[1])
        paddle2.rect.x = DISPLAY_SIZE[0] - 30 - 8
        paddle2.rect.y = int(DISPLAY_SIZE[1]/2 - PADDLE_HEIGHTS[1]/2)

        paddles = (paddle1, paddle2)

        ball = Ball(ball_color, 8, DISPLAY_SIZE)
        ball.rect.x = DISPLAY_SIZE[0]/2 - 4
        ball.rect.y = DISPLAY_SIZE[1]/2 - 4

        all_sprites = pygame.sprite.Group()
        all_sprites.add(paddle1)
        all_sprites.add(paddle2)
        all_sprites.add(ball)

        fps = pygame.time.Clock()

        conf = (self.players, self.difficulty)

        renderer = Renderer(screen, all_sprites, fps, score, DISPLAY_SIZE)
        eventhandler = EventHandler(paddles, PADDLE_SPEEDS, ball, DISPLAY_SIZE, score, conf)
        gameloop = GameLoop(renderer, eventhandler, paddles, ball, self.endless, conf)

        gameloop.main_loop()

import sys
import pygame
import database
from sprites.paddle import Paddle
from sprites.ball import Ball
from gameloop import GameLoop
from ui.renderer import Renderer
from eventhandler import EventHandler

class TitleScreen:
    def __init__(self, screen, fps, display_size, players, endless):
        self.screen = screen
        self.fps = fps
        self.display_size = display_size
        self.players = players
        self.endless = endless

    def inputs(self):
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

    def draw_title_screen(self):
        titlefont = pygame.font.SysFont("Impact", 128)
        normalfont = pygame.font.SysFont("Helvetica", 24)
        self.screen.fill([0, 0, 0])

        title = titlefont.render("Pong", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.display_size[0]/2, 80))

        endless = normalfont.render("Endless Mode", True, (255, 255, 255))
        endless_rect = endless.get_rect(center=(self.display_size[0]/4 - 60, self.display_size[1]/2))

        normal = normalfont.render("Normal Mode", True, (255, 255, 255))
        normal_rect = normal.get_rect(center=(self.display_size[0]/4 - 60, self.display_size[1]/2))

        players = normalfont.render("Two Players", True, (255, 255, 255))
        players_rect = players.get_rect(center=(self.display_size[0]/4 - 60 + self.display_size[0]/2
                                                + players.get_width(), self.display_size[1]/2))

        controls = normalfont.render("Controls:", True, (255, 255, 255))
        controls_rect = controls.get_rect(center=(self.display_size[0]/2, self.display_size[1] - controls.get_height()*5))
        player1 = normalfont.render("Player 1: W, S", True, (255, 255, 255))
        player1_rect = player1.get_rect(center=(self.display_size[0]/2, self.display_size[1] - player1.get_height()*4))
        player2 = normalfont.render("Player 2: Up Arrow, Down Arrow", True, (255, 255, 255))
        player2_rect = player2.get_rect(center=(self.display_size[0]/2, self.display_size[1] - player2.get_height()*3))
        start = normalfont.render("Start Game: Return or Space", True, (255, 255, 255))
        start_rect = start.get_rect(center=(self.display_size[0]/2, self.display_size[1] - start.get_height()*2))
        esc = normalfont.render("ESC: Quit Game", True, (255, 255, 255))
        esc_rect = esc.get_rect(center=(self.display_size[0]/2, self.display_size[1] - esc.get_height()))

        self.screen.blit(title, title_rect)
        if self.endless is True:
            self.screen.blit(endless, endless_rect)
        if self.endless is False:
            self.screen.blit(normal, normal_rect)
        self.screen.blit(players, players_rect)
        self.screen.blit(controls, controls_rect)
        self.screen.blit(player1, player1_rect)
        self.screen.blit(player2, player2_rect)
        self.screen.blit(start, start_rect)
        self.screen.blit(esc, esc_rect)

        pygame.display.flip()

        self.fps.tick(30)

    def start_game(self):
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

        db_connection = database.create_connection()
        database.create_table(db_connection)

        renderer = Renderer(screen, all_sprites, fps, score, DISPLAY_SIZE)
        eventhandler = EventHandler(paddles, PADDLE_SPEEDS, ball, DISPLAY_SIZE,
                                    score, self.players, self.endless)
        gameloop = GameLoop(renderer, eventhandler, self.endless)

        gameloop.main_loop()

import pygame
import database

class EventHandler:
    def __init__(self, paddles, paddle_speeds, ball, display_size, score, players, endless, db_connection):
        self.paddles = paddles
        self.paddle_speeds = paddle_speeds
        self.ball = ball
        self.display_size = display_size
        self.score = score
        self.players = players
        self.endless = endless
        self.db_connection = db_connection
        self.rally = 0
        self.max_rally = 0

    def quit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False

    def check_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddles[0].move_up(self.paddle_speeds[0])
        if keys[pygame.K_s]:
            self.paddles[0].move_down(self.paddle_speeds[0])

        if keys[pygame.K_UP]:
            self.paddles[1].move_up(self.paddle_speeds[1])
        if keys[pygame.K_DOWN]:
            self.paddles[1].move_down(self.paddle_speeds[1])

    def update_ball_pos(self):
        self.ball.update()

    def wall_rebound(self):
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
        if pygame.sprite.collide_rect(self.paddles[0], self.ball) == 1:
            self.ball.paddle_rebound(1)
            self.rally += 1
        if pygame.sprite.collide_rect(self.paddles[1], self.ball) == 1:
            self.ball.paddle_rebound(2)
            self.rally += 1

    def check_game_clear(self):
        if self.score[0] == 11 or self.score[1] == 11:
            if self.score[0] == 11:
                print("\nGame ended. Player 1 won!")
            if self.score[1] == 11:
                print("\nGame ended. Player 2 won!")
            print("\nFinal result:")
            print(f"{self.score[0]} - {self.score[1]}")
            print("\nLongest rally this game:")
            print(self.max_rally)
            database.insert_data(self.db_connection, self.players, self.endless, self.score, self.max_rally)
            return True
        return False

import sys
import pygame

class EventHandler:
    def __init__(self, paddle1, paddle2, paddle1_speed, paddle2_speed,
                 ball, display_size, score):
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.paddle1_speed = paddle1_speed
        self.paddle2_speed = paddle2_speed
        self.ball = ball
        self.display_size = display_size
        self.score = score

    def check_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle1.move_up(self.paddle1_speed)
        if keys[pygame.K_s]:
            self.paddle1.move_down(self.paddle1_speed)

        if keys[pygame.K_UP]:
            self.paddle2.move_up(self.paddle2_speed)
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down(self.paddle2_speed)

    def update_ball_pos(self):
        self.ball.update()

    def wall_rebound(self):
        if self.ball.rect.x <= 0:
            self.score[1] += 1
            print("\nScore is now:")
            print(f"{self.score[0]} - {self.score[1]}")
            self.ball.reset_pos(2)
        if self.ball.rect.x >= self.display_size[0] - self.ball.size:
            self.score[0] += 1
            print("\nScore is now:")
            print(f"{self.score[0]} - {self.score[1]}")
            self.ball.reset_pos(1)
        if self.ball.rect.y <= 0:
            self.ball.wall_rebound(1)
        if self.ball.rect.y >= self.display_size[1] - self.ball.size:
            self.ball.wall_rebound(1)

    def paddle_rebound(self):
        if pygame.sprite.collide_rect(self.paddle1, self.ball) == 1:
            self.ball.paddle_rebound(1)
        if pygame.sprite.collide_rect(self.paddle2, self.ball) == 1:
            self.ball.paddle_rebound(2)

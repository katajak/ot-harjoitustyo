import pygame

class EventHandler:
    def check_inputs(paddle1, paddle2, paddle1_speed, paddle2_speed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up(paddle1_speed)
        if keys[pygame.K_s]:
            paddle1.move_down(paddle1_speed)

        if keys[pygame.K_UP]:
            paddle2.move_up(paddle2_speed)
        if keys[pygame.K_DOWN]:
            paddle2.move_down(paddle2_speed)

    def update_ball_pos(ball):
        ball.update()

    def wall_rebound(ball, display_width, display_height):
        if ball.rect.x <= 0:
            ball.wall_rebound(0)
        if ball.rect.x >= display_width - ball.size:
            ball.wall_rebound(0)
        if ball.rect.y <= 0:
            ball.wall_rebound(1)
        if ball.rect.y >= display_height - ball.size:
            ball.wall_rebound(1)

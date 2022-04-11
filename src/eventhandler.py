import pygame

class EventHandler:
    def gameplay_events(paddle1, paddle2, paddle1_speed, paddle2_speed):
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

import pygame

class Renderer:
    def draw_screen(screen, all_sprites, fps):
        screen.fill([20, 20, 20])
        all_sprites.draw(screen)

        pygame.display.flip()

        fps.tick(60)
        
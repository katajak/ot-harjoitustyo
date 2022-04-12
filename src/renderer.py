import pygame

class Renderer:
    def __init__(self, screen, all_sprites, fps):
        self.screen = screen
        self.all_sprites = all_sprites
        self.fps = fps

    def draw_screen(self):
        self.screen.fill([20, 20, 20])
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

        self.fps.tick(60)
        
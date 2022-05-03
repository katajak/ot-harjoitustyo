import pygame

class Renderer:
    def __init__(self, screen, all_sprites, fps, score, display_size):
        self.screen = screen
        self.all_sprites = all_sprites
        self.fps = fps
        self.score = score
        self.scorefont = pygame.font.SysFont("CourierNew", 48)
        self.display_size = display_size

    def draw_screen(self):
        self.screen.fill([20, 20, 20])

        scoredisplay1 = self.scorefont.render(f"{self.score[0]}", True, (255, 255, 255))
        scoredisplay1_rect = scoredisplay1.get_rect(center=(self.display_size[0]/2 - 100, 30))
        scoredisplay2 = self.scorefont.render(f"{self.score[1]}", True, (255, 255, 255))
        scoredisplay2_rect = scoredisplay1.get_rect(center=(self.display_size[0]/2 + 100, 30))
        self.screen.blit(scoredisplay1, scoredisplay1_rect)
        self.screen.blit(scoredisplay2, scoredisplay2_rect)

        self.all_sprites.draw(self.screen)

        pygame.display.flip()

        self.fps.tick(60)

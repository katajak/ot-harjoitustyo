import pygame

class Renderer:
    """Luokka, joka vastaa näytön piirrosta ja päivityksestä.

    Attributes:
        screen: pygame näyttö
        all_sprites: spritejen ryhmä, jossa kaikki spritet (2 mailaa ja pallo)
        fps: pygame kello
        score: molempien pelaajien pisteet
        display_size: näytön koko (800x600)
    """

    def __init__(self, screen, all_sprites, fps, score, display_size):
        """Luokan konstruktori

        Args:
            screen: pygame näyttö
            all_sprites: spritejen ryhmä, jossa kaikki spritet (2 mailaa ja pallo)
            fps: pygame kello
            score: molempien pelaajien pisteet
            scorefont: fontti pisteiden näyttämistä varten
            display_size: näytön koko (800x600)
        """

        self.screen = screen
        self.all_sprites = all_sprites
        self.fps = fps
        self.score = score
        self.scorefont = pygame.font.SysFont("CourierNew", 48)
        self.display_size = display_size

    def draw_screen(self):
        """Piirtää näytön
        
        """

        self.screen.fill([0, 0, 0])

        scoredisplay1 = self.scorefont.render(f"{self.score[0]}", True, (255, 255, 255))
        scoredisplay1_rect = scoredisplay1.get_rect(center=(self.display_size[0]/2 - 100, 30))
        scoredisplay2 = self.scorefont.render(f"{self.score[1]}", True, (255, 255, 255))
        scoredisplay2_rect = scoredisplay1.get_rect(center=(self.display_size[0]/2 + 100, 30))
        self.screen.blit(scoredisplay1, scoredisplay1_rect)
        self.screen.blit(scoredisplay2, scoredisplay2_rect)

        self.all_sprites.draw(self.screen)

        pygame.display.flip()

        self.fps.tick(60)

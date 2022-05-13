import pygame

class Paddle(pygame.sprite.Sprite):
    """Luokka, jolla määritetään mailat ja liikutetaan niitä.

    Attributes:
        color: mailan väri
        width: mailan leveys
        height: mailan korkeus
        display_height: näytön korkeus
    """

    def __init__(self, color, width, height, display_height):
        """Luokan konstruktori

        Args:
            color: mailan väri
            width: mailan leveys
            height: mailan korkeus
            display_height: näytön korkeus
        """

        super().__init__()

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.height = height
        self.display_height = display_height

    def move_up(self, n_pixels):
        """Siirtää mailaa ylöspäin n pikseliä.

        Args:
            n_pixels: kuinka monta pikseliä mailaa siirretään
        """

        self.rect.y -= n_pixels
        self.rect.y = max(self.rect.y, 0)

    def move_down(self, n_pixels):
        """Siirtää mailaa alaspäin n pikseliä.

        Args:
            n_pixels: kuinka monta pikseliä mailaa siirretään
        """

        self.rect.y += n_pixels
        if self.rect.y >= self.display_height - self.height:
            self.rect.y = self.display_height - self.height
        
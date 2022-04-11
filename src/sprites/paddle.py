import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.height = height

    def move_down(self, px):
        self.rect.y += px
        if self.rect.y > 600 - self.height:
            self.rect.y = 600 - self.height

    def move_up(self, px):
        self.rect.y -= px
        if self.rect.y < 0:
            self.rect.y = 0
        
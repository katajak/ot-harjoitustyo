import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()

        self.size = size
        self.image = pygame.Surface([self.size, self.size])
        pygame.draw.rect(self.image, color, [0, 0, self.size, self.size])
        self.rect = self.image.get_rect()
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def wall_rebound(self, wall):
        if wall == 0:
            self.speed_x = -self.speed_x
        if wall == 1:
            self.speed_y = -self.speed_y

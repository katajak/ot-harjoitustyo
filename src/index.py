import pygame
from sprites.paddle import Paddle

pygame.init()
pygame.display.set_caption("Pong")
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

paddle1_color = [255, 255, 255]
paddle2_color = [255, 255, 255]

paddle1 = Paddle(paddle1_color, 8, 80)
paddle1.rect.x = 20
paddle1.rect.y = int(display_height/2 - 40)
 
paddle2 = Paddle(paddle2_color, 8, 80)
paddle2.rect.x = display_width - 30
paddle2.rect.y = int(display_height/2 - 40)

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move_up(4)
    if keys[pygame.K_s]:
        paddle1.move_down(4)

    if keys[pygame.K_UP]:
        paddle2.move_up(4)
    if keys[pygame.K_DOWN]:
        paddle2.move_down(4)

    screen.fill([20, 20, 20])

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

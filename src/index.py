import pygame
from sprites.paddle import Paddle
from gameloop import GameLoop

pygame.init()
pygame.display.set_caption("Pong")
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

paddle1_color = [255, 255, 255]
paddle2_color = [255, 255, 255]

paddle1_speed = 6
paddle2_speed = 6

paddle1 = Paddle(paddle1_color, 8, 80, display_height)
paddle1.rect.x = 30
paddle1.rect.y = int(display_height/2 - 40)
 
paddle2 = Paddle(paddle2_color, 8, 80, display_height)
paddle2.rect.x = display_width - 30 - 8
paddle2.rect.y = int(display_height/2 - 40)

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)

fps = pygame.time.Clock()

GameLoop.main_loop(paddle1, paddle2, paddle1_speed, paddle2_speed, screen, all_sprites, fps)

import pygame
import sys
pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

WHITE = (255,255,255)
RED = (255,0,0)

ball_x= SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT//2
ball_radius = 30
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(ball_x,ball_y),ball_radius)

    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_x-ball_radius <0 or ball_x +ball_radius >SCREEN_WIDTH:
      ball_speed_x *= -1
    if ball_y-ball_radius <0 or ball_y + ball_radius >SCREEN_HEIGHT:
      ball_speed_y *= -1

    pygame.display.flip()
    clock.tick(60)

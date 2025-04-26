import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Red Ball Control')

clock = pygame.time.Clock()

ball_color = (255, 0, 0)
ball_radius = 25
ball_x, ball_y = width // 2, height // 2
speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x - ball_radius - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + speed <= width:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - ball_radius - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + speed <= height:
        ball_y += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)
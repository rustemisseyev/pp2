import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Shapes")
clock = pygame.time.Clock()

color = (255, 0, 0)
mode = 'square'
start_pos = None

def draw_shape(screen, mode, start, end):
    if mode == 'square':
        side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], side, side)
        pygame.draw.rect(screen, color, rect, 2)
    elif mode == 'right_triangle':
        pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end], 2)
    elif mode == 'equilateral_triangle':
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        point1 = start
        point2 = (start[0] + dx, start[1])
        point3 = (start[0] + dx / 2, start[1] - abs(dx) * (3 ** 0.5) / 2)
        pygame.draw.polygon(screen, color, [point1, point2, point3], 2)
    elif mode == 'rhombus':
        center_x = (start[0] + end[0]) // 2
        center_y = (start[1] + end[1]) // 2
        pygame.draw.polygon(screen, color, [
            (center_x, start[1]),
            (end[0], center_y),
            (center_x, end[1]),
            (start[0], center_y)
        ], 2)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 'square'
            elif event.key == pygame.K_2:
                mode = 'right_triangle'
            elif event.key == pygame.K_3:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_4:
                mode = 'rhombus'

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            draw_shape(screen, mode, start_pos, end_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
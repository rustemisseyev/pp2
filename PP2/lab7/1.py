import pygame
import sys
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Mickey Clock')

background = pygame.Surface((600, 600))
background.fill((255, 255, 255))

mickey_face = pygame.image.load('mickeyclock.jpeg')
right_hand = pygame.image.load('right_hand.png')
left_hand = pygame.image.load('left_hand.png')

clock = pygame.time.Clock()

center = (300, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    minute_angle = -(now.minute * 6)
    second_angle = -(now.second * 6)

    screen.blit(background, (0, 0))
    screen.blit(mickey_face, (0, 0))

    right_rotated = pygame.transform.rotate(right_hand, minute_angle)
    left_rotated = pygame.transform.rotate(left_hand, second_angle)

    r_rect = right_rotated.get_rect(center=center)
    l_rect = left_rotated.get_rect(center=center)

    screen.blit(right_rotated, r_rect.topleft)
    screen.blit(left_rotated, l_rect.topleft)

    pygame.display.update()
    clock.tick(60)
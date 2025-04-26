import pygame
import random
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake with Timed Food")
clock = pygame.time.Clock()

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food variables
food_pos = [random.randrange(1, (width // 10)) * 10,
            random.randrange(1, (height // 10)) * 10]
food_spawn_time = time.time()
food_weight = random.choice([1, 2, 3])
food_timer = 5  # seconds

score = 0

# Colors
colors = {
    1: (0, 255, 0),
    2: (255, 165, 0),
    3: (255, 0, 0)
}

def generate_food():
    global food_pos, food_weight, food_spawn_time
    food_pos = [random.randrange(1, (width // 10)) * 10,
                random.randrange(1, (height // 10)) * 10]
    food_weight = random.choice([1, 2, 3])
    food_spawn_time = time.time()

def show_score():
    font = pygame.font.SysFont('times new roman', 24)
    score_surface = font.render(f'Score : {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        change_to = 'UP'
    if keys[pygame.K_DOWN] and direction != 'UP':
        change_to = 'DOWN'
    if keys[pygame.K_LEFT] and direction != 'RIGHT':
        change_to = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != 'LEFT':
        change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake growing mechanism
    snake_body.append(list(snake_pos))
    if snake_pos == food_pos:
        score += food_weight
        generate_food()
    else:
        snake_body.pop(0)

    # Food disappearing after timer
    if time.time() - food_spawn_time > food_timer:
        generate_food()

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, colors[food_weight], pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Check for collisions
    if (snake_pos[0] < 0 or snake_pos[0] >= width or
        snake_pos[1] < 0 or snake_pos[1] >= height or
        snake_pos in snake_body[:-1]):
        running = False

    show_score()
    pygame.display.update()
    clock.tick(15)

pygame.quit()
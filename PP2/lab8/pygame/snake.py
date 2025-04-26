import pygame
import random

# Initialize pygame
pygame.init()

# Game variables
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
done = False
score = 0
level = 1
speed = 300  # Initial delay in milliseconds

# Snake head coordinates
coor_head = [100, 100]

# Snake body coordinates
coor_body = [
    [30, 100],
    [40, 100],
    [50, 100],
    [60, 100],
    [70, 100],
    [80, 100],
    [90, 100],
    [100, 100]
]

# Function to generate new apple not on snake body
def generate_apple():
    while True:
        apple_x = random.randrange(0, width // 10) * 10
        apple_y = random.randrange(0, height // 10) * 10
        if [apple_x, apple_y] not in coor_body:
            return [apple_x, apple_y]

# First apple
coor_apple = generate_apple()
eaten = False

# Direction control
next_dir = "r"  # right
direc = "r"

# Function to display score and level
def score_update(font, size, color):
    global score, level
    score_font = pygame.font.SysFont(font, size)
    score_render = score_font.render(f"Score: {score}  Level: {level}", True, color)
    score_rect = score_render.get_rect()
    screen.blit(score_render, score_rect)

# Function to show Game Over message
def game_over_message(font, size, color):
    global score
    global done
    game_over_font = pygame.font.SysFont(font, size)
    game_over_surface = game_over_font.render("Game Over! Final Score: " + str(score), True, color)
    game_over_rect = pygame.Rect(100, 250, 600, 100)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    done = True

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_dir = "r"
            if event.key == pygame.K_LEFT:
                next_dir = "l"
            if event.key == pygame.K_UP:
                next_dir = "u"
            if event.key == pygame.K_DOWN:
                next_dir = "d"

    # Check self collision
    for seg in coor_body[:-1]:
        if coor_head[0] == seg[0] and coor_head[1] == seg[1]:
            game_over_message("times new roman", 50, (255, 0, 0))

    # Check wall collision (border collision)
    if coor_head[0] < 0 or coor_head[0] >= width or coor_head[1] < 0 or coor_head[1] >= height:
        game_over_message("times new roman", 50, (255, 0, 0))

    screen.fill((0, 0, 0))  # clear screen every frame

    # Update direction
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"

    # Move snake
    if direc == "r":
        coor_head[0] += 10
    if direc == "l":
        coor_head[0] -= 10
    if direc == "u":
        coor_head[1] -= 10
    if direc == "d":
        coor_head[1] += 10

    # Update snake body
    new_coor = [coor_head[0], coor_head[1]]
    coor_body.append(new_coor)
    coor_body.pop(0)

    # Check if apple eaten
    if coor_head[0] == coor_apple[0] and coor_head[1] == coor_apple[1]:
        eaten = True
        score += 10

        # Extend the snake
        coor_body.insert(0, coor_body[0])

        # Generate new apple
        coor_apple = generate_apple()

        # Level up every 30 points
        if score % 30 == 0:
            level += 1
            # Increase speed (decrease delay)
            if speed > 50:
                speed -= 30

    # Draw apple
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(coor_apple[0], coor_apple[1], 10, 10))

    # Draw snake body
    for el in coor_body[:-1]:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))

    # Draw snake head
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(coor_head[0], coor_head[1], 10, 10))

    # Draw score and level
    score_update("times new roman", 20, (128, 128, 128))

    # Control game speed
    pygame.time.delay(speed)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit() 
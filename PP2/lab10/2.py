import pygame
import psycopg2
import random
import time

conn = psycopg2.connect(
    dbname='yourdbname',
    user='yourusername',
    password='yourpassword',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    score INTEGER,
    level INTEGER
)
""")
conn.commit()

username = input("Enter your username: ")

cur.execute("SELECT score, level FROM user_score WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    score, level = user
else:
    score, level = 0, 1
    cur.execute("INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

snake = [[100, 100]]
direction = "RIGHT"
food = [random.randrange(0, width//10)*10, random.randrange(0, height//10)*10]
speed = 10 + level * 2

running = True

def save_progress():
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE username = %s", (score, level, username))
    conn.commit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            if event.key == pygame.K_UP:
                direction = "UP"
            if event.key == pygame.K_DOWN:
                direction = "DOWN"
            if event.key == pygame.K_p:
                save_progress()
                time.sleep(1)

    if direction == "LEFT":
        snake[-1][0] -= 10
    if direction == "RIGHT":
        snake[-1][0] += 10
    if direction == "UP":
        snake[-1][1] -= 10
    if direction == "DOWN":
        snake[-1][1] += 10

    if snake[-1][0] < 0 or snake[-1][0] >= width or snake[-1][1] < 0 or snake[-1][1] >= height:
        save_progress()
        running = False

    if snake[-1] == food:
        snake.append(food.copy())
        score += 10
        if score // 50 > level:
            level += 1
            speed += 2
        food = [random.randrange(0, width//10)*10, random.randrange(0, height//10)*10]

    screen.fill((0,0,0))
    for part in snake:
        pygame.draw.rect(screen, (0,255,0), (*part, 10, 10))
    pygame.draw.rect(screen, (255,0,0), (*food, 10, 10))

    text = font.render(f'Score: {score} Level: {level}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
cur.close()
conn.close()

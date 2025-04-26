import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Music Player')

music_files = ['song1.mp3', 'song2.mp3', 'song3.mp3']
current_track = 0

pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()

clock = pygame.time.Clock()

def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                pygame.mixer.music.unpause()
            if event.key == pygame.K_s:  # Stop
                pygame.mixer.music.pause()
            if event.key == pygame.K_n:  # Next
                current_track = (current_track + 1) % len(music_files)
                play_music()
            if event.key == pygame.K_b:  # Previous (Back)
                current_track = (current_track - 1) % len(music_files)
                play_music()

    screen.fill((30, 30, 30))
    pygame.display.update()
    clock.tick(30)
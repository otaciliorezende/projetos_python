# Faça um Programa em python que abra e reproduza o áudio de arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex16.mp3.mp3')
pygame.mixer,music.play()
pygame.event.wait()
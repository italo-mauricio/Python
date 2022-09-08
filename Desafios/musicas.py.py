#faça um programa que toque mp3 em áudio

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('#arquivo.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()


# Faça um programa em Python que abra o áudio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()
msg = str(input('Digite algo: '))
# Não sei pq isso ta bugado
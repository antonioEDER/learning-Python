# Crie um programa em python que abra e reproduza o áudio de um arquivo mp3

# Importando o PyGame
import pygame
import os

# Inicializando o PyGame
pygame.init()

file = './ferias.mp3'

# Carregando o arquivo MP3 e executando
if os.path.exists(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo {} não está no diretório do script Python'.format(file))
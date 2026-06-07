import pygame
from interface import desenhar_pontuacao, desenhar_vidas

pygame.init()

tela = pygame.display.set_mode((800, 600))

while True:
    tela.fill((0, 0, 0))

    desenhar_pontuacao(tela, 100)
    desenhar_vidas(tela, 3)

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
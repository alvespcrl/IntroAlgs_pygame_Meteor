import pygame
from src.interface import (
    desenhar_pontuacao,
    desenhar_vidas,
    desenhar_recorde
)

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Teste Interface")

rodando = True

while rodando:
    tela.fill((0, 0, 0))

    desenhar_pontuacao(tela, 100)
    desenhar_vidas(tela, 3)
    desenhar_recorde(tela, 250)

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()
import pygame
import sys
from src.jogador import Jogador
from src.tiro import Tiro

pygame.init()
tela = pygame.display.set_mode((800, 600))
relogio = pygame.time.Clock()

jogador = Jogador()
lista_tiros = []

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                novo_tiro = Tiro(jogador.x + 40, jogador.y + 12)
                lista_tiros.append(novo_tiro)


    teclas = pygame.key.get_pressed()
    jogador.movimentar(teclas)

 #controle dos tiros
    for tiro in lista_tiros[:]:
        tiro.atualizar()
        if tiro.rect.x > 800:
            lista_tiros.remove(tiro)

    tela.fill((0, 0, 0))
    jogador.desenhar(tela)
    for tiro in lista_tiros:
        tiro.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)
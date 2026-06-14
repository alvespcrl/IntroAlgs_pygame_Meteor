import pygame

pygame.font.init()

fonte = pygame.font.SysFont(None, 36)

def desenhar_pontuacao(tela, pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, (255,255,255))
    tela.blit(texto, (10,10))

def desenhar_vidas(tela, vidas):
    texto = fonte.render(f"Vidas: {vidas}", True, (255,255,255))
    tela.blit(texto, (10,50))

def desenhar_recorde(tela, recorde):
    texto = fonte.render(f"Recorde: {recorde}", True, (255, 255, 0))
    tela.blit(texto, (10, 90))
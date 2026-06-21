import pygame

pygame.font.init()

fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 72)


# HUD
def desenhar_pontuacao(tela, pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))


def desenhar_vidas(tela, vidas):
    texto = fonte.render(f"Vidas: {vidas}", True, (255, 255, 255))
    tela.blit(texto, (10, 50))


def desenhar_recorde(tela, recorde):
    texto = fonte.render(f"Recorde: {recorde}", True, (255, 255, 0))
    tela.blit(texto, (10, 90))


# Exibir mensagens organizadas
def desenhar_mensagem(tela, mensagem, y, cor=(255, 255, 255)):
    texto = fonte.render(mensagem, True, cor)
    rect = texto.get_rect(center=(400, y))
    tela.blit(texto, rect)


# Tela inicial
def tela_inicial(tela):
    tela.fill((0, 0, 0))

    titulo = fonte_titulo.render("LALA SPACE", True, (255, 255, 255))
    tela.blit(titulo, titulo.get_rect(center=(400, 180)))

    desenhar_mensagem(tela, "Pressione ENTER para iniciar", 300)
    desenhar_mensagem(tela, "Setas para mover", 350)
    desenhar_mensagem(tela, "ESPACO para atirar", 400)

    pygame.display.flip()


# Tela de Game Over
def tela_game_over(tela, pontos, recorde):
    tela.fill((0, 0, 0))

    titulo = fonte_titulo.render("GAME OVER", True, (255, 0, 0))
    tela.blit(titulo, titulo.get_rect(center=(400, 180)))

    desenhar_mensagem(tela, f"Pontos: {pontos}", 300)
    desenhar_mensagem(tela, f"Recorde: {recorde}", 350, (255, 255, 0))
    desenhar_mensagem(tela, "Pressione ESC para sair", 430)

    pygame.display.flip()
import pygame
import sys


def iniciar_jogo():
    pygame.init()

    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Nave Espacial")

    relogio = pygame.time.Clock()
    FPS = 60

    jogando = True

    while jogando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

        tela.fill((0, 0, 0))


        pygame.display.update()

        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_jogo()
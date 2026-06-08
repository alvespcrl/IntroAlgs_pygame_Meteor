import pygame
from src.meteor import (
    criar_meteoro,
    mover_meteoros,
    remover_meteoros
)

from src.interface import (
    desenhar_pontuacao,
    desenhar_vidas
)

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("LALA Space")

    relogio = pygame.time.Clock()
    
    meteoros = []
    pontos = 0
    vidas = 3

    rodando = True

    while rodando:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if len(meteoros) < 5:
            meteoros.append(criar_meteoro())

        mover_meteoros(meteoros)
        remover_meteoros(meteoros, 600)

        tela.fill((0, 0, 0))

        for meteoro in meteoros:
            pygame.draw.circle(
                tela,
                (150, 150, 150),
                (meteoro["x"], meteoro["y"]),
                meteoro["tamanho"] // 2
            )

        desenhar_pontuacao(tela, pontos)
        desenhar_vidas(tela, vidas)

        pygame.display.flip()

    pygame.quit()
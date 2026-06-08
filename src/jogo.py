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

from src.jogador import Jogador
from src.tiro import Tiro

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("LALA Space")

    relogio = pygame.time.Clock()
    
    meteoros = []
    pontos = 0
    vidas = 3
    jogador = Jogador()
    lista_tiros = []

    rodando = True

    while rodando:

        relogio.tick(60)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:

                    novo_tiro = Tiro(
                        jogador.x + jogador.largura,
                        jogador.y + jogador.altura // 2
                    )

                    lista_tiros.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.movimentar(teclas)

        if len(meteoros) < 5:
            meteoros.append(criar_meteoro())

        mover_meteoros(meteoros)
        remover_meteoros(meteoros, 600)

        for tiro in lista_tiros[:]:

            tiro.atualizar()

            if tiro.rect.x > 800:
                lista_tiros.remove(tiro)

        tela.fill((0, 0, 0))

        jogador.desenhar(tela)

        for tiro in lista_tiros:
            tiro.desenhar(tela)

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
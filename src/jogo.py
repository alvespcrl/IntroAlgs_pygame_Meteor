import pygame


from src.meteor import (
    criar_meteoro,
    mover_meteoros,
    remover_meteoros,
    aumentar_dificuldade
)

from src.jogador import Jogador
from src.tiro import Tiro

from src.interface import (
    desenhar_pontuacao,
    desenhar_vidas,
    desenhar_recorde
)

from src.dados import carregar_recorde, salvar_recorde
from src.config import CAMINHO_RECORDE

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("LALA Space")

    relogio = pygame.time.Clock()
    
    meteoros = []
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicio = pygame.time.get_ticks()
    jogador = Jogador()
    lista_tiros = []

    rodando = True
    ultimo_meteoro = pygame.time.get_ticks()
    while rodando:
        relogio.tick(60)

        tempo_atual = pygame.time.get_ticks()
        nivel = (tempo_atual - tempo_inicio) // 10000

        aumentar_dificuldade(meteoros, nivel)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:

                    novo_tiro = Tiro(
                        jogador.x + jogador.largura,
                        jogador.y + jogador.altura // 2 - 2
                    )
                    lista_tiros.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.movimentar(teclas)

        max_meteoros = 5 + nivel

        agora = pygame.time.get_ticks()
        if agora - ultimo_meteoro > 1000:
            if len(meteoros) < max_meteoros:
                meteoros.append(criar_meteoro())

            ultimo_meteoro = agora

        mover_meteoros(meteoros)
        remover_meteoros(meteoros, 600)

        jogador_rect = pygame.Rect(
            jogador.x,
            jogador.y,
            jogador.largura,
            jogador.altura
        )
        for meteoro in meteoros[:]:
            meteoro_rect = pygame.Rect(
                meteoro["x"] - meteoro["tamanho"] //2,
                meteoro["y"] - meteoro["tamanho"] //2,
                meteoro["tamanho"],
                meteoro["tamanho"]
            )

            if jogador_rect.colliderect(meteoro_rect):
                meteoros.remove(meteoro)
                vidas -= 1

                if vidas <=0:
                    rodando = False

        for tiro in lista_tiros[:]:

            tiro.atualizar()

            if tiro.rect.x > 800:
                lista_tiros.remove(tiro)
                continue

            acertou = False

            for meteoro in meteoros[:]:
                meteoro_rect = pygame.Rect(
                    meteoro["x"] - meteoro["tamanho"] //2,
                    meteoro["y"] - meteoro["tamanho"] //2,
                    meteoro["tamanho"],
                    meteoro["tamanho"]
                )

                if tiro.rect.colliderect(meteoro_rect):

                    if meteoro in meteoros:
                        meteoros.remove(meteoro)

                    pontos += 10
                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                    acertou = True
                    break

            if acertou:
                if tiro in lista_tiros:
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
        desenhar_recorde(tela, recorde)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    executar_jogo()

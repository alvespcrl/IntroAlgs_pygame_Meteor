import pygame
import random


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

class FundoEspacial:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        # 🌟 estrelas
        self.estrelas = [
            [random.randint(0, largura), random.randint(0, altura), random.randint(1, 3)]
            for _ in range(140)
        ]

        # 🪐 planetas
        self.planetas = [self.criar_planeta() for _ in range(3)]

        # ☁️ nebulosas (camada lenta)
        self.nebulosas = [self.criar_nebulosa() for _ in range(5)]

        # 👾 naves alien
        self.aliens = []

        self.scroll = 0
        self.timer_alien = 0

        # 🌌 deslocamento da galáxia (parallax)
        self.galaxia_offset = 0

    def criar_planeta(self):
        return {
            "x": random.randint(0, self.largura),
            "y": random.randint(-600, 0),
            "vel": random.uniform(0.3, 1.2),
            "tam": random.randint(40, 120)
        }

    def criar_nebulosa(self):
        surf = pygame.Surface((random.randint(200, 400), random.randint(150, 300)), pygame.SRCALPHA)
        cor = (
            random.randint(80, 160),
            random.randint(0, 120),
            random.randint(120, 255),
            random.randint(30, 80)  # transparência
        )
        pygame.draw.ellipse(surf, cor, surf.get_rect())

        return {
            "surf": surf,
            "x": random.randint(0, self.largura),
            "y": random.randint(-600, self.altura),
            "vel": random.uniform(0.1, 0.4)
        }

    def criar_alien(self):
        return {
            "x": random.choice([-100, self.largura + 100]),
            "y": random.randint(50, self.altura - 200),
            "vel": random.uniform(2, 4),
            "dir": random.choice([-1, 1])
        }

    def atualizar(self):
        self.scroll += 1
        self.galaxia_offset += 0.2  # 🌌 efeito galáxia movimento leve

        # 🌟 estrelas (parallax leve)
        for e in self.estrelas:
            e[1] += 0.3 + e[2] * 0.05
            if e[1] > self.altura:
                e[1] = 0
                e[0] = random.randint(0, self.largura)

        # 🪐 planetas
        for p in self.planetas:
            p["y"] += p["vel"]
            if p["y"] > self.altura + 200:
                p.update(self.criar_planeta())

        # ☁️ nebulosas (movimento lento + galáxia)
        for n in self.nebulosas:
            n["y"] += n["vel"]
            n["x"] += 0.05  # drift galáctico

            if n["y"] > self.altura + 200:
                novo = self.criar_nebulosa()
                n.update(novo)

        # 👾 spawn alien aleatório
        self.timer_alien += 1
        if self.timer_alien > 180:  # ~3 segundos
            self.aliens.append(self.criar_alien())
            self.timer_alien = 0

        # 👾 mover aliens
        for a in self.aliens:
            a["x"] += a["vel"] * a["dir"]

        # remover aliens fora da tela
        self.aliens = [
            a for a in self.aliens
            if -150 < a["x"] < self.largura + 150
        ]

    def desenhar(self, tela):
        # 🌌 fundo galáxia com leve movimento
        tela.fill((5, 5, 20))

        # ☁️ nebulosas
        for n in self.nebulosas:
            tela.blit(n["surf"], (n["x"], n["y"]))

        # 🌟 estrelas (efeito galáxia: deslocamento leve)
        for e in self.estrelas:
            offset_x = e[0] + self.galaxia_offset * (e[2] * 0.2)
            pygame.draw.circle(
                tela,
                (200, 200, 255),
                (int(offset_x) % self.largura, int(e[1])),
                e[2]
            )

        # 🪐 planetas
        for p in self.planetas:
            pygame.draw.circle(
                tela,
                (120, 80, 255),
                (int(p["x"]), int(p["y"])),
                p["tam"]
            )

        # 👾 aliens
        for a in self.aliens:
            pygame.draw.circle(
                tela,
                (255, 80, 255),
                (int(a["x"]), int(a["y"])),
                12
            )
            pygame.draw.circle(
                tela,
                (0, 255, 200),
                (int(a["x"]), int(a["y"])),
                6
            )
    def desenhar(self, tela):
        # fundo base
        tela.fill((5, 5, 20))

        # estrelas
        for e in self.estrelas:
            pygame.draw.circle(
                tela,
                (200, 200, 255),
                (int(e[0]), int(e[1])),
                e[2]
            )

        # planetas (simples, desenhados em círculo)
        for p in self.planetas:
            pygame.draw.circle(
                tela,
                (120, 80, 255),
                (int(p["x"]), int(p["y"])),
                p["tam"]
            )

            pygame.draw.circle(
                tela,
                (80, 200, 255),
                (int(p["x"] + 10), int(p["y"] + 10)),
                p["tam"] // 2,
                2
            )


def escolher_nave(tela):
    fonte = pygame.font.SysFont(None, 50)
    instrucao = fonte.render(
        "Pressione 1, 2 ou 3",
        True,
        (200, 200, 200)
    )

    tela.blit(instrucao, (220, 140))
    

    nave1 = pygame.image.load(
        "assets/imagens/nave/nave1.png"
    ).convert_alpha()

    nave2 = pygame.image.load(
        "assets/imagens/nave/nave2.png"
    ).convert_alpha()

    nave3 = pygame.image.load(
        "assets/imagens/nave/nave3.png"
    ).convert_alpha()

    nave1 = pygame.transform.scale(nave1, (100, 80))
    nave2 = pygame.transform.scale(nave2, (100, 80))
    nave3 = pygame.transform.scale(nave3, (100, 80))

    while True:

        tela.fill((0, 0, 20))

        titulo = fonte.render(
            "ESCOLHA SUA NAVE",
            True,
            (255, 255, 255)
        )

        tela.blit(titulo, (220, 80))
        tela.blit(instrucao, (220, 140))

        tela.blit(nave1, (100, 220))
        tela.blit(nave2, (350, 220))
        tela.blit(nave3, (600, 220))

        pygame.display.flip()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    return "azul"

                if evento.key == pygame.K_2:
                    return "verde"

                if evento.key == pygame.K_3:
                    return "vermelha"

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    fundo = FundoEspacial(800, 600)    
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("LALA Space")

    imagem_meteoro = pygame.image.load(
        "assets/imagens/meteoro.png"
    ).convert_alpha()

    relogio = pygame.time.Clock()
    
    meteoros = []
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicio = pygame.time.get_ticks()
    nave_escolhida = escolher_nave(tela)
    jogador = Jogador(nave_escolhida)
    lista_tiros = []
    explosoes = []

    rodando = True
    ultimo_meteoro = pygame.time.get_ticks()
    while rodando:
        fundo.atualizar()
        relogio.tick(60)
    

        tempo_atual = pygame.time.get_ticks()
        nivel = (tempo_atual - tempo_inicio) // 10000

        aumentar_dificuldade(meteoros, nivel)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:

                    for x, y in jogador.posicoes_tiro():

                        novo_tiro = Tiro(
                            x, 
                            y,
                            jogador.imagem_laser
                        )
                        
                        lista_tiros.append(novo_tiro)

        teclas = pygame.key.get_pressed()
        jogador.movimentar(teclas)

        max_meteoros = min(15, 5 + nivel)

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

            if tiro.rect.x < - 30:
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

                        explosoes.append({
                            "x": meteoro["x"],
                            "y": meteoro["y"],
                            "tempo": 15
                        })

                    pontos += 10
                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                    acertou = True
                    break

            if acertou:
                if tiro in lista_tiros:
                    lista_tiros.remove(tiro)

        fundo.desenhar(tela)

        jogador.desenhar(tela)

        for tiro in lista_tiros:
            tiro.desenhar(tela)

        for meteoro in meteoros:

            tamanho = meteoro["tamanho"]

            sprite = pygame.transform.scale(
               imagem_meteoro,
                (tamanho, tamanho)
            )

            sprite = pygame.transform.rotate(
                sprite,
                meteoro["angulo"]
            )

            tela.blit(
                sprite,
                (
                    meteoro["x"] - tamanho // 2,
                    meteoro["y"] - tamanho // 2
                )
            )

            for explosao in explosoes[:]:

                pygame.draw.circle(
                    tela,
                    (255, explosao["tempo"] * 10, 0),
                    (explosao["x"], explosao["y"]),
                    explosao["tempo"] * 3
                )

                explosao["tempo"] -= 1

                if explosao["tempo"] <= 0:
                    explosoes.remove(explosao)

        desenhar_pontuacao(tela, pontos)
        desenhar_vidas(tela, vidas)
        desenhar_recorde(tela, recorde)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    executar_jogo()

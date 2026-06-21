import pygame
import random
NAVES = {
    "azul": {
        "imagem": "assets/imagens/nave/nave1.png",
        "laser": "assets/imagens/laser/laser_azul.png",
        "tipo_tiro": "duplo",
        "cor_efeito": (0, 150, 255)
    },

    "verde": {
        "imagem": "assets/imagens/nave/nave2.png",
        "laser": "assets/imagens/laser/laser_verde.png",
        "tipo_tiro": "duplo",
        "cor_efeito": (0, 255, 100)
    },

    "vermelha": {
        "imagem": "assets/imagens/nave/nave3.png",
        "laser": "assets/imagens/laser/laser_vermelho.png",
        "tipo_tiro": "central",
        "cor_efeito": (255, 50, 50)
    }
}

class Jogador:
    def __init__(self, tipo_nave="azul"):
        # Posição inicial da nave
        self.x = 100
        self.y = 300
        self.velocidade = 5
        self.largura = 40
        self.altura = 30
        self.vidas = 3
        self.angulo = 0
        self.particulas = []
        self.rastro = []
        dados = NAVES[tipo_nave]

        self.tipo_tiro = dados["tipo_tiro"]
        self.caminho_laser = dados["laser"]
        self.cor_efeito = dados["cor_efeito"]

        self.imagem_laser = pygame.image.load(
            self.caminho_laser
        ).convert_alpha()

        self.imagem = pygame.image.load(
            dados["imagem"]
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (self.largura, self.altura)
        )

    def movimentar(self, teclas):
        self.angulo = 0
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.velocidade

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.velocidade

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
            self.angulo = 10

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
            self.angulo = -10
        
        if self.x < 0: self.x = 0
        if self.x > 800 - self.largura: self.x = 800 - self.largura
        if self.y < 0: self.y = 0
        if self.y > 600 - self.altura: self.y = 600 - self.altura
        
        self.particulas.append({
            "x": self.x + self.largura // 2,
            "y": self.y + self.altura,
            "raio": random.randint(3, 7),
            "vida": 20
            })

    def desenhar(self, tela):
    
        for particula in self.particulas[:]:
            particula["y"] += 2
            particula["vida"] -= 1

            if particula["vida"] <= 0:
                self.particulas.remove(particula)
                continue

            alpha = max(0, int(255 * (particula["vida"] / 20)))

            pygame.draw.circle(
                tela,
                (255, random.randint(120, 200), 50),
                (int(particula["x"]), int(particula["y"])),
                particula["raio"]
            )
        nave_rotacionada = pygame.transform.rotate(
            self.imagem,
            self.angulo
        )
        rect = nave_rotacionada.get_rect(
            center=(
                self.x + self.largura // 2,
                self.y + self.altura // 2
            )
        )
    
        tela.blit(
           nave_rotacionada,
           rect.topleft
        )

    def posicoes_tiro(self):
        
        centro_x = self.x +self.largura // 2
        if self.tipo_tiro == "duplo":
            return [
                (
                    self.x + 6,
                    self.y
                ),

                (
                    self.x + self.largura - 18,
                    self.y
                )
            
            ]

        return [
            (
                centro_x - 6,
                self.y
            )
        ]

    @property
    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
    )
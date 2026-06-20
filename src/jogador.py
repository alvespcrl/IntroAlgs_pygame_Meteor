import pygame

class Jogador:
    def __init__(self):
        # Posição inicial da nave
        self.x = 100
        self.y = 300
        self.velocidade = 5
        self.largura = 40
        self.altura = 30
        self.vidas = 3

        self.imagem = pygame.image.load("imagens/nave/nave1.png")
        self.imagem = pygame.transform.scale(
            self.imagem,
            (self.largura, self.altura)
        )

    def movimentar(self, teclas):
      
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.velocidade
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
        if self.x < 0: self.x = 0
        if self.x > 800 - self.largura: self.x = 800 - self.largura
        if self.y < 0: self.y = 0
        if self.y > 600 - self.altura: self.y = 600 - self.altura

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
    @property
    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
    )
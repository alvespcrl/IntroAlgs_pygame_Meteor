import pygame

class Jogador:
    def __init__(self):
        # Posição inicial da nave
        self.x = 100
        self.y = 300
        self.velocidade = 5
        self.largura = 40
        self.altura = 30

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
      
        ponto1 = (self.x + self.largura, self.y + self.altura // 2)
        ponto2 = (self.x, self.y)
        ponto3 = (self.x, self.y + self.altura)
        pygame.draw.polygon(tela, (0, 255, 0), [ponto1, ponto2, ponto3])
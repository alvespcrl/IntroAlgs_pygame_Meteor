import pygame

class Tiro:
    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 15, 5)
        self.velocidade = 7

    def atualizar(self):
      
        self.rect.x += self.velocidade

    def desenhar(self, tela):

        pygame.draw.rect(tela, (255, 0, 0), self.rect)
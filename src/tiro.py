import pygame

class Tiro:
    def __init__(self, x, y, imagem=None):

        self.rect = pygame.Rect(x, y, 12, 30)
        self.velocidade = 7
        self.imagem = imagem
        if self.imagem:
            self.imagem = pygame.transform.scale(
                self.imagem,
                (12, 30)
            )

    def atualizar(self):
      
        self.rect.y -= self.velocidade

    def desenhar(self, tela):
        if self.imagem:
            tela.blit(
                self.imagem,
                (self.rect.x, self.rect.y)
            )
        else:
            pygame.draw.rect(tela, (255, 0, 0), self.rect)
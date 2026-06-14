import sys
import pygame

pygame.init()
pygame.font.init()


def mostrar_mensagem(tela, texto, tamanho, cor, x, y):
    """Função auxiliar para desenhar textos na tela facilmente."""
    fonte = pygame.font.SysFont("Arial", tamanho, bold=True)
    superficie_texto = fonte.render(texto, True, cor)
    retangulo_texto = superficie_texto.get_rect(center=(x, y))
    tela.blit(superficie_texto, retangulo_texto)


def iniciar_jogo():
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Nave Espacial")

    relogio = pygame.time.Clock()
    FPS = 60

    vidas = 3 
    jogando = True
    game_over = False

    while jogando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

            if game_over and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: 
                    vidas = 3
                    game_over = False
                elif evento.key == pygame.K_ESCAPE:  
                    jogando = False

        if not game_over:

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                vidas -= 1
                pygame.time.delay(200)  

            if vidas <= 0:
                game_over = True

        tela.fill((0, 0, 0))  

        if not game_over:
            mostrar_mensagem(
                tela, f"Vidas: {vidas}", 30, (255, 255, 255), 70, 30
            )
        else:
            mostrar_mensagem(
                tela, "GAME OVER", 60, (255, 0, 0), LARGURA // 2, ALTURA // 2 - 50
            )
            mostrar_mensagem(
                tela,
                "Pressione R para Reiniciar ou ESC para Sair",
                24,
                (255, 255, 255),
                LARGURA // 2,
                ALTURA // 2 + 30,
            )

        pygame.display.update()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    iniciar_jogo()
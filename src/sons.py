import pygame
import os

class GerenciadorAudio:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            

        self.caminho_assets = os.path.join(os.path.dirname(__file__), '..', 'assets')

        try:
            self.som_tiro = pygame.mixer.Sound(os.path.join(self.caminho_assets, 'som_tiro.wav'))
            self.som_explosao = pygame.mixer.Sound(os.path.join(self.caminho_assets, 'som_explosao.wav'))
            self.som_dano = pygame.mixer.Sound(os.path.join(self.caminho_assets, 'som_dano.wav'))
        except pygame.error as e:
            print(f"Erro ao carregar efeitos sonoros: {e}")
            self.som_tiro = self.som_explosao = self.som_dano = None

        self.musica_fundo_path = os.path.join(self.caminho_assets, 'musica_fundo.mp3')

    def tocar_tiro(self):
        if self.som_tiro:
            self.som_tiro.play()

    def tocar_explosao(self):
        if self.som_explosao:
            self.som_explosao.play()

    def tocar_dano(self):
        if self.som_dano:
            self.som_dano.play()

    def iniciar_musica_fundo(self, volume=0.5):
        """Inicia a música de fundo em loop infinito."""
        if os.path.exists(self.musica_fundo_path):
            try:
                pygame.mixer.music.load(self.musica_fundo_path)
                pygame.mixer.music.set_volume(volume)
             
                pygame.mixer.music.play(-1)
            except pygame.error as e:
                print(f"Erro ao tocar música de fundo: {e}")
        else:
            print("Arquivo de música de fundo não encontrado.")

    def parar_musica_fundo(self):
        pygame.mixer.music.stop()

    def ajustar_volume_efeitos(self, volume):
        """Ajusta o volume de todos os efeitos sonoros (0.0 a 1.0)"""
        if self.som_tiro: self.som_tiro.set_volume(volume)
        if self.som_explosao: self.som_explosao.set_volume(volume)
        if self.som_dano: self.som_dano.set_volume(volume)
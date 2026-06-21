
from src.jogo import executar_jogo


if __name__ == "__main__":
    # Ponto de entrada da aplicação.
    executar_jogo()


from src.sons import GerenciadorAudio

audio = GerenciadorAudio()

audio.iniciar_musica_fundo(volume=0.3) 
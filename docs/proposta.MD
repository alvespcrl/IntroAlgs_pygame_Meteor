# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> LALA Space


## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Gustavo Alves Costa Sousa
- Nome 2: Allan Cristian Rodrigues
- Nome 3: Lourenço Hamdan Quirino Costa
- Nome 4: Luíz Felipe Pereira Guimarães

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Nave desviando e Atirando em Obstáculos.

## 4. Descrição geral do jogo

Descrição:

> O jogador contrala uma nave espacial que se movimenta para esquerda e direita para desviar e destruir meteoros e para cada meteoro destruído o jogador acumula pontos. O jogo a medida que passa fica cada vez mais dificil com o aumento da velocidade e qauntidade de meteoros.

## 5. Objetivo do jogador

Objetivo:

> Sobreviver o maior tempo possível e destruir meteoros para acumular pontos

## 6. Regras principais

Regras do grupo:

- Regra 1: A nave pode se mover para esquerda e direita.
- Regra 2: O jogador pode disparar tiros.
- Regra 3: Meteoros caem do topo da tela.
- Regra 4: Quando um tiro atinge um meteoro, ele é destruído.
- Regra 5: Quando um meteoro atinge a nave, o jogador perde uma vida.
- Regra 6: Novos meteoros surgem continuamente.
- Regra 7: A dificuldade aumenta ao longo do tempo.

## 7. Condição de vitória

Condição de vitória:

> Não existe vitória. O objetivo é fazer a maior pontuação possível.

## 8. Condição de derrota ou encerramento

> Perder todas as 3 vidas.

## 9. Elementos previstos no jogo

    Nave espacial
    Meteoros
    Tiros
    Contador de pontos
    Sistema de vidas
    Tela inicial
    Tela de Game Over

## Jogador ou elemento principal

Descrição:

> Nave controlada pelo "a" e "d" e as setas "<" e ">" e espaço para atirar. 

## Obstáculos, inimigos ou desafios

Descrição:

> Meteoros aparecem em posições aleatórias e devem ser evitados ou destruídos.

## Itens, alvos ou objetos de interação

Descrição:

> O jogador controla uma nave espacial e deve destruir meteoros utilizando projéteis. Os meteoros surgem aleatoriamente na parte superior da tela. Os tiros disparados podem destruir os meteoros antes que eles atinjam o jogador.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador inicia a partida com 3 vidas. Cada meteoro destruído concede 10 pontos. A partida termina quando todas as vidas forem perdidas.

Descrição:

> O jogador inicia a partida com 3 vidas. Cada meteoro destruído concede 10 pontos. A partida termina quando todas as vidas forem perdidas ou quando o jogador for eliminado

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: A ou Seta para esquerda: mover a nave para a esquerda
- Tecla/comando: D ou Seta para direita: mover a nave para a direita
- Tecla/comando: Espaço: Para atirar projeteis
- Tecla/comando: ESC: Sair do jogo

## 11. Organização inicial do código

Organização planejada:

> main.py: inicia a execução do jogo; 
> src/jogo.py: contém o loop principal do jogo;
> src/jogador.py: funções relacionadas à nave do jogador;
> src/meteoro.py: criação e movimentação dos meteoros;
> src/tiro.py: criação e movimentação dos projéteis;
> src/config.py: configurações gerais do jogo;
> src/dados.py: leitura e escrita de recordes em arquivo.


## 12. Recursos externos previstos

Recursos previstos:

> imagens gratuitas para a nave e meteoros;
> sons gratuitos para tiros e explosões;
> tutoriais de Pygame utilizados apenas como referência;
> fonte padrão do Pygame para exibição dos textos.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementação das colisões entre tiros e meteoros;
- Dificuldade 2: Controle do surgimento e movimentação dos meteoros;
- Dificuldade 3: Organização do código em módulos e funções.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pelo teclado, meteoros surgindo na tela, sistema de disparos, sistema de vidas, sistema de pontuação e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Tela inicial e menu de pausa;
- Melhoria 2: Aumento progressivo da dificuldade;
- Melhoria 3: Diferentes tipos de meteoros;
- Melhoria 4: Ranking de pontuações;
- Melhoria 5: Efeitos sonoros e animações;
- Melhoria 6: Poderes especiais para a nave.
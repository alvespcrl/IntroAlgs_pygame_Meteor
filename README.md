# Nome do Jogo

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Gustavo Alves
- Allan Cristian
- Luiz Felipe
- Lourenço Hanbam

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo


> O jogo consiste em controlar uma nave que deve atirar para destruir os meteoros para ganhar pontos e evita-los. O jogador perde vidas ao colidir com o meteoro. A partida termina quando o jogador perde todas as vidas.

## Objetivo do jogador

> O objetivo é fazer a maior quantidade possível de pontos, evitando colisões com os meteoros

## Regras do jogo

Liste as principais regras do jogo.

Exemplo:

- O jogador se movimenta usando as setas e o w/a/s/d do teclado.
- Cada meteoro destruido aumenta a pontuação.
- Colidir com um meteoro reduz a quantidade de vidas.
- A partida termina quando o jogador perde todas as vidas.

## Controles

Informe as teclas ou comandos utilizados no jogo.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- W : mover para cima
- A : para baixo: mover para baixo
- S : mover para esquerda
- D : mover para direita
- Espaço: Atirar

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.

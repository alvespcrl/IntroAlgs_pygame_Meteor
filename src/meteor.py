import random

# cria um novo meteoro
def criar_meteoro():
    meteoro = {
        "x": random.randint(0, 760),
        "y": -40,
        "velocidade": random.randint(3, 8),
        "tamanho": random.randint(20, 60)
    }

    return meteoro

# move um meteoro
def mover_meteoro(meteoro):
    meteoro["y"] += meteoro["velocidade"]
# move todos meteoros da lista
def mover_meteoros(meteoros):
    for meteoro in meteoros:
        mover_meteoro(meteoro)

# Remove meteoros que saíram da tela
def remover_meteoros(meteoros, altura_tela):
    meteoros[:] = [
        meteoro
        for meteoro in meteoros
        if meteoro["y"] < altura_tela
    ]

# aumenta a velocidade dos meteoros
def aumentar_dificuldade(meteoros, nivel):
    for meteoro in meteoros:
        meteoro["velocidade"] = 5 + nivel

# TESTE
if __name__ == "__main__":

    meteoros = []

    for i in range(5):
        meteoros.append(criar_meteoro())

    print("Meteoros criados:")
    print(meteoros)
    

    mover_meteoros(meteoros)

    print("\nMeteoros após movimento:")
    print(meteoros)

    remover_meteoros(meteoros, 600)

    print("\nMeteoros após remoção:")
    print(meteoros)
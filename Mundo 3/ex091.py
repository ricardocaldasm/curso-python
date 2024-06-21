from random import randint
from operator import itemgetter

jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}

ranking = list()

for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# utilizado para deixar os valores em ordem crescente - 0 para chave e 1 para valor

for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]} pontos.")

camp = dict()
gols = list()

camp["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {camp['nome']} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
camp["gols"] = gols[:]
camp["total"] = sum(gols)
print("=-" * 30)
print(camp.items())
print("=-" * 30)
for k, v in camp.items():
    print(f"O campo {k} tem o valor {v}")
print("=-" * 30)
print(f'O jogador {camp['nome']} jogou {partidas} partidas.')
for i in range(0,partidas):
    print(f'Na partida {i+1}, fez {gols[i]} gols')

'''
for i,v in enumerate(camp['gols']): #v lê o valor dentro da lista
    print(f'Na partida {i+1}, fez {v} gols.')
'''

time = list()
jogador = dict()
gols = list()
cod = 0

while True:
    cod += 1
    jogador["cod"] = cod
    jogador["nome"] = str(input("Nome do jogador: "))
    jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    for i in range(0, jogador["partidas"]):
        gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    gols.clear()
    time.append(jogador.copy()) #.copy() utilizado para copiar dicionários, diferente de [:] que é utilizado em listas
    jogador.clear()
    while True:
        opt = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
        if opt not in 'SN':
            print('Opção incorreta! Digite S ou N.')
        else:
            break
    if opt in 'N':
        break

for k in time[0].keys():
    print(f'{k:<15}', end = " ")

print()
for i,j in enumerate(time):
    for v in j.values():
        print(f'{str(v):<15}', end=" ")
    print()

while True:
    dados = int(input("Mostrar dados de qual jogador? (0 para sair) "))
    if dados > len(time) or dados < 0:
        print('Dado inválido. Favor digite o código correto.')
    elif dados != 0:
        print(f'Levantamento do jogador {time[dados-1]['nome']}.')
        for i,j in enumerate (time):
            if dados == j['cod']:
                for o,p in enumerate(j['gols']):
                    print(f'No jogo {o+1} fez {p} gols.')
    if dados == 0:
        break

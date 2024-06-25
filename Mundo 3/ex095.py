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

print(time)

for k in time[0].keys():
    print(k, end = " ")

print()
for i,j in enumerate(time):
    for v in j.values():
        print(v, end=" ")
    print()

while True:
    dados = int(input("Mostrar dados de qual jogador? (0 para sair) "))
    if dados != 0:
        for i,j in enumerate(time):
            if j['cod'] == dados:
                for k,v in j.items():
                    print(v)
    if dados == 0:
        break

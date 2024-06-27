def jogador(nome="<desconhecido>", gol=0):
    print(f"O jogador {nome} fez {gol} gol(s) no campeonato.")


jog = str(input("Nome do jogador: "))
num = str(input("Número de gols: "))
if num.isnumeric():
    num = int(num)
else:
    num = 0
if jog.strip() == "":
    jogador(gol=num)
else:
    jogador(jog,num)

from random import randint

linha = list()
coluna = list()

for i in range(0,3):
    for j in range(0,3):
        num = randint(0,9)
        coluna.append(num)
    linha.append(coluna[:])
    coluna.clear()

for i in range(0,3):
    print(linha[i])


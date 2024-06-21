"""
linha = list()
coluna = list()

for i in range (0,3):
    for j in range (0,3):
        num = int(input('Digite um valor para [{}, {}]: ' .format(i,j)))
        linha.append(num)
    coluna.append(linha[:])
    linha.clear()

print(coluna[0])
print(coluna[1])
print(coluna[2])
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]:^5}", end="")
    print()

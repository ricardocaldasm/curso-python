from random import randint

linha = list()
coluna = list()
par = col = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        num = randint(0, 9)
        if num % 2 == 0:
            par += num
        if j == 2:
            col += num
        if i == 1:
            if j == 0:
                maior = num
            elif num > maior:
                maior = num
        coluna.append(num)
    linha.append(coluna[:])
    coluna.clear()

for i in range(0, 3):
    print(linha[i])

print(f"A soma dos valores pares é {par}.")
print(f"A soma dos valores da terceira coluna é {col}")
print(f"O maior valor da segunda linha é {maior}")

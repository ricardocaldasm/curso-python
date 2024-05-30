menor = 0
maior = 0
for i in range(1,6):
    peso = float(input('Peso da {}ª pessoa: ' .format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso peso lido foi de {:.1f}kg.\nO menor peso lido foi de {:.1f}kg.' .format(maior, menor))
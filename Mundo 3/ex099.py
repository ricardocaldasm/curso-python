from random import randint


def maior(val):
    # print(val) aparece os valores dentro da tupla e print(*val) aparece somente os valores
    # caso queira colocar uma lista dentro da função maior(), não posso utilizar *.
    cont = maior = 0
    for i in val:
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(maior)


lista = list()
for i in range(0, randint(1, 5)):
    lista.append(randint(0, 10))
print(lista)

maior(lista)

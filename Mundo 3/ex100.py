from random import randint


def sorteio(lista):
    print("Sorteando 5 valores da lista:", end=" ")
    for i in range(0, 5):
        lista.append(randint(0, 9))
    print(lista)


def somapar(lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += i
    print(f"Somando os valores pares de {lista}: {cont}")


num = list()
sorteio(num)
somapar(num)

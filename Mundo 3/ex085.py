lista = [[], []]
for i in range(1, 8):
    valor = int(input("Digite o {}º valor: ".format(i)))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f"Os valores {lista[0]} são pares e o valores {lista[1]} são ímpares.")

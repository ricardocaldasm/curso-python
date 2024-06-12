lista = []
for i in range(0, 5):
    lista.append(int(input(f"Digite o valor para a posição {i}: ")))

print(f"Você digitou os valores {lista}.")

max = max(lista)
min = min(lista)

print(f"O maior valor digitado foi {max} nas posições", end=" ")
for p, n in enumerate(lista):
    if n == max:
        print(p, end=" ")

print(f"\nO menor valor digitado foi {min} nas posições", end=" ")
for p, n in enumerate(lista):
    if n == min:
        print(p, end=" ")

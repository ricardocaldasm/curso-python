from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(lista)

for i in range(0, len(lista)):
    print(lista[i], end=" ")

print(f"\nO maior valor foi {max(lista)}")
print(f"O menor valor foi {min(lista)}")

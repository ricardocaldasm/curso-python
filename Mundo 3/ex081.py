lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    opt = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if opt in "N":
        break

print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")

if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")

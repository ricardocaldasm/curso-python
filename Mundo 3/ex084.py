lista = list()
dados = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    opcao = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if opcao in "N":
        break

print(lista)

print(f"Ao todo você cadastrou {len(lista)} pessoa(s).")
print(f"O maior peso foi {maior}kgs. Peso de", end=" ")
for i in lista:
    if i[1] == maior:
        print(f"[{i[0]}]", end=" ")
print()
print(f"O menor peso foi {menor}kgs. Peso de", end=" ")
for i in lista:
    if i[1] == menor:
        print(f"[{i[0]}]", end=" ")

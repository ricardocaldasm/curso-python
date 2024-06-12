lista = []
for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > lista[len(lista) - 1]:
        lista.append(num)
        print("Valor adicionado na última posição")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Valor adicionado na posição {pos}")
                break
            pos += 1

print(f"Os valores adicionados em ordem foram {lista}")

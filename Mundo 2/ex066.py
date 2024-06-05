soma = cont = 0

while True:
    num = float(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} valores foi de {soma}')
resp = 'S'
cont = soma = maior = menor = 0

while resp == 'S':
    num = float(input('Digite um número: '))
    cont += 1
    soma += num
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/cont
print('Você digitou {} números e a média é de {}' .format(cont,media))
print('O maior número foi {} e o menor número foi {}.' .format(maior, menor))
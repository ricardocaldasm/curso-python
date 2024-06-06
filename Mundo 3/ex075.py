num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

lista = (num1, num2, num3, num4)
print(f'Você digitou os valores: {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
print(f'O valor 3 foi digitado na posição {lista.index(3)+1}' if 3 in lista else 'Não foi digitado o valor 3.')
print(f'Os valores pares digitados foram: ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=' ')
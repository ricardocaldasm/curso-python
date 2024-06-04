from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))

fat = 1
cont = num

print('O resultado de {}! = ' .format(num), end='')
while cont > 0:
    fat *= cont
    print('{}' .format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1    

print('{}.' .format(fat))

print('O resultado de {}! é igual a {}.' .format(num,factorial(num)))
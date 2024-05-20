num = int(input('Digite um número de 0 a 9999: '))
print('Milhar: {}' .format(num // 1000 % 10)) #// divisão inteira %resto da divisão
print('Centema: {}' .format(num // 100 % 10))
print('Dezena: {}' .format(num // 10 % 10))
print('Unidade: {}' .format(num // 1 % 10))
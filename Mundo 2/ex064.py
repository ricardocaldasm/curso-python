soma = num = cont = 0

num = float(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = float(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}' .format(cont, soma))
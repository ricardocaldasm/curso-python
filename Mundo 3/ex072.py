while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if num not in range(0,11):
        print('Valor incorreto.')
    else:
        break

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

print(f'Você digitou o número {lista[num]}')
from random import randint
from time import sleep

user_opt = str(input('Escolha PAR ou IMPAR: ')).upper().strip()[0]

while True:
    if user_opt not in 'IÍP':
        user_opt = str(input('Opcão inválida. Favor escolher PAR ou IMPAR: ')).upper().strip()[0]
    else:
        break

if user_opt in 'IÍ':
    user_opt = 'ÍMPAR'
    pc_opt = 'PAR'
elif user_opt in 'P':
    user_opt = 'PAR'
    pc_opt = 'ÍMPAR'
else:
    print('ERRO')

user = int(input('Digite um numero de 0 a 10: '))

while True:
    if user not in range(0,11):
        user = int(input('Valor inválido. Por favor, digite um valor de 0 a 10: '))
    else:
        break

pc = randint(0,10)

soma = user + pc
result = (soma) % 2

if result == 0:
    result_opt = 'PAR'
else:
    result_opt = 'ÍMPAR'

if result_opt == user_opt:
    print('Você venceu!')
elif result_opt == pc_opt:
    print('Você perdeu!')
else:
    print('ERRO')

print(f'Você escolheu: {user_opt}. Seu número escolhido foi: {user}')
print(f'O computador escolheu: {pc_opt}. O número escolhido pelo computador foi: {pc}')
print(f'A soma é {soma}, que é {result_opt}.')
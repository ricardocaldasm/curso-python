from random import randint

user = int(input('Digite um numero de 0 a 10: '))

while True:
    if user not in range(0,10):
        user = int(input('Valor inválido. Por favor, digite um valor de 0 a 10: '))
    else:
        break

user_opt = str(input('Escolha PAR ou IMPAR.')).upper().strip()[0]

while True:
    if user_opt != 'I'or user_opt != 'P':
        user_opt = str(input('Opcão inválida. Favor escolher PAR ou IMPAR')).upper().strip()[0]
    else:
        break

if user_opt == 'I':
    pc_opt = 'P'
else:
    pc_opt = 'I'

print(f'Sua opção: {user_opt} | Opção do PC: {pc_opt}')
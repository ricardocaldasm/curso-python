from random import randint
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')

itens = ('Pedra', 'Papel', 'Tesoura')

pc = randint(0,2)
jog = int(input('Qual é a sua jogada? '))

if jog == 0 or jog == 1 or jog == 2:
    if pc == jog:
        print('EMPATE')
    elif (pc == 0 and jog == 2) or (pc == 1 and jog == 0) or (pc == 2 and jog == 1):
        print('VOCÊ PERDEU!')
    else:
        print('VOCÊ GANHOU!')

    print('-='*15)
    print('Você escolheu {}.' .format(itens[jog]))
    print('O computador escolheu {}.' .format(itens[pc]))
    print('-='*15)

else:
    print('Jogada Inválida.')
from random import randint

ran = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?''')
num = int(input('Qual é seu palpite? '))

cont = 1
while num != ran:
    if num < ran:
        num = int(input('Mais... Tente mais uma vez: '))
    if num > ran:
        num = int(input('Menos... Tente mais uma vez: '))
    cont += 1

print('Acertou com {} tentativas. Parabéns.' .format(cont))
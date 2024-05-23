from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
num = int(input('Em que número pensei? '))
rand = randint(0,5)
print('Processando...')
sleep(1)
if num != rand:
    print('Ganhei. Eu pensei no número {} e não no {}.' .format(rand, num))
else:
    print('Você ganhou. Eu pensei no número {}.' .format(rand))
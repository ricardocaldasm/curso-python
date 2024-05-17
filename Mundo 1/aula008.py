import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}' .format(num, math.ceil(raiz))) #ceil arredonda pra cima; floor para baixo

#from math import sqrt -> utilizar somente sqrt(raiz)

import random
num = random.randint(1,10)
print(num)

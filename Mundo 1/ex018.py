import math
a = float(input('Digite o ângulo: '))
rad = math.radians(a)
print('O ângulo de {} tem o seno de {:.2f}' .format(a,math.sin(rad)))
print('O ângulo de {} tem o cosseno de {:.2f}' .format(a,math.cos(rad)))
print('O ângulo de {} tem o tangente de {:.2f}' .format(a,math.tan(rad)))
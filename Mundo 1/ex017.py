from math import sqrt, pow, hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = sqrt(pow(co,2)+pow(ca,2))
print('Hipotenusa: {}' .format(h))
print('Hipotenusa: {}' .format(hypot(co,ca)))
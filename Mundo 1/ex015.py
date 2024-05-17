d = float(input('Distância percorrida: '))
t = int(input('Dias de aluguel: '))
p = 60*t + 0.15*d
print('Preço a pagar é de R${:.2f}' .format(p))
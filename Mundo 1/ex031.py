d = float(input('Qual a distância da viagem? '))
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('O preço da passagem será de R${:.2f}' .format(preco))
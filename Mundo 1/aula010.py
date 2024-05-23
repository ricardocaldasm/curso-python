tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

print('Carro novo' if tempo <=3 else 'Carro velho')

nome = str(input('Qual é seu nome? '))
if nome == 'Ricardo':
    print('Belo Nome')
else:
    print('Que nome feio')
print('Bom dia, {}!' .format(nome))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}.' .format(m))
if m >= 6:
    print('Passou de ano')
else:
    print('Recuperação')
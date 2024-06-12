lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    opt = str(input('Quer continuar? ')).strip().upper()[0]
    if opt in 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'Lista completa: {lista}')
print(f'Lista dos pares: {par}')
print(f'Lista dos ímpares: {impar}')
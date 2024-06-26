def area(l,c):
    a = l*c
    print(f'A área de um terreno {l}m x {c}m é de {a}m².')

print('Controle de terreno')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg,comp)
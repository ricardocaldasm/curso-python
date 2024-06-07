print('-'*30)
print(f'{'LISTAGEM DE PREÇOS':^30}')
print('-'*30)

materiais = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.9, 'Mochila', 120.85, 'Canetas', 22.3, 'Livro', 34.9

for i in range(0,len(materiais)):
    if i % 2 == 0:
        print(f'{materiais[i]:.<22}', end='')
    else:
        print(f'R${materiais[i]:>6.2f}')
print('-'*30)
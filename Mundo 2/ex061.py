print('GERADOR DE PA\n'+'-='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

cont = 0
while cont < 10:
    print('{} -> ' .format(termo) if cont < 9 else '{}' .format(termo), end='')
    termo += razao
    cont += 1
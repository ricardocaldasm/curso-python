print('Gerador de PA\n'+'-='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

cont = 0
quant = 10
total = 0
while quant != 0:
    total += quant
    while cont < total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    quant = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))

'''
while quant != 0:
    cont = 0
    while cont < quant:
        termo += razao
        cont += 1
        print('{} ->' .format(termo), end=' ')
    print('PAUSA')
    quant = int(input('Quantos termos você quer mostrar mais? '))
'''
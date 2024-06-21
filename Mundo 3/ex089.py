dados = list()
lista = list()

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    opt = str(input('Quer continuar [S/N?]? ')).strip().upper()[0]
    if opt == 'N':
        break

print(f'{'No.':<8}{'Nome':<15}{'Média':<10}')
for i, l in enumerate(lista):
    media = (l[1] + l[2])/2
    print(f'{i:<7} {l[0]:<14} {media:<10}')

while True:
    num = int(input('Mostrar nota de qual aluno (999 para sair)? '))
    if num == 999:
        break
    if num > len(lista) - 1:
        print('Digite um valor válido!')
    else:
        print(f'Notas de {lista[num][0]} são {lista[num][1]} e {lista[num][2]}')

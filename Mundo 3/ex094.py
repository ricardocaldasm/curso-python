#neste exercício, fiz as listas dentro de um dicionário. o correto seria ter feito dicionários dentro de uma lista

dicio = dict()
lnome = list()
lsexo = list()
lidade = list()

while True:
    nome = str(input('Nome: '))
    lnome.append(nome)
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print(f'Valor incorreto! Por favor, digite M ou F.')
        else:
            break
    lsexo.append(sexo)
    idade = int(input('Idade: '))
    lidade.append(idade)
    while True:
        opt = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if opt not in 'SN':
            print(f'Valor incorreto! Por favor, digite S ou N.')
        else:
            break
    if opt in 'N':
        break

dicio['nome'] = lnome[:]
dicio['sexo'] = lsexo[:]
dicio['idade'] = lidade[:]
print(dicio)
print('=-'*30)
print(f'Ao todo temos {len(dicio['nome'])} pessoas cadastradas.')
print(f'A média de idade é de {sum(dicio['idade'])/len(dicio['idade'])}.')
print(f'As mulheres cadastradas foram', end=' ')
for i,v in enumerate(dicio['sexo']):
    if v == 'F':
        print(dicio['nome'][i], end=' ')
print('\nLista das pessoas que estão acima da média: ')

for c in range(0,len(dicio['nome'])):
    for k,v in dicio.items():
        print(f'{k} = {v[c]};', end=' ')
    print()

#[0][0] [1][0] [2][0]

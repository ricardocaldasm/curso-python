dicio = dict()

dicio['nome'] = str(input('Nome: '))
dicio['media'] = float(input('Média: '))

if dicio['media'] < 5:
    dicio['situacao'] = 'reprovado'
elif dicio['media'] >= 5 and dicio['media'] < 7:
    dicio['situacao'] = 'recuperação'
elif dicio['media'] >= 7:
    dicio['situacao'] = 'aprovado'

for k, v in dicio.items():
    print(f'{k} é igual a {v}.')
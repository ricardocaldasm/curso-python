from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <=19:
    print('Classificação: JÚNIOR')
elif 19 < idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
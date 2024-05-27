from datetime import date

nas = int(input('Ano de nascimento: '))

atual = date.today().year
idade = atual - nas

print('Quem nasceu em {} tem {} anos em {}.' .format(nas, idade, atual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}.' .format(18-idade, atual+18-idade))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você já deveria ter se alistado a {} anos.\nSeu alistamento foi em {}.' .format(idade-18, atual-(idade-18)))
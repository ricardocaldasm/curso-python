somaidade = 0
cont = 0
velho = 0
nomevelho = ''

for i in range(1,5):
    print('-'*5,'{}ª PESSOA' .format(i),'-'*5)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if sexo == 'M':
        if i == 1:
            velho = idade
        else:
            if idade > velho:
                velho = idade
                nomevelho = nome
    if sexo == 'F':
        if idade < 20 and sexo == 'F':
            cont += 1

print('A média de idade do grupo é de {:.0f} anos.' .format(somaidade/i))
print('O homem mais velho tem {} anos e se chama {}' .format(velho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(cont))
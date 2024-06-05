print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

cont = cont1000 = soma = 0

while True:
    prod = str(input('Digite o nome do produto: '))
    cont += 1
    preco = float(input('Preço: R$'))
    soma += preco
    if preco >= 1000:
        cont1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        prodmenor =  prod
    opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opcao in 'N':
        break

print(f'O total de {cont} produtos comprados foi R${soma}.')
print(f'Temos {cont1000} produto(s) custando R$1000,00 ou mais')
print(f'O produto mais barato foi {prodmenor} e custou {menor}.')
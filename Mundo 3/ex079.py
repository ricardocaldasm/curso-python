lista = []

while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não será adicionado.')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opcao not in 'SN':
        print('Digite uma opção válida.')
    if opcao == 'N':
        break

print('-='*30)
lista.sort()
print(f'Você digitou os valores: {lista}')
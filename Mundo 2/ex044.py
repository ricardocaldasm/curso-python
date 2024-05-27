print('='*10,'LOJAS AMERICANAS','='*10)
val = float(input('Valor das compras: R$'))
print('''FORMAR DE PAGAMENTO
[1] pix ou dinheiro 
[2] débito
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = val * 0.9
    print('Sua compra terá 10% de desconto.')
elif opcao == 2:
    total = val * 0.95
    print('Sua compra terá 5% de desconto.')
elif opcao == 3:
    total = val
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.' .format(val/2))
elif opcao == 4:
    total = val * 1.2
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.' .format(parcela, (val*1.2)/parcela))
else:
    total = val
    print('Opção inválida.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(val,total))
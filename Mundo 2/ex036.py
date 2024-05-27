casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
fin = float(input('Anos de financiamento: '))

prest = casa/(fin*12)
print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação mensal será de R${:.2f}.' .format(casa,fin,prest))

if prest <= 0.3*salario:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEDADO!')
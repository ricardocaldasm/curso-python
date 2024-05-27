num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:)
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
base = int(input('Sua opção: '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}.' .format(num, bin(num))) #inicial 0b para binário | usar bin(num)[2:] para renmover
elif base == 2:
    print('{} convertido para OCTAL é igual a {}.' .format(num, oct(num))) #inicial 0o oara octal
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.' .format(num, hex(num))) #inicial 0x para hexadecimal
else:
    print('Opção inválida. Tente novamente.')
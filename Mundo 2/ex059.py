num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa''')

    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        result = num1 + num2
        print('A soma dos valores é {}.' .format(result))
    elif opcao == 2:
        result = num1 * num2
        print('O produto dos valores é {}.' .format(result))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('Entre {} e {} o maior valor é {}.' .format(num1,num2,maior))
        elif num2 > num1:
            maior = num2
            print('Entre {} e {} o maior valor é {}.' .format(num1,num2,maior))
        elif num1 == num2:
            print('Os valores são iguais.')    
    elif opcao == 4:
        num1 = float(input('Digite o novo primeiro valor: '))
        num2 = float(input('Digite o novo segundo valor: '))
    elif opcao > 5:
        print('Opção incorreta. Favor digitar uma da opções válidas.')

print('FIM DO PROGRAMA')
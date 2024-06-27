def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("Erro! Digite um número inteiro válido")
        if ok:
            break
    return valor

num = leiaint('Digite um número: ')
print(f'Você digitou o número {num}.')
def escreva(txt):
    comp = len(txt)
    print('~'*comp)
    print(txt)
    print('~'*comp)

msg = str(input('Digite uma mensagem: '))
escreva(msg)
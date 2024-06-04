sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0] #fatiamento para pegar só o primeiro caractere

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.' .format(sexo))
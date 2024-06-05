cont18 = contmasc = contfem20 = 0

while True:
    idade = int(input('Idade: '))
    if idade > 18:
        cont18 += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        contmasc += 1
    if sexo == 'F' and idade < 20:
        contfem20 += 1
    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opcao != 'S':
        break

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contmasc} homem(s) cadastrado(s).')
print(f'Temos {contfem20} mulher(es) com menos de 20 anos.')
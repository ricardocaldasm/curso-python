nome = input('Digite o nome completo: ').strip() #remove espaços antes a depois
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
dividido = nome.split()
print(len(dividido[0]))
nome = str(input('Nome completo: ')).strip()
lista = nome.split()
print('Primeiro nome: {}' .format(lista[0]))
print('Último nome: {}' .format(lista[len(lista)-1]))

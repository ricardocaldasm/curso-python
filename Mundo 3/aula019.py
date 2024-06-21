dicionario = {'cor':'azul',
              'numero':22,
              'formato':'quadrado'
              }

print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

for k,v in dicionario.items(): #chave e valor - NÃO TEM O ENUMERATE
    print(k,v)

lista = list()
lista.append(dicionario)

print(lista[0]['cor'])
print(f'{dicionario['numero']}')

for k in dicionario.keys():
    print(k)

for v in dicionario.values():
    print(v)

dicionario['cor'] = 'vermelho'
print(dicionario['cor'])

dicionario['nome'] = 'Ricardo' #não precisa de append
print(dicionario.items())

#em dicionário, não é possível fazer cópia por fatiamento [:] - tem que ser feito .copy()

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil: #variável e passa por todos os itens do dicionário
    for k,v in e.items(): #variável k passa por 'uf' e 'sigla' e v passa pelo valor inserido de 'Estado' e 'Sigla'
        print(f'O campo {k} tem valor {v}.')
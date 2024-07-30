"""
Listas compostas:
pessoas = [["Pedro", 25], ["Maria", 19], ["João", 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
"""

teste = list()
teste.append("Ricardo")
teste.append(33)
galera = list()
galera.append(teste)
teste[0] = "Deborah"
teste[1] = 32
galera.append(teste)
# neste caso, o append faz uma ligação entre as duas estruturas. Neste caso, deve usar o [:]
print(galera)

teste2 = list()
teste2.append("Ricardo")
teste2.append(33)
galera2 = list()
galera2.append(teste2[:])
teste2[0] = "Deborah"
teste2[1] = 32
galera2.append(teste2[:])
print(galera2)

grupo = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for i in grupo:
    print(f'{i[0]} tem {i[1]} anos de idade.')

grupo2 = list()
dado = list()
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo2.append(dado[:])
    dado.clear()
print(grupo2)

for p in grupo2:
    if p[1] >=18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade.')
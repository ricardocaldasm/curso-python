'''
() -> tupla
[] -> lista
{} -> dicionário
tuplas são imutáveis
tuplas podem ser criadas sem parênteses
'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1]) #a referência sempre é feita com colchetes
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))

#lanche[1] = 'refrigerante' errado, pois tuplas são imutáveis

for pos, comida in enumerate(lanche):
    print(comida,pos, end=' ')
print('')
for cont in range(0,len(lanche)):
    print(lanche[cont], cont, end=' ')
print('')
print(sorted(lanche)) #mostra em ordem alfabética - é feito através de listas, pois tem colchetes

a = (2, 5, 8)
b = (5, 8, 1, 2)
c = a + b #a ordem tem diferença. b + a != a + b
print(c)
print(c.count(5)) #conta o número de vezes que aparece o 5
print(c.index(5)) #primeira posição que aparece
print(c.index(5,2)) #a partir da prosição 2
del(a) #apagou os dados de a
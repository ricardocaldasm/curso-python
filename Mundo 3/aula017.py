'''
listas são mutáveis e podem adicionar valores (append) ou inserir valores (insert)
para deletar pela posição: del lista[3] ou lista.pop(3) - caso seja lista.pop(), ele elimina o último elemento
para deletar pelo nome: lista.remove(item1)
no caso de remoção, os itens são reposicionados ao invés de ficar um espaço vazio

valores = [8,5,7,3,5]
valores.sort() - ordem crescente
valores.sorte(reverse=True) - ordem decrescente
'''
lista = [3, 5, 6, 1]
lista[1] = 3  # listas são mutáveis
# num[4] = 7 não funciona, pois valores não são adicionados dessa maneira
lista.append(7)
lista.insert(2, 9) #Insere o valor 9 na posição 2 e sobe todos de posição
lista.pop()  # elimina o último elemento se o parênteses estiver vazio
# elimina o primeiro elemento 3, e não na posição 3. Elimina somente a primeira ocorrência
lista.remove(3)
# lista.sort(reverse=True)
print(lista)
print(f'Essa lista tem {len(lista)} elementos.')

exemplo = []
for i in range(0, 3):
    exemplo.append(int(input('Digite o valor: ')))
print(exemplo)
for c, i in enumerate(exemplo):
    print(f'Posição {c} valor {i}')

a = [5, 3, 7, 1]
b = a  # o python faz uma ligação de listas. Sendo assim, o que modificar na b também vai modificar na a
b[0] = 2
print(a)
print(b)

c = [1, 3, 5, 7]
d = c[:]  # neste caso, o python não realiza uma ligação e faz somente uma cópia
d[0] = 9
print(c)
print(d)

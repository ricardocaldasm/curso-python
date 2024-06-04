print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
t1 = 0
t2 = 1

qnt = int(input('Quantos termos você quer mostrar? '))

print('{} -> {} ->' .format(t1,t2), end =' ')

cont = 3
while cont <= qnt:
    t3 = t1 + t2
    print('{} ->' .format(t3), end = ' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
    
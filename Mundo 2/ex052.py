num = int(input('Digite um número: '))

cont = 0
for i in range(1,num+1):
    print(i, end=' ')
    if num % i == 0:
        cont += 1

print('\nO número {} foi divisível {} vezes.' .format(num,cont))

if cont <= 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É É PRIMO.')
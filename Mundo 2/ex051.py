print('='*15)
print('10 TERMOS DE UMA PA')
print('='*15)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(0,10):
    num = termo + razao*i
    print('{} ->' .format(num), end=' ')

print('Acabou!')
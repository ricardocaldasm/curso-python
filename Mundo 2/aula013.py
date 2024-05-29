for a in range(0, 4): # range não considera o último número
    print(a)
print('FIM')

for b in range(3, 0, -1):
    print(b)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo:'))

for c in range(i,f+1,p):
    print(c)

s = 0
for d in range(0,4):
    n = int(input('Digite um valor: '))
    s += n # é o mesmo de s = s + n
print('O somatório de todos os valores foi {}.' .format(s))
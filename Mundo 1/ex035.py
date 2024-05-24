print('*'*30)
print('Analisador de triângulo')
print('*'*30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Os segmentos acima NÃO PODEM formar um trigângulo.')
else:
    print('Os segmentos acima PODEM formar um triângulo.')
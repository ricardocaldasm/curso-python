a = float(input('Primeiro segmento: '))
b = float(input('Segumento segmento: '))
c = float(input('Terceiro segmento: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Não é possível formar um triângulo.')
else:
    if a == b == c:
        print('Triângulo equilátero.')
    elif a != b and a != c and b != c:
        print('Triângulo escaleno.')
    else:
        print('Triângulo isóceles.')
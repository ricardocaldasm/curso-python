peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual a sua altura em m? '))
imc = peso / pow(altura,2)
print('O IMC desta pessoa é {:.1f}.' .format(imc))
if imc < 18.5:
    print('Faixa de peso: MAGREZA')
elif imc < 25:
    print('Faixa de peso: NORMAL')
elif imc < 30:
    print('Faixa de peso: SOBREPESO')
elif imc < 40:
    print('Faixa de peso: OBESIDADE')
else:
    print('Faixa de peso: OBESIDADE GRAVE')
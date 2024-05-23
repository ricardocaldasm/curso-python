vel = float(input('Velocidade do carro: '))
multa = (vel-80) * 7
if vel<=80:
    print('Tudo ok. Dirija com segurança')
else:
    print('Multado! Você excedeu o limite de 80km/h.\nVocê deve pagar a multa de R${:.2f}' .format(multa))
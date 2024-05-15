a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
tinta = (a*l)/2
print('São necessários {:.2f} litros de tinta para pintar uma parde de {} metros por {} metros' .format(tinta,a,l))
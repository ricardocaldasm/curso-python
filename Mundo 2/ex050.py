s=0
cont=0
for i in range(0,6):
    num = int(input('Digite o {}º valor: ' .format(i+1)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Você informou {} números pares e a soma total deles é igual a {}' .format(cont,s))
s = 0
cont = 0
for i in range(1,501):
    if i % 3 == 0 and i % 2 ==1:
        cont = cont + 1
        s += i
print('A soma de {} números ímapares múltiplos de três no intervalo de 1 a 500 é igual a {}.' .format(cont,s))
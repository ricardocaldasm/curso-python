from datetime import date

menor = 0
maior = 0
for i in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? ' .format(i)))
    if (date.today().year - ano) < 18:
        menor += 1
    else:
        maior += 1
    
print('Ao todo tivemos {} pessoas menores de idade e {} pessoas maiores de idade' .format(menor,maior))
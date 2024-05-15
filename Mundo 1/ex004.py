a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a)) #a função input sempre retorna uma string
print('Só tem espaços?', a.isspace())
print('É um núnero?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculo?', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada?', a.istitle())

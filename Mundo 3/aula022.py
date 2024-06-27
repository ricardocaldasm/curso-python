from aula022modulos import fatorial

# definição de módulos em python | todo arquivo .py pode ser considerado um módulo
# não é recomendado pois pode gerar conflito caso haja uma segunda importação

num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")

from uteis import numeros

print(numeros.contador(0, 5))

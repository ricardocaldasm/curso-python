def soma(a, b):
    s = a + b
    print(f"A soma de {a} e {b} é igual a {s}.")
    # tem que dar 2 linhas de espaço após a função


def contador(*num):
    # * é utilizado para desempacotar. Neste caso, é quando o número de parâmetros é variável.
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.")


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


soma(4, 5)
soma(b=3, a=5)

contador(1, 2, 3)  # Os valores do desempacotamento estão dentro de uma tupla.
contador(4, 5)

valores = [1, 2, 3]
dobra(valores)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :parâmetro i: início de uma contagem
    :parâmetro f: fim de uma contagem
    :parâmetro p: passo de uma contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p
    print("FIM!")


def soma(a=0, b=0, c=0):  # parâmetro opcional
    s = a + b + c
    print(f"A soma vale {s}")


def teste(b):
    global a  # este a passa a ser global e perde o valor a=5 que tinha fora da função
    a = 8
    b += 4
    c = 2
    print(f"a da função vale {a}.")
    print(f"b da função vale {b}.")
    print(f"c da função vale {c}.")

def retorno(a,b,c):
    s = a+b+c
    return s #com a função retorno, é possível igualar uma variável à função

def fatorial (f=1):
    num = 1
    for i in range(f,0,-1):
        num *= i
    return num
    

contador(0, 10, 1)
help(contador)  # aparece a docstring

soma(1, 2)

a = 5
teste(a)
print(f"a fora da função vale {a}")

funcaosoma = retorno(1,2,3)
print(retorno(1,2,3))

# escopo local: variável que funciona somente dentro de uma função
# escopo global: variável que funciona em todo o programa

print(fatorial(4))
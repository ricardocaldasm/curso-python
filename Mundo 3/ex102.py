def fatorial(val=1, show=False):
    """
    Calcula o fatorial de um número
    :param val: O número a ser calculado
    :param calc: (opcional) Mostra o não o cálculo
    :return: Não há
    """
    cont = 1
    for i in range(val, 0, -1):
        cont *= i
        if show:
            if i != 1:
                print(f"{i} x", end=" ")
            else:
                print(f"{i} =", end=" ")
    print(f"{cont}")
    return cont


num = int(input("Digite o valor para cálculo do fatorial: "))
fatorial(num, show=False)

help(fatorial)

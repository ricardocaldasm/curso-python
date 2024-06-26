from time import sleep


def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}.")

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            cont += p
        print("FIM!")
    elif i > f:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ")
            cont -= p
        print("FIM!")


contador(0, 10, 1)
contador(10, 0, 2)

from time import sleep


def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    sleep(0.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ", flush=True)
            cont += p
            sleep(0.5)
        print("FIM!")
        sleep(0.5)
    elif i > f:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")
        sleep(0.5)
    else:
        print("Não é possível realizar uma contagem.")


contador(0, 10, 1)
contador(10, 0, 2)

print("Agora é a sua vez de personalizar a contagem:")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)

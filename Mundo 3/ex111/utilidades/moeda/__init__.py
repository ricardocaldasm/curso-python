def metade(val=0, formato=False):
    met = val / 2
    return met if formato is False else moeda(met)


def dobrar(val=0, formato=False):
    dob = val * 2
    return dob if formato is False else moeda(dob)


def aumentar(val=0, tx=0, formato=False):
    aument = (1 + (tx / 100)) * val
    return aument if formato is False else moeda(aument)


def diminuir(val=0, tx=0, formato=False):
    dimin = (1 - (tx / 100)) * val
    return dimin if formato is False else moeda(dimin)


def moeda(val=0, cifrao="R$"):
    return f"{cifrao}{val:.2f}".replace(".", ",")


def resumo(val=0, tx=0, formato=False):
    print("-" * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(val)}")
    # \t é uma tabulação, para valores serem formatados como tabela
    print(f"Dobro do preço: \t{dobrar(val, True)}")
    print(f"Metade do preço: \t{metade(val, True)}")
    print(f"{tx}% de aumento: \t{aumentar(val,tx,True)}")
    print(f"{tx}% de redução: \t{diminuir(val,tx,True)}")

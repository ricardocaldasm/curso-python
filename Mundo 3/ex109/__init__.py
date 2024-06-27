def metade(val=0, formato=False):
    met = val / 2
    return met if formato is False else moeda(met)


def dobrar(val=0, formato=False):
    dob = val * 2
    return dob if formato is False else moeda(dob)


def aumentar(val=0, tx=100, formato=False):
    aument = (1 + (tx / 100)) * val
    return aument if formato is False else moeda(aument)


def diminuir(val=0, tx=100, formato=False):
    dimin = (1 - (tx / 100)) * val
    return dimin if formato is False else moeda(dimin)


def moeda(val=0, cifrao="R$"):
    return f"{cifrao}{val:.2f}".replace(".", ",")

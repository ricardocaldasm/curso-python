def metade(val=0):
    met = val / 2
    return met


def dobrar(val=0):
    dob = val * 2
    return dob


def aumentar(val=0, tx=100):
    aument = (1 + (tx / 100)) * val
    return aument


def diminuir(val=0, tx=100):
    dimin = (1 - (tx / 100)) * val
    return dimin

import ex108

preco = float(input("Digite o preço: R$"))
taxa = float(input("Digite a taxa em %: "))
print(f"{ex108.moeda(ex108.aumentar(preco, taxa))}")
print(f"{ex108.moeda(ex108.diminuir(preco, taxa))}")
print(f"{ex108.moeda(ex108.dobrar(preco))}")
print(f"{ex108.moeda(ex108.metade(preco))}")

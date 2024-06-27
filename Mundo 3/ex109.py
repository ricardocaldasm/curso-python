import ex109

preco = float(input("Digite o preço: R$"))
taxa = float(input("Digite a taxa em %: "))
print(f"{ex109.aumentar(preco, taxa, True)}")
print(f"{ex109.diminuir(preco, taxa, True)}")
print(f"{ex109.dobrar(preco, True)}")
print(f"{ex109.metade(preco, True)}")

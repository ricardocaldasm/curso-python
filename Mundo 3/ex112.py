from ex112.utilidades import moeda, dado

preco = dado.leiadinheiro("Digite o preço: R$")
taxa = float(input("Digite a taxa em %: "))
moeda.resumo(preco, taxa)

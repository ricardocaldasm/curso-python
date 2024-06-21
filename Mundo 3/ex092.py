from datetime import datetime

dados = dict()

dados["nome"] = str(input("Nome: "))
ano = int(input("Digite o ano de nascimento: "))
dados["idade"] = datetime.now().year - ano
dados["carteira"] = int(input("Carteira de trabalho (0 não tem): "))
if dados["carteira"] != 0:
    dados["contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário: R$"))
    dados["aposentadoria"] = (dados["contratação"] + 35) - datetime.now().year + dados["idade"]

for k,v in dados.items():
    print(f'{k} tem o valor {v}.')
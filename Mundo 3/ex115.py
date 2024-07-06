from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = "lista.txt"

if arqexiste(arq):
    print("Arquivo encontrado com sucesso.")
else:
    print("Arquivo não existe.")
    criararq(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Pessoas", "Sair do Sistema"])
    if resposta == 1:
        lerarq(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do programa.")
        break
    else:
        print("Digite uma opção válida.")

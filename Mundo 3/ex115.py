from ex115.lib.interface import *
from ex115.lib.arquivo import *
import os

arq = "lista.txt"

if arqexiste(arq):
    print("Arquivo encontrado com sucesso.")
else:
    print("Arquivo não existe.")

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Pessoas", "Sair do Sistema"])
    if resposta == 1:
        cabecalho("Opção 1")
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do programa.")
        break
    else:
        print("Digite uma opção válida.")

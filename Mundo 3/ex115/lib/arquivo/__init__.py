from ex115.lib.interface import *


def arqexiste(arquivo):
    import os

    os.chdir(
        r"C:\Users\riccm\OneDrive\Documentos\Cursos\Curso em Vídeo\curso-python\Mundo 3\ex115"
    )
    try:
        abrir = open(arquivo, "rt")
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arquivo):
    try:
        abrir = open(arquivo, "+wt")
        abrir.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {arquivo} criado com sucesso.")


def lerarq(arquivo):
    try:
        abrir = open(arquivo, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        # print(abrir.read())  # readlines para mostrar em forma de lista
        for linha in abrir:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        abrir.close()


def cadastrar(arquivo, nome="desconhecido", idade=0):
    try:
        abrir = open(arquivo, "at")
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            abrir.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro ao escrever os dados.")
        else:
            print(f"Novo registro de {nome} adicionado.")
            abrir.close()

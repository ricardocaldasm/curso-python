def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, v in enumerate(lista):
        print(f"{i+1} - {v}")
    print(linha())
    opc = leiaint("Sua Opção: ")
    return opc


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("Erro: usuário não digitou um número inteiro válido.")
            continue  # continue joga para o while novamente
        except KeyboardInterrupt:
            print("Usuário não digitou nenhum valor.")
            return 0
        else:
            return num

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'")
    help(com)


def titulo(msg):
    tam = len(msg)
    print("~" * tam)
    print(msg)
    print("~" * tam)


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP")
    comando = str(input("Função ou biblioteca (digite 'fim' para encerrar): ")).lower().strip()
    if comando in "fim":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO")

def leiadinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f'"{entrada}" é um valor inválido.')
        else:
            return float(entrada)

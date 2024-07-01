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
        
def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("Erro: usuário não digitou um número real válido.")
            continue  # continue joga para o while novamente
        except KeyboardInterrupt:
            print("Usuário não digitou nenhum valor.")
            return 0
        else:
            return num
        
valorint = leiaint("Digite um valor inteiro: ")
valorfloat = leiafloat("Digite um valor real: ")
print(f"O valor inteiro digitado foi {valorint} e o valor real foi {valorfloat}.")
exp = str(input("Digite a expressão: "))
lista = []
for i in exp:
    if i == "(":
        lista.append("(")
    elif i == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está errada")

lista = (
    "APRENDER",
    "PROGRAMAR",
    "LINGUAGEM",
    "PYTHON",
    "CURSO",
    "GRATIS",
    "ESTUDAR",
    "PRATICAR",
    "TRABALHAR",
    "MERCADO",
    "PROGRAMADOR",
    "FUTURO",
)

for palavra in lista:
    print(f"\nNa palavra {palavra} temos as vogais", end=" ")
    for letra in palavra:
        if letra in "AEIOU":
            print(letra, end=" ")

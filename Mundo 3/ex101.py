def voto(n):
    from datetime import date

    idade = date.today().year - n
    if idade < 16:
        print(f"Com {idade} anos: NÂO VOTA")
    elif 16 <= idade < 18 or idade >= 70:
        print(f"Com {idade} anos: VOTO FACULTATIVO")
    else:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO")


ano = int(input("Em que ano você nasceu? "))
voto(ano)

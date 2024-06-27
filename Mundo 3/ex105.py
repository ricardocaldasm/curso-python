def notas(*val, sit=False):
    dicio = dict()
    maior = menor = soma = 0
    for i, v in enumerate(val):
        soma += v 
        if i == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    media = soma / len(val)
    dicio["total"] = len(val)
    dicio["maior"] = maior #pode usar max(val)
    dicio["menor"] = menor #pode usar min(val)
    dicio["média"] = media #pode usar sum(val)/len(val)
    if sit:
        if media < 5:
            dicio["situação"] = "Reprovado"
        elif 5 <= media < 7:
            dicio["situação"] = "Recuperação"
        else:
            dicio["situação"] = "Aprovado"

    return dicio


resp = notas(10, 8, 10, sit=True)
print(resp)

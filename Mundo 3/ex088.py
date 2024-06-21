from random import randint

bilhete = list()
jogo = list()

qnt = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(0, qnt):
    while True:
        num = randint(1, 60)
        if num not in bilhete:
            bilhete.append(num)
        if len(bilhete) == 6:
            break
    bilhete.sort()
    jogo.append(bilhete[:])
    bilhete.clear()

for i, j in enumerate(jogo):
    print(f"Jogo {i+1}: {j}")

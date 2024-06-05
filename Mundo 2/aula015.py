from time import sleep

cont = 1

while True: #loop infinito até entrar o comando break
    print(cont)
    cont += 1
    sleep(0.1) #não é possível usar sleep com end = ''
    break

print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    s += n
    
print(f'A soma dos numeros foi de {s:.2f}') #f string
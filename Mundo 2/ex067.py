
while True:
    num = int(input('Quer ver tabuada de qual valor? '))
    if num == 0:
        break
    for i in range (1,11):
        print(f'{num} x {i} = {num*i}')
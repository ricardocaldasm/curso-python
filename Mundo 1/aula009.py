frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:10])
print(frase[15:])
print(frase[:15:2])
print(frase[::3])
print(frase.count('o'))
print(frase.upper())
print(len(frase))
print(frase.replace('Python', 'Android')) #replace não muda a string, pois não está recebendo
#frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.split()) 
dividido = frase.split()
print(dividido[2][3]) #terceira palavra, quarta letra

print('''Teste para
pular linha no Python''')


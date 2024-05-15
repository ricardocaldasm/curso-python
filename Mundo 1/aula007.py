print('Oi'*5)
print('-'*20)
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
#:20 aparece em 20 caracteres; :>20 ou :<20 centraliza esq/dir; :^20 centraliza meio;
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma é {}'.format(n1+n2),end=' ') #função para nãoi quebrar a linha
print('Não quebra \n a linha') #\n quebra a linha

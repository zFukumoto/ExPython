# Faça um programa que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece a última vez
msg = str(input('Digite uma frase: ')).lower().strip()
print('A letra "a" aparece {} vezes na frase.'
      .format(msg.count('a')))
print('A primeira letra "a" apareceu na posição {}'
      .format(msg.find('a')+1))
print('A última letra "a" apareceu na posição {}'
      .format(msg.rfind('a')+1))
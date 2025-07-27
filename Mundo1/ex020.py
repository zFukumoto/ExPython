# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalho dos alunos. Fala um programa que leia os nomes dos quatro alunos
# e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terciro Aluno: '))
a4 = str(input('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: {}'
      .format(lista))
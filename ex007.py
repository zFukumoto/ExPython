# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
nota1 = float(input('Digite a sua 1ª Nota:'))
nota2 = float(input('Digite a sua 2ª Nota:'))
print('A média das Notas: {:.1f}\nSoma das Notas: {:.1f}'
       .format(((nota1+nota2)/2), (nota1+nota2)))
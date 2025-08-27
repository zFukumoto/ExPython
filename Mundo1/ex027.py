# Faça um programa que leia o nome completo de uma pessoa, mostrando em 
# seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()
print('Nome Completo: {}'
      .format(nome))
print('Primeiro nome: {}'
      .format(nomes[0]))
print('Último nome: {}'
      .format(nomes[len(nomes)-1]))
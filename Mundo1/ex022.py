# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maisúculas e minúsculas
# Quantas letras tem ao todo (Sem contar os espaços)
# Quantas tem o primeiro nome
nome = str(input('Digite seu nome Completo: ')).strip()
letra = nome.split()
print('Nome em Maiúsculo:',nome.upper())
print('Nome em Minúsculo:',nome.lower())
print('Seu nome possui {} letras'
      .format(len(nome.replace(' ', '')))) 
# Poderia ser feito com "- nome.count(' ')))"
print('{} possui {} letras'
      .format(letra[0],len(letra[0])))
# print('Seu primeiro nome tem {} letras'.
#     .format(nome.find(' ')))
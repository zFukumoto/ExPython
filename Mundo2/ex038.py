# Escreva um programa que leia dois números inteiros e compare-os, 
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
n1 = int(input('\033[0;34mDigite um \033[0;36mNúmero Inteiro \033[0;34mqualquer: \033[m'))
n2 = int(input('\033[0;34mDigite \033[0;36mOutro \033[0;34m: \033[m'))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
if n1 > n2:
    print('{} é maior que {}'
          .format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'
          .format(n2, n1))
else:
    print('{} é igual a {}'
          .format(n1, n2))
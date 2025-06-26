# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
msg = int(input('Diga um Valor:'))
print('Número escolhido: {} \nAntecessor: {}\nSucessor: {}'
      .format(msg, (msg-1), (msg+1)))
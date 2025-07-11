# Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosse e tange desse ângulo.
from math import radians, sin, cos, tan
msg = float(input('Fale um angulo: '))
print('O seno vale {:.2f}.\nO cosseno vale {:.2f}.\nA tangente vale {:.2f}.'
      .format(sin(radians(msg)), cos(radians(msg)), tan(radians(msg))))
# Faça um programa que leia o comprimento do cateto oposto e do cateo 
# adjacente de um triângulo. calcule e mostre o comprimento da hipotenusa.
from math import hypot
catetoa = float(input('Qual o valor do Cateto Adjacente? '))
catetoo = float(input('Qual o valor do Cateto Oposto? '))
print('A hipotenusa desse triângulo vale {:.2f}'
      .format(hypot(catetoa, catetoo)))
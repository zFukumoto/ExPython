# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais;
# - ISÓSCELES: dois lados iguais;
# - ESCALENO: todos os lados diferentes.
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
print('Digite 3 valores inteiros diferentes.')
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('Os segmentos acima formam um triângulo ', end='')
     if r1 == r2 == r3:
          print('EQUILÁTERO!')
     elif r1 != r2 != r3 != r1:
          print('ESCALENO!')
     else:
          print('ISÓSCELES!'),
else:
     print('Os segmentos acima NÃO PODEM formar um triângulo')
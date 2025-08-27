# Faça um programa que calcule a soma entre todos os número impares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
soma = 0
for n in range(0, 500, +3):
    soma += n
print('Todos os números múltiplos de três entre 1 e 500 somados é: {}'
      .format(soma))
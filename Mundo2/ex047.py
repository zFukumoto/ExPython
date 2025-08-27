# Crie um programa que mostre na tela todos os números pares que estão no intervalo
# entre 1 e 50.
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
print('Esses são todos os números pares entre 1 e 50:')
for par in range(0, 51, +2):
    print(par)
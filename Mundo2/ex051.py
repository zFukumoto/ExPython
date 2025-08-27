# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
# final, mostre os 10 primeiros termos dessa progressão.
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '
          .format(c), end='-> ')
print('Fim')
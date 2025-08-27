# Faça um programa que leia um número inteiro e diga se ele é ou não um número
# primo.
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
total = 0
n = int(input('Digite um número inteiro: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end= '')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '
          .format(c), end= '')
print('\n\033[mO número {} foi divisível {} vezes'
      .format(n, total))
if total == 2:
    print('E por isso ele \033[32mÉ PRIMO')
else:
    print('E por isso ele \033[31mNÃO é PRIMO')
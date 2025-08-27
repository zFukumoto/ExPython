# Escreva um programa que leia um númerio inteiro qualquer e peça para o 
# usuário escolher qual será a base da conversão.
# 1 = Biário
# 2 = Octal
# 3 = Hexadecimal
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
num = int(input('Digite um Número Inteiro qualquer: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
print('''Escolha uma das bases para conversão:'
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
op = int(input('Sua Opção: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'
          .format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertitdo para OCTAL é igual a {}'
          .format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'
          .format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
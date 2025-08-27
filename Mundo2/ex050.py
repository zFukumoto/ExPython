# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor for ímpar desconsidere-o.
soma = 0
cont = 0
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 15)
print('Digite 6 números Inteiros abaixo.')
for c in range(1, 7):
    num = int(input('{}º Valor: '
                    .format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 15)
print('{} número(s) PAR(ES) informado(s), sendo a {} soma deles'
      .format(cont, soma))
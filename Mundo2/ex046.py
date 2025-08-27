# Faça um programa que mostre na tela uma contagem regressiva para o estouro 
# de fogos de artifícios de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
print('Os fogos vão começar em:')
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('AÊÊÊÊ!!!')
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
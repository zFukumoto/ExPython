# Escreva um programa que faça o computador "pensar" entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.
from random import randint
from time import sleep
print('\033[0;33m=-=\033[m' * 16)
print('\033[0;34mEstou pensando em um número de 0 a 5. Tente adivinhar...\033[m')
print('\033[0;33m=-=\033[m' * 16)
res = int(input('\033[0;34mEm que número eu pensei?\033[m '))
print('\033[0;33m=-=\033[m' * 16)
print('\033[0;34mProcessando...\033[m')
n = randint(0,5)
sleep(1)
if res == n:
    print('\033[0;32mParabéns\033[0;34m!!! eu estava pensando no número \033[0;32m{}\033[m'
          .format(n))
else:
    print('\033[0;31mQue pena\033[0;34m, eu pensei no número: \033[0;32m{}\033[0;34m e não no \033[0;31m{}\033[m'
          .format(n, res))
# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
escolha = randint(1,3)
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
print('\033[0;36mJOKENPÔ\033[m')
print('[ 1 ] - Pedra')
print('[ 2 ] - Papel')
print('[ 3 ] - Tesoura')
resposta = int(input('\033[0;34mDigite o \033[0;36mnúmero \033[0;34mda sua escolha: \033[m'))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
sleep(0.3)
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PÔ')
sleep(0.2)
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
if resposta == 3:
    if escolha == 3:
        print('Empatamos!!! Escolhi Tesoura!')
    elif escolha == 2:
        print('Você me venceu!!! Escolhi Papel!')
    elif escolha == 1:
        print('Você perdeu!!! Escolhi Pedra!'),
elif resposta == 2:
    if escolha == 3:
        print('Empatamos!!! Escolhi Papel!')
    elif escolha == 2:
        print('Você me venceu!!! Escolhi Pedra!')
    elif escolha == 1:
        print('Você perdeu!!! Escolhi Tesoura!'),
elif resposta == 1:
    if escolha == 3:
        print('Empatamos!!! Escolhi Pedra!')
    elif escolha == 2:
        print('Você me venceu!!! Escolhi Tesoura!')
    elif escolha == 1:
        print('Você perdeu!!! Escolhi Papel!'),
else:
    print('Jogada Inválida!')
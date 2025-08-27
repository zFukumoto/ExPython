# Faça um programa que leia o ano de nascimento de um jovem e informe, de 
# acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se aliastar;
# - Se já passou do tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou que passou do prazo
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
nas = int(input('Ano de Nascimento: '))
print('Qual seu gênero biológico?')
print('[ 1 ] - Masculino')
print('[ 2 ] - Feminino')
op = int(input('Sua Opção: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
from datetime import date
ano = date.today().year
idade = ano - nas
print('Quem nasceu em {} tem {} ano(s) em {}.'
      .format(nas, idade, ano))
if idade == 18 and op == 1:
    print('Você tem que se alistar IMEDIATAMENTE.'),
elif idade < 18 and op == 1:
    saldo = 18 - idade
    idade2 = idade - 18
    idade3 = ano - idade2
    print('Ainda falta {} ano(s) para seu alistamento.'
          .format(saldo))
    print('Ele ocorrerá em {}.'
          .format(idade3)),
elif idade > 18 and op == 1:
    idade2 = idade - 18
    saldo = ano - idade2
    print('Seu alistamento foi em {}.'
          .format(saldo)),
elif idade > 18 and op == 2:
    print('Você não precisou se alistar.'),
else:
    print('Você não precisará se alistar.')
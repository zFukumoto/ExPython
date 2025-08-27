# A Confederação Nacional de Natação precisa de um programa que leia o ano
# nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 ANOS: JUNIOR
# Até 25 anos: SENIOR
# Acima: MASTER
from datetime import date
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
nas = int(input('Ano de Nascimento: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
idade = date.today().year - nas
print('O atleta tem {} anos.'
      .format(idade))
if idade <= 9:
    print('Classificação: MIRIM'),
elif idade <= 14:
    print('Classificação: INFANTIL'),
elif idade <= 19:
    print('Classificação: JUNIOR'),
elif idade == 20:
    print('Classificação: SENIOR'),
else:
    print('Classificação: MASTER')
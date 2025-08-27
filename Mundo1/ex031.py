# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até
# 200Km e R$0,45 para viagens mais longas.
dis = float(input('Digite quantos Km de distância sua viagem tem: '))
if dis <= 200.00:
    v1 = dis * 0.50
    print('O valor dessa viagem será de R${:.2f}.'
          .format(v1))
else:
    v2 = dis * 0.45
    print('O valor dessa viagem será de R${:.2f}.'
          .format(v2))
print('Tenha uma Boa viagem!!!')
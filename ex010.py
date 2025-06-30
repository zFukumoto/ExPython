# Crie um programa que leia quanto dinheiro uma pessoa tem na carteia e mostre quantos Dólares ela pode comprar
# Considere U$1,00 = R$3,27
msg = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar U${:.2f}.'
     .format(msg, (msg/3.27)))
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
msg = float(input('Para saber o quanto você econom100izou com 5% de desconto, digite o preço do produto: R$'))
print('Você está economizando R${:.2f}, o preço final ficará: R${:.2f}'
      .format((msg*5/100), (msg-(msg*5/100))))
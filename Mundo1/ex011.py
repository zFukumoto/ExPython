# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de inta pinta uma área de 2m²
larg = float(input('Quanto de largura (em metros) sua parede tem? '))
alt = float(input('Quanto de altura (em metros) sua parede tem: '))
print('Sua parede tem uma área total de {:.2f}m².\nPrecisará de {:.2f}L de tinta para pinta-la totalmente.'
      .format((larg*alt), ((larg*alt)/2)))

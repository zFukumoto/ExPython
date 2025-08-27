# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80Km/h, mostre uma mensagem que ele foi multado. A multa vai custar R$7.00
# Km acima do limite
vel = float(input('Quantos Km/h você estava dirigindo? '))
multa = (vel - 80.0) * 7.0
if vel <= 80.0:
    print('Está tudo bem, você estava dentro do limite de velocidade')
else:
    print('Você ultrapassou o limite de velocidade e será multado')
    print('Você deverá pagar R${:.2f} de multa'
          .format(multa))
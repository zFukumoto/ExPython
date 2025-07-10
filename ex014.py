# Escreva um programa que converta uma temperatura digitada em ºC para ºF
msg = float(input('Informe a temperatura em ºC:'))
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF'
    .format(msg, msg*9/5+32))
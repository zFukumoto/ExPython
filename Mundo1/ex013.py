# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
msg = float(input('Qual seu salário atual? R$:'))
print('Aumento de 15% nos salários.\nSeu salário: R${:.2f}.\nAumento de R${:.2f}.\nSalário final: R${:.2f}'
      .format(msg, ((msg*115/100)-msg), (msg*115/100)))

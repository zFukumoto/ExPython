# Escreva um programa que pergunte o salário de um funcionário e calcule o
# o valor de seu aumento. Para salários superiores a R$1.250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o seu salário? '))
if sal > 1250:
    n1 = sal * (10 / 100) + sal
    print('Seu novo salário será R${:.2f}'
          .format(n1))
else:
    n2 = sal * (15 / 100) + sal
    print('Seu novo salário será R${:.2f}'
          .format(n2))
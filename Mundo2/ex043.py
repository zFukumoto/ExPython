# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 40: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
altura = float(input('Qual sua altura (m)? '))
peso = float(input('Qual seu peso (Kg)? '))
imc = peso / altura ** 2
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
print('Seu IMC é de {:.1f}'
      .format(imc)),
if imc < 18.5:
    print('Você está ABAIXO do Peso Ideal'),
elif 18.5 <= imc < 25:
    print('Você ESTÁ no Peso Ideal'),
elif 25 <= imc < 30:
    print('Você está ACIMA do Peso Ideal'),
elif 30 <= imc < 40:
    print('Você está na OBESIDADE, Cuidado!!!'),
else:
    print('Você está ma OBESIDADE MÓRBIDA, procure um médico!!!')
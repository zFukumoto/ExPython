# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
media = ( n1 + n2) / 2
print('Sua média é {:.1f}'
      .format(media))
if media < 5.0:
    print('Você foi REPROVADO.')
elif media > 5.0 and media < 5.9:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você foi APROVADO.')
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou
# não com o nome 'Santo'
cidade = str(input('Digite o Nome de uma Cidade: ')).strip()
print(cidade[:6].capitalize() == 'Santo')
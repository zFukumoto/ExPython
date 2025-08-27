# Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que
# agora utilizando um 'for'
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 11)
num = int(input('Digite um número para ver sua Tabuada: '))
for tab in range(0 ,11):
    print('{} x {:2} = {}'
          .format(num, tab, num*tab))
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% juros
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
preço = int(input('Digite o valor do produto R$:'))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
print('Escolha o método de Pagamento:')
print('[ 1 ] Á vista em Dinheiro/Cheque (10% de Desconto)')
print('[ 2 ] Á vista no Cartão Débito (5% de Desconto)')
print('[ 3 ] Em até 2x no cartão Crédito (Preço Normal)')
print('[ 4 ] De 3x a 6x no Cartão Crédito (20% de Juros)')
op = int(input('Qual o método de pagamento? '))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
if op == 1 :
    desc = preço - preço * 10 / 100
    print('O produto custará R${:.2f}'
          .format(desc))
elif op == 2:
    desc = preço - preço * 5 / 100
    print('O produto custará R${:.2f}'
          .format(desc))
elif op == 3:
    print('Você deseja parcelar sua compra em 2x?')
    print('- Sim')
    print('- Não')
    parcela = str(input('Escolha sua opção: ')).strip().capitalize()
    print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
    if parcela == 'Sim':
        parcela2 = preço / 2
        print('O valor de cada parcela será de R$:{:.2f}'
              .format(parcela2))
    if parcela == 'Não':
        print('O valor total da compra é de R$:{:.2f}'
              .format(preço)),
elif op == 4:
    preço2 = preço + preço * 20 / 100
    print('Em quantas parcelas você deseja pagar (3, 4, 5 ou 6)?')
    parcela = int(input('Escola sua opção: '))
    preço3 = preço / parcela
    print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
    print('O valor total do produto ficará R$:{:.2f}'
          .format(preço2))
    print('Cada parcela ficará R$:{:.2f}'
          .format(preço3)),
else:
    print('Opção inválida, por favor tente novamente.')
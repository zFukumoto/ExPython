# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O
# programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado.
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
casa = float(input('\033[0;34mDigite o \033[0;36mValor \033[0;34mda Casa: \033[mR$'))
sal = float(input('\033[0;34mDigite o seu \033[0;36mSalário \033[0;34m: \033[mR$'))
anos = int(input('\033[0;34mDigite em quantos \033[0;36manos \033[0;34mvocê quer pagar? \033[m'))
print('\033[0;33m=\033[0;35m-\033[0;33m=\033[m' * 20)
parcela = casa / ( anos * 12 )
print('\033[0;34mPara pagar uma casa de \033[0;36m{:.2f} \033[0;34mem \033[0;36m{} anos \033[0;34m a parcela será de \033[0;36mR$:{:.2f}\033[m'
      .format(casa, anos, parcela))
if parcela <= sal * 30 / 100:
    print('\033[0;34mEmpréstimo \033[0;32mCONCEDIDO \033[0;34m')
else:
    print('\033[0;34mEmpréstimo \033[0;31mNEGADO \033[0;34m')
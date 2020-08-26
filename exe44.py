#coding: utf-8

#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#* À vista dinheiro/cheque: 10% de desconto
#* À vista no cartão: 5% de desconto
#* Em até 2x no cartão: Preço normal
#* 3x ou mais no cartão: 20% de juros
print('\033[1;32m''-_*=*_-'*30, '\033[m')
print()
print('\033[1;30m'' '*20, 'Lojas Wecol')
print()
valor_compras = float(input('Total das compras: R$'))
print('Qual será a forma de pagamento?')
print('Escolha a opção desejada.''\033[1;32m')
print('[ 1 ] Á vista no dinheiro ou cheque: 10% desconto')
print('[ 2 ] Á vista no cartão: 5% de desconto.')
print('[ 3 ] Em até 2x no cartão: Preço normal')
print('[ 4 ] Em 3x ou mais no cartão: 20% de juros''\033[m')
escolha = int(input('\033[1;30m''Sua escolha: '))
print('O total das suas compras é de R${:.2f}'.format(valor_compras))
print('Sua escolha de pagamento foi:')
if escolha == 1:
    print('Pagamento á vista, no dinheiro ou cheque, com 10% de desconto: R${:.2f}'.format(valor_compras - valor_compras*10/100))
elif escolha == 2:
    print('Á vista no cartão, com 5% de desconto: R${:.2f} '.format(valor_compras - (valor_compras * 5/100)))
elif escolha == 3:
    print('2x no cartão de: R${:.2f}'.format(valor_compras / 2))
elif escolha == 4:
    print('Acima de 3x no cartão, com 20% de juros: R${:.2f}'.format(valor_compras + (valor_compras*20/100)))

#coding: utf-8

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar.
#* Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
#################### Programa de simulação de financiamento Habitacional #################################
print('^='*10, 'Análise para financiamento Habitacional', '^='*10)
print()
valor_casa = float(input('\033[1;30m''Informe o valor do imóvel: R$'))
salario = float(input('Informe a renda do comprador: R$'))
tempo_pagar = int(input('Quantos anos de financiamento: '))
prestação = valor_casa/(tempo_pagar*12)
if prestação > salario * 30 / 100:
    print('\033[1;31m''Financiamento Negado!')
else:
    print('\033[1;36m''Financiamento Aprovado!')
print('\033[1;33m''Segue abaixo as informações da simulação:\nTempo total de financiamento de {} meses\nSalário de R${:.2f}\nPrestação no valor de R${:.2f}'.format(tempo_pagar*12, salario, prestação))